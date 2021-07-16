package net.clasmit;

import org.jlab.jnp.hipo4.data.Bank;
import org.jlab.jnp.hipo4.io.HipoReader
import org.jlab.jnp.hipo4.io.HipoWriter
import org.jlab.jnp.hipo4.data.SchemaFactory
import org.jlab.jnp.hipo4.operations.BankIterator;
import org.jlab.jnp.hipo4.operations.BankSelector;
import org.jlab.jnp.hipo4.data.Schema
import org.jlab.io.hipo.HipoDataEvent
import org.jlab.io.hipo.HipoDataSource
import org.jlab.groot.data.H1F
import org.jlab.groot.data.H2F
import org.jlab.groot.data.TDirectory
import groovyx.gpars.GParsPool
import groovy.cli.picocli.CliBuilder
import net.clasmit.filtering.filtering
import net.clasmit.event.Event
import net.clasmit.event.EventConverter


def cli = new CliBuilder(usage: 'java -jar target/filter-1.2.jar net.clasmit.particle [--options] file_names')

cli.with {
    h longOpt: 'help', 'Show usage information'
    p longOpt: 'polarity',        defaultValue:'inbending', args: 1, argName: 'polarity',        'inbending| outbending, default is inbending'
    s longOpt: 'start', defaultValue: "0", args: 1, argName: 'starting event', 'starting event count, or percentage, ex) 1000, or 10%%'
    e longOpt: 'end', defaultValue: "-1", args: 1, argName: 'last event', 'last event count, or percentage, ex) 2000, or 20%%'
    t longOpt: 'twophotons', type: boolean, argName: 'requiringTwoPhotons', 'if on, requiring photons'
    eb longOpt: 'eb', type: boolean, argName: 'EB only', 'if on, use eb pid only'
}

def options = cli.parse(args)

if (options.h) {
  cli.usage()
  return
}

def fnames = options.arguments()
def polarity = options.p


def start, end
def start_mode, end_mode

def requirePi0 = options.t
def useEB = options["eb"]

if (options.s=="0"){
  start = "0"
  start_mode = "default"
}

if (options.e=="-1"){
  end = "-1"
  end_mode = "default"
}

if(!start_mode){
  start = options.s
  start_mode = "count"
  if(start.contains("%")) start_mode = "percentage"
}  

if(!end_mode){
  end = options.e
  end_mode = "count"
  if(end.contains("%")) end_mode = "percentage"
}

if (start_mode == "count") start = start as Integer
if (end_mode == "count") end = end as Integer

println("filtering with "+polarity+" polarity option.")

def jsonbank = '''
    {   
        "name": "FILTER::Index",
        "group": 999,
        "item" : 99,
        "info": "test",
        "entries": [
            {"name":"before",      "type":"I", "info":"indices before filtering"},
            {"name":"pcal_sector", "type":"I", "info":"pcal sector"},
            {"name":"ecinner_sector", "type":"I", "info":"ecal inner sector"},
            {"name":"ecouter_sector", "type":"I", "info":"ecal outer sector"},
            {"name":"dc_track_sector", "type":"I", "info":"dc track sector"},
            {"name":"dc1_traj_sector", "type":"I", "info":"dc1 traj sector"},
            {"name":"dc2_traj_sector", "type":"I", "info":"dc2 traj sector"},
            {"name":"dc3_traj_sector", "type":"I", "info":"dc3 traj sector"},
            {"name":"ftof1a_sector", "type":"I", "info":"ftof1a sector"},
            {"name":"ftof1b_sector", "type":"I", "info":"ftof1b sector"},
            {"name":"ftof2_sector", "type":"I", "info":"ftof2 sector"},
            {"name":"htcc_sector", "type":"I", "info":"htcc sector"}
        ]
    }
'''
def customSchema = Schema.fromJsonString(jsonbank)

def outname = fnames[0].split('/')[-1]

if (outname[-5..-1]!=".hipo"){
  println("The input file name must end with \".hipo\".")
  println("Halt.")
  return
}
println("Filtering $outname..")
outname = outname.substring(0,outname.lastIndexOf(".")) + "_filtered_with_DcTof.hipo"
println("Saving filtered file as $outname...\n\n\n")

def processor = new filtering(polarity)

def evcount = 0
def saved = 0
def debug = {evc->
  println("processing "+evc+"-th event")
}

