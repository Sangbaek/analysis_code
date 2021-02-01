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

  def ProtonSelector(){
    this.initalizeCustomProCuts()
  }

  def ProtonSelector(event){
    this.event = event
    this.initalizeCustomProCuts()
    this.getGoodProton(event)
    this.getGoodProtonCustom(event)
  }

  def applyCuts(event){
    this.getGoodProton(event)
    return this.protonCutResults
  }

  def initalizeCustomProCuts(){
    this.protonCutStrategies = [
      this.proton_candidate.passProtonEBPIDCut,
      this.proton_candidate.passProtonDCR1,
      this.proton_candidate.passProtonDCR2,
      this.proton_candidate.passProtonDCR3,
      this.proton_candidate.passProtonTrackQuality,
      this.proton_candidate.passProtonCDPolarAngleCut,
      this.proton_candidate.passProtonVertexCut
    ]

    def field_setting = "inbending"
    this.proton_candidate.setProtonCutParameters(field_setting)

  }

  def getGoodProton(event){
    //return a list of REC::Particle indices for tracks passing all proton cuts
    def pro_cut_result = (0..<event.npart).findAll{event.charge[it]>0}.collect{ ii -> [ii, this.protonCutStrategies.collect{ el_test -> el_test(event,ii) } ] }.collectEntries()
    this.protonCutResults = pro_cut_result.findResults{el_indx, cut_result -> !cut_result.contains(false) ? el_indx : null}
  }
}