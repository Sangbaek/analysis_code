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
  def field_setting = "inbending"

  public ElectronSelector(){
    initalizeCustomElecCuts()
  }

  public ElectronSelector(polarity){
    field_setting = "outbending"
    initalizeCustomElecCuts()
  }

  def applyCuts(event){
    getGoodElectron(event)
    return electronCutResults
  }

  def initalizeCustomElecCuts(){
    electronCutStrategies = [
      // electron_candidate.passElectronStatus,
      // electron_candidate.passElectronChargeCut,
      electron_candidate.passElectronTrackQualityCut,
      // electron_candidate.passElectronMinMomentum,
      // electron_candidate.passElectronEBPIDCut,
      electron_candidate.passElectronSamplingFractionCut,
      electron_candidate.passElectronNpheCut,
      electron_candidate.passElectronVertexCut,
      electron_candidate.passElectronPCALFiducialCut,
      electron_candidate.passElectronPCALEdepCut,
      electron_candidate.passElectronDCR1,
      electron_candidate.passElectronDCR2,
      electron_candidate.passElectronDCR3,
      // electron_candidate.passElectronAntiPionCut
    ]

    // cut lvl meanings: 0 loose, 1 med, 2 tight
    def el_cut_strictness_lvl=["ecal_cut_lvl":1,
               "nphe_cut_lvl":1,
               "vz_cut_lvl":1,
               "anti_pion_cut_lvl":1
    ]
    electron_candidate.setElectronCutStrictness(el_cut_strictness_lvl)
    electron_candidate.setElectronCutParameters(field_setting)

  }

  def getGoodElectron(event){
    //return a list of REC::Particle indices for tracks passing all electron cuts
    def el_cut_result = (0..<event.npart).findAll{event.charge[it]<0 && event.pid[it] == 11 && event.status[it] < 0}.collect{ ii -> [ii, electronCutStrategies.collect{ el_test -> el_test(event,ii) } ] }.collectEntries()
    electronCutResults = el_cut_result.findResults{el_indx, cut_result -> !cut_result.contains(false) ? el_indx : null}
  }
}