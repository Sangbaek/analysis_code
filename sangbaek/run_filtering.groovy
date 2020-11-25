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

def processor = new filtering()

def evcount = new AtomicInteger()

def exe = Executors.newScheduledThreadPool(1)

GParsPool.withPool 12, {
  args.eachParallel{fname->
    def reader = new HipoDataSource()
    reader.open(fname)
    def writer = new HipoDataSync()
    writer.open("test.hipo")

    while(reader.hasEvent()) {
      evcount.getAndIncrement()
      def data_event = reader.getNextEvent()
      def event = EventConverter.convert(data_event)
      def count = event.event_number
      if (count==0 || processor.filterEvent(event)){
        writer.writeEvent(data_event)
      }
    }
    reader.close()
    writer.close()
  }
}

exe.shutdown()