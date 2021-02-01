package net.clasmit.pid.gamma

import org.jlab.io.base.DataBank;
import org.jlab.io.base.DataEvent;
import net.clasmit.pid.gamma.GammaFromEvent
import net.clasmit.event.Event
import org.jlab.clas.physics.Vector3

class GammaSelector{

  def event

  def gamma_candidate = new GammaFromEvent()
  def gammaCutStrategies
  def gammaCutResults

  def GammaSelector(){
    this.initalizeCustomGamCuts()
  }

  def GammaSelector(event){
    this.event = event
    this.initalizeCustomGamCuts()
    this.getGoodGamma(event)
    this.getGoodGammaCustom(event)
  }

  def applyCuts(event){
    this.getGoodGamma(event)
    return this.gammaCutResults
  }

  def initalizeCustomGamCuts(){
    this.gammaCutStrategies = [
      this.gamma_candidate.passGammaEBPIDCut,
      this.gamma_candidate.passGammaPCALFiducialCut,
      this.gamma_candidate.passGammaBetaCut
    ]
  }

  def getGoodGamma(event){
    //return a list of REC::Particle indices for tracks passing all gamma cuts
    def gam_cut_result = (0..<event.npart).findAll{event.charge[it]==0}.collect{ ii -> [ii, this.gammaCutStrategies.collect{ gam_test -> gam_test(event,ii) } ] }.collectEntries()
    this.gammaCutResults = gam_cut_result.findResults{gam_indx, cut_result -> !cut_result.contains(false) ? gam_indx : null}
  }
}