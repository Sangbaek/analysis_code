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

  def determineSector = {hit->
    def phi = Math.toDegrees(Math.atan2(hit.get(1) /Math.sqrt(hit.get(0)*hit.get(0) + hit.get(1)*hit.get(1) + hit.get(2)*hit.get(2)),
                  hit.get(0) / Math.sqrt(hit.get(0)*hit.get(0) + hit.get(1)*hit.get(1) + hit.get(2)*hit.get(2))))

    if(phi < 30 && phi >= -30){        return 1;}
    else if(phi < 90 && phi >= 30){    return 2;}
    else if(phi < 150 && phi >= 90){   return 3;}
    else if(phi >= 150 || phi < -150){ return 4;}
    else if(phi < -90 && phi >= -150){ return 5;}
    else if(phi < -30 && phi >= -90){  return 6;}
    return 0
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
      if (electron_candidates&&proton_candidates&&gamma_candidates){

        def pinds = [*electron_candidates, *proton_candidates, *gamma_candidates]

        def pcal_sectors = pinds.collect{index->
          if (Math.abs(event.status[index])<2000 || Math.abs(event.status[index])>4000) event.status[index]
          else if(event.pcal_status.contains(index)) event.pcal_sector[index]
          else 0
        }

        def ecinner_sectors = pinds.collect{index->
          if (Math.abs(event.status[index])<2000 || Math.abs(event.status[index])>4000) event.status[index]
          else if(event.ecal_inner_status.contains(index)) event.ecal_inner_sector[index]
          else 0
        }

        def ecouter_sectors = pinds.collect{index->
          if (Math.abs(event.status[index])<2000 || Math.abs(event.status[index])>4000) event.status[index]
          else if(event.ecal_outer_status.contains(index)) event.ecal_outer_sector[index]
          else 0
        }

        def dc_track_sectors = pinds.collect{index->
          if (Math.abs(event.status[index])<2000 || Math.abs(event.status[index])>4000) event.status[index]
          else if(event.dc_sector.containsKey(index)) event.dc_sector[index]
          else 0
        }

        def dc1_traj_sectors = pinds.collect{index->
          if (Math.abs(event.status[index])<2000 || Math.abs(event.status[index])>4000) event.status[index]
          else if (event.dc1_status.contains(index)){
            def hit = event.dc1.get(index).find{ hit -> hit.layer == 6}
            determineSector([hit.x, hit.y, hit.z])
          }
          else 0
        }
        def dc2_traj_sectors = pinds.collect{index->
          if (Math.abs(event.status[index])<2000 || Math.abs(event.status[index])>4000) event.status[index]
          else if (event.dc2_status.contains(index)){
            def hit = event.dc2.get(index).find{ hit -> hit.layer == 18}
            determineSector([hit.x, hit.y, hit.z])
          }
          else 0
        }

        def dc3_traj_sectors = pinds.collect{index->
          if (Math.abs(event.status[index])<2000 || Math.abs(event.status[index])>4000) event.status[index]
          else if (event.dc3_status.contains(index)){
            def hit = event.dc3.get(index).find{ hit -> hit.layer == 36}
            determineSector([hit.x, hit.y, hit.z])
          }
          else 0
        }

        def ftof1a_sectors = pinds.collect{index->
          if (Math.abs(event.status[index])<2000 || Math.abs(event.status[index])>4000) event.status[index]
          else if (event.tof_status.contains(index)){
            def hit = event.tof.get(index).find{ hit -> hit.layer == 1}
            if (hit) hit.sector
            else 0
          }
          else 0
        }

        def ftof1b_sectors = pinds.collect{index->
          if (Math.abs(event.status[index])<2000 || Math.abs(event.status[index])>4000) event.status[index]
          else if (event.tof_status.contains(index)){
            def hit = event.tof.get(index).find{ hit -> hit.layer == 2}
            if (hit) hit.sector
            else 0
          }
          else 0
        }

        def ftof2_sectors = pinds.collect{index->
          if (Math.abs(event.status[index])<2000 || Math.abs(event.status[index])>4000) event.status[index]
          else if (event.tof_status.contains(index)){
            def hit = event.tof.get(index).find{ hit -> hit.layer == 3}
            if (hit) hit.sector
            else 0
          }
          else 0
        }

        def htcc_sectors = pinds.collect{index->
          if (Math.abs(event.status[index])<2000 || Math.abs(event.status[index])>4000) event.status[index]
          else if(event.cherenkov_status.contains(index)) event.cherenkov_sector[index]
          else 0
        }

        return [pinds:pinds, pcal_sectors:pcal_sectors, ecinner_sectors: ecinner_sectors,
        ecouter_sectors: ecouter_sectors, dc_track_sectors:dc_track_sectors,
        dc1_traj_sectors: dc1_traj_sectors, dc2_traj_sectors: dc2_traj_sectors, dc3_traj_sectors: dc3_traj_sectors,
        ftof1a_sectors: ftof1a_sectors, ftof1b_sectors: ftof1b_sectors, ftof2_sectors: ftof2_sectors, htcc_sectors: htcc_sectors]
      }
      else return  [pinds: null, pcal_sectors: null, ecinner_sectors: null,
      ecouter_sectors: null, dc_track_sectors: null,
      dc1_traj_sectors: null, dc2_traj_sectors: null, dc3_traj_sectors: null,
      ftof1a_sectors: null, ftof1b_sectors: null, ftof2_sectors:null, htcc_sectors: null]
    }
    return  [pinds: null, pcal_sectors: null, ecinner_sectors: null,
    ecouter_sectors: null, dc_track_sectors: null,
    dc1_traj_sectors: null, dc2_traj_sectors: null, dc3_traj_sectors: null,
    ftof1a_sectors: null, ftof1b_sectors: null, ftof2_sectors:null, htcc_sectors: null]
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