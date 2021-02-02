package net.clasmit;

// import org.jlab.jnp.hipo4.data.Event;
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
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.Executors
import java.util.concurrent.ScheduledExecutorService
import java.util.concurrent.TimeUnit
import java.util.concurrent.atomic.AtomicInteger
import groovy.cli.picocli.CliBuilder
import net.clasmit.filtering.filtering
import net.clasmit.event.Event
import net.clasmit.event.EventConverter


def cli = new CliBuilder(usage: 'java -jar target/filter-1.1.jar -[p] polarity file_names')

cli.with {
    h longOpt: 'help', 'Show usage information'
    p longOpt: 'polarity',        defaultValue:'inbending', args: 1, argName: 'polarity',        'inbending| outbending, default is inbending'
}

def options = cli.parse(args)
if (options.h) {
  cli.usage()
  return
}
def fnames = options.arguments()
def polarity = options.p

println("filtering with "+polarity+" polarity option.")

def jsonbank = '''
    {   
        "name": "FILTER::Index",
        "group": 999,
        "item" : 99,
        "info": "test",
        "entries": [
            {"name":"before",      "type":"I", "info":"indices before filtering"}
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
outname = outname.substring(0,outname.lastIndexOf(".")) + "_filtered.hipo"
println("Saving filtered file as $outname...\n\n\n")

def processor = new filtering(polarity)

def evcount = new AtomicInteger()
def debug = {
  println "event count: "+evcount.get()
//  evcount.set(0)
}

def exe = Executors.newScheduledThreadPool(1)
exe.scheduleWithFixedDelay(debug, 5, 30, TimeUnit.SECONDS)

GParsPool.withPool 12, {
  fnames.eachParallel{fname->

    def reader = new HipoReader()
    reader.open(fname)
    SchemaFactory schema = reader.getSchemaFactory();
    SchemaFactory writerFactory = schema.reduce(["REC::Particle", "RUN::config", "REC::Event"]);
    // // defining schema with REC::Scintillator
    // SchemaFactory writerFactory = schema.reduce(["REC::Particle", "REC::Scintillator", "RUN::config", "REC::Event"]);
    writerFactory.addSchema(customSchema)
    def writer = new HipoWriter(writerFactory)

    writer.open(outname)

    BankIterator           iterPart = new BankIterator(4096);
    BankSelector   dataSelectorPart = new BankSelector(schema.getSchema("REC::Particle"));
    // // defining iterator and selector for filtering REC::Scintillator
    // BankIterator           iterScin = new BankIterator(4096);
    // BankSelector   dataSelectorScin = new BankSelector(schema.getSchema("REC::Scintillator"));

    def jnp_event = new org.jlab.jnp.hipo4.data.Event()

    while(reader.hasNext()) {
      evcount.getAndIncrement()
      reader.nextEvent(jnp_event)
      if(!jnp_event.hasBank(reader.getSchemaFactory().getSchema("REC::Particle"))) continue
      def data_event = new HipoDataEvent(jnp_event, reader.getSchemaFactory())
      def event = EventConverter.convert(data_event)
      def partList = processor.filterEPGs(event)// get columns of REC::Particle to be saved
      //saves only such columns
      if (partList) {
        dataSelectorPart.getIterator(jnp_event, iterPart);
        iterPart.reset()

        // // preparing for REC::Scintillator
        // dataSelectorScin.getIterator(jnp_event, iterScin);
        // iterScin.reset()
        
        // preparing for FILTER::Index
        def customBank = new Bank(customSchema, partList.size)

        //filtering REC::Particle
        partList.eachWithIndex{val, index ->
          iterPart.addIndex(val)
          customBank.putInt("before", index, val) //saving old pindex at FILTER::Index:before
        }

        // //filtering REC::Scintillator
        // Bank recScinBank = dataSelectorScin.getBank()
        // if (recScinBank.getRows()>0){
        //   (0..<recScinBank.getRows()).each{
        //     def pindex = recScinBank.getInt("pindex", it)
        //     if (partList.contains(pindex)) iterScin.addIndex(it)
        //   }
        // }

        //saving filtered REC::Particle
        Bank newPartBank = BankSelector.reduceBank(dataSelectorPart.getBank(), iterPart);
        jnp_event.remove(dataSelectorPart.getBank().getSchema());
        jnp_event.write(newPartBank); // REC::Particle only passed filtering.filterEPGs

        jnp_event.write(customBank)//saving FILTER::Index bank

        // //saving filtered REC::Scintillator
        // Bank newScinScin = BankSelector.reduceBank(recScinBank, iterScin);
        // jnp_event.remove(dataSelectorScin.getBank().getSchema());
        // jnp_event.write(newScinScin);
        writer.addEvent(jnp_event)
      }
    }
    writer.close()
    reader.close()
  }
}

exe.shutdown()
debug()