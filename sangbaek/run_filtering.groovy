import org.jlab.jnp.hipo4.data.Event;
import org.jlab.jnp.hipo4.io.HipoReader
import org.jlab.jnp.hipo4.io.HipoWriter
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
  evcount.set(0)
}


def mode = "dvcs"

if (args.size()>1){
  if (args[1]=="dvcs" || args[1]=="pi0")  mode = args[1]
  else{
    println("The filtering mode must be dvcs or pi0.")
    println("Halt.")
    return
  }
}
println("filtering $mode events with fiducial cuts...")

def filterEvents = { ev, proc, mod ->
  if (mod == "dvcs") return proc.filterDVCSEvents(ev)
  if (mod == "pi0") return proc.filterPi0Events(ev)
  else return
}

def exe = Executors.newScheduledThreadPool(1)
exe.scheduleWithFixedDelay(debug, 5, 30, TimeUnit.SECONDS)

GParsPool.withPool 12, {
  def reader = new HipoReader()
  reader.open(args[0])
  def writer = new HipoWriter(reader.getSchemaFactory())
  writer.open(outname)

  def jnp_event = new org.jlab.jnp.hipo4.data.Event()

  while(reader.hasNext()) {
    evcount.getAndIncrement()
    reader.nextEvent(jnp_event)
    def data_event = new HipoDataEvent(jnp_event, reader.getSchemaFactory())
    def event = EventConverter.convert(data_event)
    if (filterEvents(event, processor, mode)) {
      writer.addEvent(jnp_event)
    }
  }
  writer.close()
  reader.close()
}

exe.shutdown()
debug()