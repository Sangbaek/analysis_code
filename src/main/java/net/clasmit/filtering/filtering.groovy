package net.clasmit.filtering

import org.jlab.clas.physics.LorentzVector
import org.jlab.clas.physics.Vector3
import org.jlab.groot.data.H1F
import org.jlab.groot.data.H2F
import net.clasmit.utils.KinTool
import net.clasmit.event.Event
import net.clasmit.event.EventConverter
import net.clasmit.pid.electron.ElectronSelector
import net.clasmit.pid.proton.ProtonSelector
import net.clasmit.pid.gamma.GammaSelector
import java.util.concurrent.ConcurrentHashMap
import org.jlab.clas.pdg.PDGDatabase

class filtering{

  def polarity = "inbending"
  def electron_selector
  def proton_selector
  def gamma_selector = new GammaSelector()

  def filtering(){
    electron_selector = new ElectronSelector()
    proton_selector = new ProtonSelector()
  }

  def filtering(polar){
    polarity = polar
    electron_selector = new ElectronSelector(polarity)
    proton_selector = new ProtonSelector(polarity)
  }

  def filterDVCSEvents(event){

    if (event.npart>0) {
      def electron_candidate = electron_selector.applyCuts(event)
      def proton_candidate = proton_selector.applyCuts(event)
      def gamma_candidate = gamma_selector.applyCuts(event)
      if (electron_candidate.size()*proton_candidate.size()*gamma_candidate.size()) return true
      else return false
    }
    return false
  }

  def filterPi0Events(event){

    if (event.npart>0) {
      def electron_candidate = electron_selector.applyCuts(event)
      def proton_candidate = proton_selector.applyCuts(event)
      def gamma_candidate = gamma_selector.applyCuts(event)
      if (electron_candidate.size()*proton_candidate.size()*gamma_candidate.size() && gamma_candidate.size()>1) return true
      else return false
    }
    return false
  }

  def filterEPGs(event){
    if (event.npart>0) {
      def electron_candidates = electron_selector.applyCuts(event)
      def proton_candidates = proton_selector.applyCuts(event)
      def gamma_candidates = gamma_selector.applyCuts(event)
      if (electron_candidates&&proton_candidates&&gamma_candidates) return [*electron_candidates, *proton_candidates, *gamma_candidates]
      else return null
    }
    return null
  }

  def filterGammas(event){
    if (event.npart>0) {
      def gamma_candidates = gamma_selector.applyCuts(event)
      def candidates = []
      if (gamma_candidates.size()>1){
        (0..<gamma_candidates.size()-1).each{ind1 ->
          (ind1+1..<gamma_candidates.size()).each{ind2 ->
            def pind1 = gamma_candidates[ind1]
            def pind2 = gamma_candidates[ind2]
            def gam1 = LorentzVector.withPID(22, event.px[pind1], event.py[pind1], event.pz[pind1])
            def gam2 = LorentzVector.withPID(22, event.px[pind2], event.py[pind2], event.pz[pind2])
            def pi0_candidate = gam1 + gam2
            if (pi0_candidate.mass()>0.08 && pi0_candidate.mass()<0.2){
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