package net.clasmit.pid.electron

import org.jlab.io.base.DataBank;
import org.jlab.io.base.DataEvent;
import net.clasmit.pid.electron.ElectronFromEvent
import net.clasmit.event.Event
import org.jlab.clas.physics.Vector3

public class ElectronSelector{

  def event

  def electron_candidate = new ElectronFromEvent()
  def electronCutStrategies
  def electronCutResults

  public ElectronSelector(){
    this.initalizeCustomElecCuts()
  }

  def applyCuts(event){
    this.getGoodElectron(event)
    return this.electronCutResults
  }

  def initalizeCustomElecCuts(){
    this.electronCutStrategies = [
      this.electron_candidate.passElectronStatus,
      this.electron_candidate.passElectronChargeCut,
      this.electron_candidate.passElectronTrackQualityCut,
      this.electron_candidate.passElectronMinMomentum,
      this.electron_candidate.passElectronEBPIDCut,
      this.electron_candidate.passElectronSamplingFractionCut,
      this.electron_candidate.passElectronNpheCut,
      this.electron_candidate.passElectronVertexCut,
      this.electron_candidate.passElectronPCALFiducialCut,
      this.electron_candidate.passElectronPCALEdepCut,
      this.electron_candidate.passElectronDCR1,
      this.electron_candidate.passElectronDCR2,
      this.electron_candidate.passElectronDCR3,
      // this.electron_candidate.passElectronAntiPionCut
    ]

    def field_setting = "inbending"
    // cut lvl meanings: 0 loose, 1 med, 2 tight
    def el_cut_strictness_lvl=["ecal_cut_lvl":1,
               "nphe_cut_lvl":1,
               "vz_cut_lvl":1,
               "anti_pion_cut_lvl":1
    ]
    this.electron_candidate.setElectronCutStrictness(el_cut_strictness_lvl)
    this.electron_candidate.setElectronCutParameters(field_setting)

  }

  def getGoodElectron(event){
    //return a list of REC::Particle indices for tracks passing all electron cuts
    def el_cut_result = (0..<event.npart).findAll{event.charge[it]<0}.collect{ ii -> [ii, this.electronCutStrategies.collect{ el_test -> el_test(event,ii) } ] }.collectEntries()
    this.electronCutResults = el_cut_result.findResults{el_indx, cut_result -> !cut_result.contains(false) ? el_indx : null}
  }
}