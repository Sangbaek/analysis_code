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



args.each{filename ->

    HipoReader reader = new HipoReader();
    reader.open(filename);

    def jnp_event = new org.jlab.jnp.hipo4.data.Event()
    SchemaFactory schema = reader.getSchemaFactory();

    // dataSelector.add("sqrt(px*px+py*py+pz*pz)>2.0");

    while(reader.hasNext()==true){

      reader.nextEvent(jnp_event);
      if(!jnp_event.hasBank(reader.getSchemaFactory().getSchema("MC::Particle"))) continue
      def data_event = new HipoDataEvent(jnp_event, reader.getSchemaFactory())
      def event = EventConverter.convert(data_event)
      if (event.mc_px[0] <-0.4696 && event.mc_px[0] > -0.4698){
        Bank  MCparticles = new Bank(schema.getSchema("MC::Particle"));
        Bank  RunConfigs = new Bank(schema.getSchema("RUN::config"));
        println(filename)
        MCParticles.show();
        RunConfigs.show();
      }
    }
}
