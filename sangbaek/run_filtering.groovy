import org.jlab.jnp.hipo4.data.Event;
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
import sangbaek.filtering.filtering
import event.Event
import event.EventConverter
import my.Sugar

Sugar.enable()
/////////////////////////////////////////////////////////////////////

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

def outname = args[0].split('/')[-1]

if (outname[-5..-1]!=".hipo"){
  println("The input file name must end with \".hipo\".")
  println("Halt.")
  return
}
println("Filtering $outname..")
outname = outname.substring(0,outname.lastIndexOf(".")) + "_filtered.hipo"
println("Saving filtered file as $outname...\n\n\n")

def processor = new filtering()

def evcount = new AtomicInteger()
def debug = {
  println "event count: "+evcount.get()
//  evcount.set(0)
}

def exe = Executors.newScheduledThreadPool(1)
exe.scheduleWithFixedDelay(debug, 5, 30, TimeUnit.SECONDS)

GParsPool.withPool 12, {
  args.eachParallel{fname->

    def reader = new HipoReader()
    reader.open(fname)
    SchemaFactory schema = reader.getSchemaFactory();
//    def writer = new HipoWriter(schema)
    SchemaFactory writerFactory = schema.reduce(["REC::Particle", "RUN::config", "REC::Event"]);
    writerFactory.addSchema(customSchema)
    def writer = new HipoWriter(writerFactory)

    writer.open(outname)

    BankIterator           iter = new BankIterator(4096);
    BankSelector   dataSelector = new BankSelector(schema.getSchema("REC::Particle"));

    def jnp_event = new org.jlab.jnp.hipo4.data.Event()

    while(reader.hasNext()) {
      evcount.getAndIncrement()
      reader.nextEvent(jnp_event)
      if(!jnp_event.hasBank(reader.getSchemaFactory().getSchema("REC::Particle"))) continue
      def data_event = new HipoDataEvent(jnp_event, reader.getSchemaFactory())
      def event = EventConverter.convert(data_event)
      def partlist = processor.filterGammas(event)//filterEPGs(event)

      if (partlist) {
        dataSelector.getIterator(jnp_event, iter);
        iter.reset()
        def customBank = new Bank(customSchema, partlist.size)
        partlist.eachWithIndex{val, index ->
          iter.addIndex(val)
          customBank.putInt("before", index, val)
        }
        Bank newBank = BankSelector.reduceBank(dataSelector.getBank(), iter);
        jnp_event.remove(dataSelector.getBank().getSchema());
        jnp_event.write(newBank);
        jnp_event.write(customBank)
        writer.addEvent(jnp_event)
      }
    }
    writer.close()
    reader.close()
  }
}

exe.shutdown()
debug()