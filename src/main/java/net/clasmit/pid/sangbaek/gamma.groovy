package pid.sangbaek

import org.jlab.io.base.DataBank;
import org.jlab.io.base.DataEvent;
import pid.gamma.GammaFromEvent
import event.Event
import org.jlab.clas.physics.Vector3

class gamma{

  def event

  def gamma_candidate = new GammaFromEvent()
  def gammaCutStrategies_Stefan
  def gammaCutStrategies_Custom

  def gammaCutResults_Stefan
  def gammaCutResults_Custom

  def gamma(){
    this.initalizeCustomGamCuts()
  }

  def gamma(event){
    this.event = event
    this.initalizeCustomGamCuts()
    this.getGoodGamma(event)
    this.getGoodGammaCustom(event)
  }

  def applyCuts_Stefan(event){
    this.getGoodGamma(event)
    return this.gammaCutResults_Stefan
  }

  def applyCuts_Custom(event){
    this.getGoodGammaCustom(event)
    return this.gammaCutResults_Custom
  }


  def initalizeCustomGamCuts(){
    this.gammaCutStrategies_Stefan = [
      this.gamma_candidate.passGammaEBPIDCut,
      this.gamma_candidate.passGammaPCALFiducialCut,
      this.gamma_candidate.passGammaBetaCut
    ]

    this.gammaCutStrategies_Custom = [
      this.find_byMOM
    ]
  }


  def getGoodGamma(event){
    //return a list of REC::Particle indices for tracks passing all gamma cuts
    def gam_cut_result = (0..<event.npart).findAll{event.charge[it]==0}.collect{ ii -> [ii, this.gammaCutStrategies_Stefan.collect{ gam_test -> gam_test(event,ii) } ] }.collectEntries()
    this.gammaCutResults_Stefan = gam_cut_result.findResults{gam_indx, cut_result -> !cut_result.contains(false) ? gam_indx : null}
  }

  def getGoodGammaCustom(event){
    this.gammaCutResults_Custom = this.gammaCutResults_Stefan.findResults{ index ->
      this.gammaCutStrategies_Custom.collect{custom_test -> !custom_test(event,index)}.contains(false)? index : null
    }
  }

  // FTOF Hit Response
  def find_byFTOF = {event, index ->
    return event.tof_status.contains(index)
  }

  // momentum cut
  def find_byMOM = {event, index ->
    def lv = new Vector3(event.px[index], event.py[index], event.pz[index])
    def p = lv.mag()
    def vz = event.vz[index]
    def theta = Math.toDegrees(lv.theta())
    def phi = Math.toDegrees(lv.phi())
    return p > 0.4
  }
}