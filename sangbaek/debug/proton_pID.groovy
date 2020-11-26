import org.jlab.io.hipo.HipoDataSource
import org.jlab.detector.base.DetectorType
import org.jlab.clas.physics.Particle
import org.jlab.clas.physics.Vector3
import org.jlab.groot.data.H2F
import org.jlab.groot.data.TDirectory
import event.Event
import event.EventConverter
import utils.KinTool
import pid.sangbaek.proton

def hist_pro_theta_mom = [:].withDefault{new H2F("hist_pro_theta_mom_$it", "momentum vs theta", 250,0,100, 250,0,11)}
 
def proton_ind = new proton()
   
def count = -1
def count2 = 0

for(fname in args) {
    def reader = new HipoDataSource()
    reader.open(fname)
    
    while(reader.hasEvent()) {
		def data_event = reader.getNextEvent()
		def event = EventConverter.convert(data_event)

		count += 1
		def good_pro_with_cuts_Stefan = proton_ind.applyCuts_Stefan(event)
		// def good_pro_with_cuts_Custom = proton_ind.applyCuts_Custom(event)

		if(good_pro_with_cuts_Stefan){
			// println(event.event_number)
			// println(event.event_number)
			// println(good_pro_with_cuts_Stefan)
		}
		good_pro_with_cuts_Stefan.each{proind->
	        def pro = new Particle(2212, *[event.px, event.py, event.pz].collect{it[proind]})
			def pro_p = pro.p()
			def pro_theta = Math.toDegrees(pro.theta())
			hist_pro_theta_mom['Stefan'+event.pcal_sector[proind]].fill(pro_theta,pro_p)
			count2 +=1
			// println(event.pcal_sector[proind])
		}

		// println(count)
		// println(count2)

		// if (count!=count2){
		// 	break
		// }
		// good_pro_with_cuts_Custom.each{ proind ->
	 //        def pro = new Particle(11, *[event.px, event.py, event.pz].collect{it[proind]})
		// 	def pro_p = pro.p()
		// 	def pro_theta = Math.toDegrees(pro.theta())
		// 	hist_pro_theta_mom['Custom'+event.pcal_sector[proind]].fill(pro_theta,pro_p)
		// }
    }
    reader.close()
}

def out = new TDirectory()
out.mkdir('/proton')
out.cd('/proton')
hist_pro_theta_mom.values().each{out.addDataSet(it)}
out.writeFile('proton_out.hipo')