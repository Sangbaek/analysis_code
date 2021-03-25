package sangbaek.beamOffset
import org.jlab.clas.physics.Vector3
import org.jlab.groot.data.H2F
import org.jlab.groot.data.H1F
import java.util.concurrent.ConcurrentHashMap
import org.jlab.clas.physics.Particle
// import pid.electron.ElectronFromEvent
// import pid.proton.ProtonFromEvent
// import pid.gamma.GammaFromEvent

class beamOffset {
	def hists = new ConcurrentHashMap()
    def vxvy = {new H2F("$it", "$it", 100, -0.1, 0.1, 100, -0.1, 0.1)}
    def vzphi_dc = {new H2F("$it", "$it", 100, -180, 180, 100, -20, 20)}
    def vzphi = {new H2F("$it", "$it", 100, -180, 180, 100, -20, 20)}

    def runNumber, runRange, vx, vy, vz, ele, hits, phi
	def processEvent(event) {


		(0..<event.npart).each{ index ->

            runNumber = event.run_number
            if (runNumber<5278) runRange = 1
            else if (runNumber>5419) runRange = 2
            else runRange = 3

            // electron
            if (event.pid[index]==11 && event.status[index] < 0){

                vx = event.vx[index]
                vy = event.vy[index]
                vz = event.vz[index]
                ele = new Particle(11, event.px[index], event.py[index], event.pz[index])
                if (event.dc1_status.contains(index)){
                    hits = event.dc1.get(index)
                    if (hits){
                        hits.each{
                            phi =  Math.toDegrees(Math.atan2(it.y, it.x))
                            hists.computeIfAbsent("/trig/vzphi_dc1_run"+runRange, vzphi_dc).fill(phi, vz)
                        }
                    }
                }   
                if (event.dc2_status.contains(index)){
                    hits = event.dc2.get(index)
                    if (hits){
                        hits.each{
                            phi =  Math.toDegrees(Math.atan2(it.y, it.x))
                            hists.computeIfAbsent("/trig/vzphi_dc2_run"+runRange, vzphi_dc).fill(phi, vz)
                        }
                    }
                }   
                if (event.dc3_status.contains(index)){
                    hits = event.dc3.get(index)
                    if (hits){
                        hits.each{
                            phi =  Math.toDegrees(Math.atan2(it.y, it.x))
                            hists.computeIfAbsent("/trig/vzphi_dc3_run"+runRange, vzphi_dc).fill(phi, vz)
                        }
                    }
                }   
                hists.computeIfAbsent("/trig/vzphi_run"+runRange, vzphi).fill(Math.toDegrees(ele.phi()), vz)
                hists.computeIfAbsent("/trig/vxvy_run"+runRange, vxvy).fill(vx, vy)
            }
        }
	}
}