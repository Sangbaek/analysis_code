package sangbaek.filtering

import org.jlab.clas.physics.LorentzVector
import org.jlab.clas.physics.Vector3
import org.jlab.groot.data.H1F
import org.jlab.groot.data.H2F
import exclusive.sangbaek.DVCS
import utils.KinTool
import event.Event
import event.EventConverter
import pid.sangbaek.electron
import pid.sangbaek.proton
import pid.sangbaek.gamma
import java.util.concurrent.ConcurrentHashMap
import org.jlab.clas.pdg.PDGDatabase

class filtering{

  def electron_selector = new electron()
  def proton_selector = new proton()
  def gamma_selector = new gamma()

  def filterDVCSEvents(event){

    if (event.npart>0) {
      def electron_candidate = electron_selector.applyCuts_Brandon(event)
      def proton_candidate = proton_selector.applyCuts_Stefan(event)
      def gamma_candidate = gamma_selector.applyCuts_Stefan(event)
      if (electron_candidate.size()*proton_candidate.size()*gamma_candidate.size()) return true
      else return false
    }
    return false
  }

  def filterPi0Events(event){

    if (event.npart>0) {
      def electron_candidate = electron_selector.applyCuts_Brandon(event)
      def proton_candidate = proton_selector.applyCuts_Stefan(event)
      def gamma_candidate = gamma_selector.applyCuts_Stefan(event)
      if (electron_candidate.size()*proton_candidate.size()*gamma_candidate.size() && gamma_candidate.size()>1) return true
      else return false
    }
    return false
  }

  def filterEPGs(event){
    if (event.npart>0) {
      def electron_candidates = electron_selector.applyCuts_Brandon(event)
      def proton_candidates = proton_selector.applyCuts_Stefan(event)
      def gamma_candidates = gamma_selector.applyCuts_Stefan(event)
      if (electron_candidates&&proton_candidates&&gamma_candidates) return [*electron_candidates, *proton_candidates, *gamma_candidates]
      else return null
    }
    return null
  }

  def filterGammas(event){
    if (event.npart>0) {
      def gamma_candidates = gamma_selector.applyCuts_Stefan(event)
      def candidates = []
      if (gamma_candidates.size()>1){
        (0..<gamma_candidates.size()-1).each{ind1 ->
          (ind1+1..<gamma_candidates.size()).each{ind2 ->
            def pind1 = gamma_candidates[ind1]
            def pind2 = gamma_candidates[ind2]
            def gam1 = LorentzVector.withPID(22, event.px[pind1], event.py[pind1], event.pz[pind1])
            def gam2 = LorentzVector.withPID(22, event.px[pind2], event.py[pind2], event.pz[pind2])
            def pi0_candidates = gam1 + gam2
            if (pi0_candidates.mass()>0.08 && pi0_candidates.mass()<0.2){
              if(!candidates.contains(pind1)) candidates.add(pind1)
              if(!candidates.contains(pind2)) candidates.add(pind2)
            }
          }
        }
      }
      if (candidates)  return candidates
      else return null
    }
    return null
  }


}