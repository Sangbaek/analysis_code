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

  def photon_kine_correction = {gam ->
    gam.setPxPyPzE(gam.px()+0.25*gam.px()/gam.e(), gam.py()+0.25*gam.py()/gam.e(), gam.pz()+0.25*gam.pz()/gam.e(), gam.e()+0.25)
  }

  def processEvent(event){

    if (event.npart>1) {
      (0..<event.npart-1).each{ind1 ->
        (ind1+1..<event.npart).each{ind2 ->
          def gam1 = LorentzVector.withPID(22, event.px[ind1], event.py[ind1], event.pz[ind1])
          def gam2 = LorentzVector.withPID(22, event.px[ind2], event.py[ind2], event.pz[ind2])
          def status1 = event.status[ind1].intdiv(1000)
          def status2 = event.status[ind2].intdiv(1000)
          def status = status1*status2
          def pi0 = gam1 + gam2
          def coneAngle = KinTool.Vangle(gam1.vect(), gam2.vect())
          def pi0_mass = pi0.mass()
          if (pi0_mass>0.08 && pi0_mass<0.2 && pi0.e()>3 && (gam1.e()>2 || gam2.e()>2)){
            hists.computeIfAbsent("pi0_mass_$status",h_inv_mass_gg).fill(pi0_mass)
          }

        }
      }
    }
  }
}