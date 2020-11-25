import org.jlab.io.hipo.HipoDataSource
import org.jlab.io.hipo.HipoDataSync
import org.jlab.groot.data.H1F
import org.jlab.groot.data.H2F
import org.jlab.groot.data.TDirectory
import groovyx.gpars.GParsPool
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.Executors
import java.util.concurrent.ScheduledExecutorService
import java.util.concurrent.TimeUnit
import java.util.concurrent.atomic.AtomicInteger
import sangbaek.filtering
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
  def reader = new HipoDataSource()
  reader.open(args[0])
  def writer = new HipoDataSync()
  writer.open(outname)

  while(reader.hasEvent()) {
    evcount.getAndIncrement()
    def data_event = reader.getNextEvent()
    def event = EventConverter.convert(data_event)
    if (event.event_number==0 || filterEvents(event, processor, mode)) {
      writer.writeEvent(data_event)
    }
  }
  reader.close()
  writer.close()
}

exe.shutdown()
debug()