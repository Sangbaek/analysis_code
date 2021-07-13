package sangbaek.proton

import org.jlab.clas.physics.LorentzVector
import org.jlab.clas.physics.Vector3
import org.jlab.groot.data.H1F
import org.jlab.groot.data.H2F
import utils.KinTool
import event.Event
import event.EventConverter
import java.util.concurrent.ConcurrentHashMap
import org.jlab.clas.pdg.PDGDatabase

class proton{

  //defining histograms
  def hists = new ConcurrentHashMap()
  def h_dp_p = {new H2F("$it", "$it", 100, 0, 2, 100, -0.05, 0.05)}
  // def h_maxEminE = {new H2F("$it", "$it", 10, 0.5, 5.5, 10, 0.5, 5.5)}
  // def h_events = {new H1F("$it","$it",5, 0,5)}

  // def beam = LorentzVector.withPID(11, 0, 0, 10.6)
  // def target = LorentzVector.withPID(2212, 0, 0, 0)
  // def M = PDGDatabase.getParticleMass(2212)
  // def Mpi0 = PDGDatabase.getParticleMass(111)

  def pro_problem = {pro_p, pro_mc_p ->
     pro_mc_p - pro_p > -0.008+0.015/pro_p 
  }

  def hit_ftof1a, hit_ftof1b, hit_ftof2

  def processEvent(event){

    if (event.npart>1) {
      (0..<event.npart-1).each{ind1 ->
        if (event.pid[ind1]==2212){
          def pindex = event.before[ind1]
          def ftof_exists = event.tof_status.contains(pindex)
          def ctof_exists = event.ctof_status.contains(pindex)
          if (ftof_exists){
            hit_ftof1a = event.tof.get(index).find{ hit -> hit.layer == 1}
            hit_ftof1b = event.tof.get(index).find{ hit -> hit.layer == 2}
            hit_ftof2 = event.tof.get(index).find{ hit -> hit.layer == 3}

            if (hit_ftof2){
              if (pro_problem) hists.computeIfAbsent("/pro/dp_p_1", h_dp_p).fill(event.p[ind1],event.mc_p[ind1]-event.p[ind1])
              else hists.computeIfAbsent("/pro/dp_p_2", h_dp_p).fill(event.p[ind1],event.mc_p[ind1]-event.p[ind1])
            }
          }          
        }
      }
    }
  }
}