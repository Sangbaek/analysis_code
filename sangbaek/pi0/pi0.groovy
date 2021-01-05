package sangbaek.pi0

import org.jlab.clas.physics.LorentzVector
import org.jlab.clas.physics.Vector3
import org.jlab.groot.data.H1F
import org.jlab.groot.data.H2F
import utils.KinTool
import event.Event
import event.EventConverter
import java.util.concurrent.ConcurrentHashMap
import org.jlab.clas.pdg.PDGDatabase

class pi0{

  //defining histograms
  def hists = new ConcurrentHashMap()
  def h_inv_mass_gg = {new H1F("$it", "$it", 100, 0.08, 0.2)}

  def beam = LorentzVector.withPID(11, 0, 0, 10.6)
  def target = LorentzVector.withPID(2212, 0, 0, 0)
  def M = PDGDatabase.getParticleMass(2212)
  def Mpi0 = PDGDatabase.getParticleMass(111)

  def processEvent(event){

    if (event.npart>1) {
      (0..<event.npart-1).each{ind1 ->
        (ind1+1..<event.npart).each{ind2 ->
          def gam1 = LorentzVector.withPID(22, event.px[ind1], event.py[ind1], event.pz[ind1])
          def gam2 = LorentzVector.withPID(22, event.px[ind2], event.py[ind2], event.pz[ind2])
          def status1 = event.status[ind1]
          def status2 = event.status[ind2]
          if (status1>=2000 && status2>=2000 && gam1.e() > 2 && gam2.e() > 2){
            def pi0_candidate = gam1 + gam2
            def pi0_mass = pi0_candidate.mass()
            if (pi0_mass>0.08 && pi0_mass<0.2 && pi0_candidate.e() > 2){
              hists.computeIfAbsent("pi0_mass",h_inv_mass_gg).fill(pi0_mass)
            }
          }
        }
      }
    }
  }
}