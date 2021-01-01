import org.jlab.jnp.hipo4.data.Event;
import org.jlab.jnp.hipo4.data.Bank
import org.jlab.jnp.hipo4.io.HipoReader
import org.jlab.io.hipo.HipoDataEvent
import org.jlab.io.hipo.HipoDataSource
import org.jlab.groot.data.TDirectory
import groovyx.gpars.GParsPool
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.Executors
import java.util.concurrent.ScheduledExecutorService
import java.util.concurrent.TimeUnit
import java.util.concurrent.atomic.AtomicInteger
import org.jlab.jnp.hipo4.data.SchemaFactory
import org.jlab.jnp.hipo4.data.Schema
import event.Event
import event.EventConverter
import my.Sugar

Sugar.enable()
/////////////////////////////////////////////////////////////////////
def evcount = new AtomicInteger()

def problematicRuns = [45040104, 45167466, 90664027, 45282893, 27046060, 27196869, 69221029, 41957238, 139439623, 132085813, 60462487, 107004602, 107025707, 71579058, 128424051, 85423888, 50002416, 93204648, 29114644, 144625985, 32764272, 81704849, 79539897, 46208798, 46297015, 46460162, 46555534, 86511011, 81850085, 81988334]

GParsPool.withPool 12, {
  args.eachParallel{fname->
    def reader = new HipoReader()
    reader.open(fname)
    SchemaFactory schema = reader.getSchemaFactory();
    Schema recParticle = schema.getSchema("REC::Particle")
    Schema runConfig = schema.getSchema("RUN::config")
    def particle = new Bank(recParticle)
    def config = new Bank(runConfig)
    def jnp_event = new org.jlab.jnp.hipo4.data.Event()

    while(reader.hasNext()) {
      evcount.getAndIncrement()
      reader.nextEvent(jnp_event)
      particle = jnp_event.read(particle)
      config = jnp_event.read(config)
      def eventNumber = config.getInt("event", 0)
      if (problematicRuns.contains(eventNumber)) particle.show()
    }
    reader.close()
  }
}