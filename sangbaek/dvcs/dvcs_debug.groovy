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

class dvcs{

  def processEvent(event){

    if (event.npart>0) {

      // get epg coincidence, no exclusive cut applied. electron cut from Brandon's package
      def dsets = DVCS.getEPG(event, electron_selector, proton_selector, gamma_selector)
      def (ele, pro, gam) = dsets*.particle.collect{it ? it.vector() : null} 
      // process only if there's a epg set in coincidence
      if(ele!=null) {
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
        def TrentoAng = KinTool.calcPhiTrento(beam, ele, pro)
        def TrentoAng2 = KinTool.calcPhiTrento2(beam, ele, gam)
        def t = KinTool.calcT(pro) //-t
        def nu = KinTool.calcNu(beam, ele)
        def t2 = KinTool.calcT2(beam, ele, gam)

        if (DVCS.KineCuts_xcG(xB, Q2, W, ele, gam) || (event.mc_status && gam.e()>0.4)){

          if (DVCS.ExclCuts_xcG(gam, ele, VMISS, VmissP, VmissG, Vhadr, Vhad2)){

            println("debug::run"+event.run_number+ "\t event "+event.event_number)

          } // exclusivity cuts ended
        }//kine cuts ended
      }// event with e, p, g
    }// event with particles
  }
}