fnames.each{fname->

  def reader = new HipoReader()
  reader.open(fname)
  
  // set up the range of filtering
  def totalEvent = reader.getEventCount()
  if (start == "0" || start == "0%") start = 0
  else if (start_mode =="percentage") start = Math.round(Float.valueOf(start[0..-2])*totalEvent/100)
  if (end == "-1" || end == "100%") end = totalEvent
  else if (end_mode =="percentage") end = Math.round(Float.valueOf(end[0..-2])*totalEvent/100)
  
  println("Requested from events "+start+ " to " + end)

  SchemaFactory schema = reader.getSchemaFactory();
  // SchemaFactory writerFactory = schema.reduce(["REC::Particle", "RUN::config", "REC::Event"]);
  // defining schema with REC::Scintillator
  SchemaFactory writerFactory = schema.reduce(["REC::Particle", "REC::Scintillator", "REC::Traj", "RUN::config", "REC::Event"]);
  if (schema.hasSchema("MC::Particle")) writerFactory = schema.reduce(["REC::Particle", "REC::Scintillator", "REC::Traj", "RUN::config", "REC::Event", "MC::Particle"]);
  writerFactory.addSchema(customSchema)
  def writer = new HipoWriter(writerFactory)

  writer.open(outname)

  BankIterator           iterPart = new BankIterator(4096);
  BankSelector   dataSelectorPart = new BankSelector(schema.getSchema("REC::Particle"));
  // defining iterator and selector for filtering REC::Scintillator
  BankIterator           iterScin = new BankIterator(4096);
  BankSelector   dataSelectorScin = new BankSelector(schema.getSchema("REC::Scintillator"));
  // defining iterator and selector for filtering REC::Traj
  BankIterator           iterTraj = new BankIterator(4096);
  BankSelector   dataSelectorTraj = new BankSelector(schema.getSchema("REC::Traj"));

  def jnp_event = new org.jlab.jnp.hipo4.data.Event()

  def pid

  while(evcount<totalEvent) {

    if (evcount<start){
      evcount++
      continue
    }
    else if (evcount==start) debug(evcount)
    else if (evcount==end) {
      debug(evcount-1)
      break
    }
    else if (evcount%100000==0) debug(evcount)
    
    evcount++
    reader.nextEvent(jnp_event)

    if(!jnp_event.hasBank(reader.getSchemaFactory().getSchema("REC::Particle"))) continue
    def data_event = new HipoDataEvent(jnp_event, reader.getSchemaFactory())
    def event = EventConverter.convert(data_event)
    def partDict = processor.filterEPGs(event, requirePi0, useEB)// get columns of REC::Particle to be saved
    def partList = partDict["pinds"]// get columns of REC::Particle to be saved
    def pidList = partDict["pids"]

    //saves only such columns
    if (partList) {

      saved ++

      dataSelectorPart.getIterator(jnp_event, iterPart);
      iterPart.reset()

      // preparing for REC::Scintillator
      dataSelectorScin.getIterator(jnp_event, iterScin);
      iterScin.reset()

      // preparing for REC::Traj
      dataSelectorTraj.getIterator(jnp_event, iterTraj);
      iterTraj.reset()
      
      // preparing for FILTER::Index
      def customBank = new Bank(customSchema, partList.size)

      //filtering REC::Particle
      partList.eachWithIndex{val, index ->
        iterPart.addIndex(val)
        customBank.putInt("before", index, val) //saving old pindex at FILTER::Index:before
        customBank.putInt("pcal_sector", index, partDict.pcal_sectors[index]) //saving pcal sectors at FILTER::Index:before
        customBank.putInt("ecinner_sector", index, partDict.ecinner_sectors[index]) //saving ec inner sectors at FILTER::Index:before
        customBank.putInt("ecouter_sector", index, partDict.ecouter_sectors[index]) //saving ec outer sectors at FILTER::Index:before
        customBank.putInt("dc_track_sector", index, partDict.dc_track_sectors[index]) //saving dc track sectors at FILTER::Index:before
        customBank.putInt("dc1_traj_sector", index, partDict.dc1_traj_sectors[index]) //saving dc1 traj sectors at FILTER::Index:before
        customBank.putInt("dc2_traj_sector", index, partDict.dc2_traj_sectors[index]) //saving dc2 traj sectors at FILTER::Index:before
        customBank.putInt("dc3_traj_sector", index, partDict.dc3_traj_sectors[index]) //saving dc3 traj sectors at FILTER::Index:before
        customBank.putInt("ftof1a_sector", index, partDict.ftof1a_sectors[index]) //saving ftof 1a sectors at FILTER::Index:before
        customBank.putInt("ftof1b_sector", index, partDict.ftof1b_sectors[index]) //saving ftof 1b sectors at FILTER::Index:before
        customBank.putInt("ftof2_sector", index, partDict.ftof2_sectors[index]) //saving ftof 2 sectors at FILTER::Index:before
        customBank.putInt("htcc_sector", index, partDict.htcc_sectors[index]) //saving cherenkov sectors at FILTER::Index:before
      }

      //filtering REC::Scintillator
      Bank recScinBank = dataSelectorScin.getBank()
      if (recScinBank.getRows()>0){
        (0..<recScinBank.getRows()).each{
          def pindex = recScinBank.getInt("pindex", it)
          if (partList.contains(pindex)){
            pid = pidList[partList.indexOf(pindex)]
            if (pid == 2212) iterScin.addIndex(it)
          }
        }
      }

      //filtering REC::Traj
      Bank recTrajBank = dataSelectorTraj.getBank()
      if (recTrajBank.getRows()>0){
        (0..<recTrajBank.getRows()).each{
          def pindex = recTrajBank.getInt("pindex", it)
          if (partList.contains(pindex)){
            pid = pidList[partList.indexOf(pindex)]
            if (pid == 2212) iterTraj.addIndex(it)
          }
        }
      }


      //saving filtered REC::Particle
      Bank newPartBank = BankSelector.reduceBank(dataSelectorPart.getBank(), iterPart);
      jnp_event.remove(dataSelectorPart.getBank().getSchema());
      jnp_event.write(newPartBank); // REC::Particle only passed filtering.filterEPGs

      //saving FILTER::Index bank
      jnp_event.write(customBank)

      //saving filtered REC::Scintillator
      Bank newScinBank = BankSelector.reduceBank(recScinBank, iterScin);
      jnp_event.remove(dataSelectorScin.getBank().getSchema());
      jnp_event.write(newScinBank);

      //saving filtered REC::Traj
      Bank newTrajBank = BankSelector.reduceBank(recTrajBank, iterTraj);
      jnp_event.remove(dataSelectorTraj.getBank().getSchema());
      jnp_event.write(newTrajBank);

      writer.addEvent(jnp_event)
    }
  }
  print("Saved "+saved +" events out of ")
  println(end-start + " requested events")
  writer.close()
  reader.close()
}