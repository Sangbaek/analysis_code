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

}