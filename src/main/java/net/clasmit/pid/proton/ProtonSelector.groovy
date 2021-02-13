package net.clasmit.pid.proton

import org.jlab.io.base.DataBank;
import org.jlab.io.base.DataEvent;
import net.clasmit.pid.proton.ProtonFromEvent
import net.clasmit.event.Event
import org.jlab.clas.physics.Vector3

class ProtonSelector{

  def event
  def proton_candidate = new ProtonFromEvent()
  def protonCutStrategies
  def protonCutResults
  def field_setting = "inbending"

  def ProtonSelector(){
    initalizeCustomProCuts()
  }

  def ProtonSelector(polarity){
    field_setting = polarity
    initalizeCustomProCuts()
  }


  def applyCuts(event){
    getGoodProton(event)
    return protonCutResults
  }

  def initalizeCustomProCuts(){
    protonCutStrategies = [
      // proton_candidate.passProtonEBPIDCut,
      proton_candidate.passProtonDCR1,
      proton_candidate.passProtonDCR2,
      proton_candidate.passProtonDCR3,
      // proton_candidate.passProtonTrackQuality,
      // proton_candidate.passProtonCDPolarAngleCut,
      // proton_candidate.passProtonVertexCut
    ]

    proton_candidate.setProtonCutParameters(field_setting)

  }

  def getGoodProton(event){
    //return a list of REC::Particle indices for tracks passing all proton cuts
    def pro_cut_result = (0..<event.npart).findAll{event.charge[it]>0 && event.pid[it]==2212}.collect{ ii -> [ii, protonCutStrategies.collect{ el_test -> el_test(event,ii) } ] }.collectEntries()
    protonCutResults = pro_cut_result.findResults{el_indx, cut_result -> !cut_result.contains(false) ? el_indx : null}
  }
}