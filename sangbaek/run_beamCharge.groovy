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
import sangbaek.beamCharge.beamCharge
import event.Event
import event.EventConverter
import my.Sugar

Sugar.enable()
/////////////////////////////////////////////////////////////////////

def outname = args[0].split('/')[-1]

def processors = [new beamCharge()]

def evcount = new AtomicInteger()

def exe = Executors.newScheduledThreadPool(1)

GParsPool.withPool 12, {
  args.eachParallel{fname->
    def reader = new HipoDataSource()
    reader.open(fname)

    while(reader.hasEvent()) {
      evcount.getAndIncrement()
      def data_event = reader.getNextEvent()
      def event = EventConverter.convert(data_event)
      processors.each{it.processEvent(event)}
    }

    reader.close()
  }
}

processors.each{if(it.metaClass.respondsTo(it, 'show_beamCharge')) it.show_beamCharge()}

exe.shutdown()