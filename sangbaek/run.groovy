import org.jlab.jnp.hipo4.data.Event;
import org.jlab.jnp.hipo4.io.HipoReader
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
import sangbaek.dvcs.dvcs_corr
import sangbaek.dvcs.dvcs_EB
import sangbaek.dvcs.dvcs_EB_corr
import sangbaek.beamOffset.beamOffset
import sangbaek.pi0.pi0
import event.Event
import event.EventConverter
import my.Sugar

Sugar.enable()
/////////////////////////////////////////////////////////////////////

def outname = args[0].split('/')[-1]

// def processors = [new dvcs_EB()]
def processors = [new beamOffset()]

def evcount = new AtomicInteger()
def save = {
  processors.each{
    def out = new TDirectory()
    out.mkdir("/root")
    out.cd("/root")
    it.hists.each{out.writeDataSet(it.value)}
    def clasname = it.getClass().getSimpleName()
    out.writeFile("${clasname}.hipo")
  }
  println "event count: "+evcount.get()
  evcount.set(0)
}

def exe = Executors.newScheduledThreadPool(1)
exe.scheduleWithFixedDelay(save, 5, 30, TimeUnit.SECONDS)

GParsPool.withPool 12, {
  args.eachParallel{fname->
    def reader = new HipoReader()
    reader.open(fname)

    def jnp_event = new org.jlab.jnp.hipo4.data.Event()

    while(reader.hasNext()) {
      evcount.getAndIncrement()
      reader.nextEvent(jnp_event)
      def data_event = new HipoDataEvent(jnp_event, reader.getSchemaFactory())
      def event = EventConverter.convert(data_event)
      processors.each{it.processEvent(event)}
    }
    reader.close()
  }
}

processors.each{if(it.metaClass.respondsTo(it, 'finish')) it.finish()}

exe.shutdown()
save()