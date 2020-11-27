package sangbaek.dvcs

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
import run.Run
import java.util.concurrent.ConcurrentHashMap
import org.jlab.clas.pdg.PDGDatabase

class dvcs_counts{

  //defining histograms
  def hists = new ConcurrentHashMap()

  // count total events collected
  def h_events = {new H1F("$it","$it",12, 0,12)}

  def electron_selector = new electron()
  def proton_selector = new proton()
  def gamma_selector = new gamma()
  def beam = LorentzVector.withPID(11, 0, 0, 10.6)
  def target = LorentzVector.withPID(2212, 0, 0, 0)
  def M = PDGDatabase.getParticleMass(2212)
  def Mpi0 = PDGDatabase.getParticleMass(111)

  def photon_kine_correction = {gam ->
    gam.setPxPyPzE(gam.px()+0.25*gam.px()/gam.e(), gam.py()+0.25*gam.py()/gam.e(), gam.pz()+0.25*gam.pz()/gam.e(), gam.e()+0.25)
  }

  def processEvent(event){

    hists.computeIfAbsent("/events/events", h_events).fill(0.5)  

    if (event.npart>0) {

      hists.computeIfAbsent("/events/events", h_events).fill(1.5)  

      // get epg coincidence, no exclusive cut applied. electron cut from Brandon's package
      def dsets = DVCS.getEPG(event, electron_selector, proton_selector, gamma_selector)
      def (ele, pro, gam) = dsets*.particle.collect{it ? it.vector() : null} 
      // process only if there's a epg set in coincidence
      if(ele!=null) {
        // event number histograms
        hists.computeIfAbsent("/events/events", h_events).fill(2.5)  

        // gamma correction, energy by 250 MeV
        photon_kine_correction(gam)

        // get pindex, sector, status
        def (ele_ind, pro_ind, gam_ind) = dsets*.pindex
        def (ele_sec, pro_sec, gam_sec) = dsets*.sector
        def (ele_status, pro_status, gam_status) = dsets*.status
        
        // get 4 momentum variables!
        def VmissG = beam + target - ele - pro
        def VmissP = beam + target - ele - gam
        def VMISS = beam + target - ele - pro -gam
        def VGS = beam - ele 
        def W = (beam + target -ele).mass()
        def Vlept = (beam.vect()).cross(ele.vect());
        def Vhadr = (pro.vect()).cross(VGS.vect());
        def Vhad2 = (VGS.vect()).cross(gam.vect());

        // Now kinematics used to cross sections
        def xB = KinTool.calcXb(beam, ele)
        def Q2 = KinTool.calcQ2(beam, ele)

        if (DVCS.KineCuts_xcG(xB, Q2, W, ele, gam) || (event.mc_status && gam.e()>0.4)){

          hists.computeIfAbsent("/events/events", h_events).fill(3.5)  

          if (DVCS.ExclCuts_xcG(gam, ele, VMISS, VmissP, VmissG, Vhadr, Vhad2)){

            hists.computeIfAbsent("/events/events", h_events).fill(4.5)  

            def number_of_photons = gamma_selector.applyCuts_Stefan(event).size()
            hists.computeIfAbsent("/pi0/number_of_photons", h_events).fill(number_of_photons)
            if (number_of_photons>1){
              def gam2_ind = gamma_selector.applyCuts_Stefan(event).max{ind->
                if (ind!=gam_ind) new Vector3(*[event.px, event.py, event.pz].collect{it[ind]}).mag2()}
              def gam2 = LorentzVector.withPID(22, *[event.px, event.py, event.pz].collect{it[gam2_ind]})
              def pi0 = gam+gam2
              if (pi0.mass()<0.2 && pi0.mass()>0.08)  {
                return
              }
              else if (number_of_photons>2){
                def gam3_ind = gamma_selector.applyCuts_Stefan(event).max{ind->
                  if (ind!=gam_ind && ind!=gam2_ind) new Vector3(*[event.px, event.py, event.pz].collect{it[ind]}).mag2()}
                def gam3 = LorentzVector.withPID(22, *[event.px, event.py, event.pz].collect{it[gam3_ind]})
                pi0 = gam+gam3
                if (pi0.mass()<0.2 && pi0.mass()>0.08)  {
                  return
                }
              }
            }

            hists.computeIfAbsent("/events/events", h_events).fill(5.5)

            // check CD contents
            if (pro_status>=4000){
              hists.computeIfAbsent("/events/events", h_events).fill(6.5)  
            }
            else if (pro_status<4000 && pro_status>2000){
              hists.computeIfAbsent("/events/events", h_events).fill(7.5)
            }

          } // exclusivity cuts ended
        }//kine cuts ended
      }// event with e, p, g
    }// event with particles
  }
}