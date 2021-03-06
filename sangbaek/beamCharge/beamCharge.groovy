package sangbaek.beamCharge

import org.jlab.clas.physics.LorentzVector
import org.jlab.clas.physics.Vector3
import exclusive.sangbaek.DVCS
import utils.KinTool
import event.Event
import event.EventConverter
import pid.sangbaek.electron
import pid.sangbaek.proton
import pid.sangbaek.gamma
import java.util.concurrent.ConcurrentHashMap
import org.jlab.clas.pdg.PDGDatabase

class beamCharge{

  def minbeamCharge = [:].withDefault{10000}
  def maxbeamCharge = [:].withDefault{-10000}
  def dvcscounts = [:].withDefault{0}
  def list_of_runs = []

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

  def show_beamCharge(event){

    def intbeamCharge = 0
    println("list of runs in files read: " + list_of_runs)
    list_of_runs.each{ run_number ->
      println("run: " + run_number)
      println("maximum beam charge (nC): " + maxbeamCharge[run_number])
      println("minimum beam charge (nC): " + minbeamCharge[run_number])
      def beamChargediff = maxbeamCharge[run_number] - minbeamCharge[run_number]
      println("charge accumulated in this run (nC): " + beamChargediff)
      intbeamCharge = intbeamCharge + beamChargediff
      println("charge accumulated so far (nC): " + intbeamCharge)
    }
    println("integrated beam charge (nC): " + intbeamCharge)
    def rhotarget = 0.071 // in g/cm^3
    println("target density (g/cm^3): "+rhotarget)
    def na = 6.022E23 // Avogadro's
    def h2aw = 1.00784 // hydrogen atomic weight
    def ntarget = rhotarget * na / h2aw
    println("target number density (/cm^3): "+ntarget)
    def length = 5
    println("target length (cm): "+length)
    def thickness = ntarget * length
    println("target thickness (/cm^2): "+thickness)
    def eCharge = 1.6022E-10 // in nC
    //number of incoming beam particles
    def beamParticles = intbeamCharge/eCharge 
    println("number of electrons passed target: "+ beamParticles )
    def intLuminosity  = thickness * beamParticles
    println("integrated luminosity (/cm^2): " + intLuminosity)
  }

  def processEvent(event){

    if (event.npart>0) {

      def run_number = event.run_number
      if (!list_of_runs.contains(run_number)){
        list_of_runs = [*list_of_runs,run_number]
      }
      // get epg coincidence, no exclusive cut applied. electron cut from Brandon's package
      def dsets = DVCS.getEPG(event, electron_selector, proton_selector, gamma_selector)
      def (ele, pro, gam) = dsets*.particle.collect{it ? it.vector() : null} 
      // process only if there's a epg set in coincidence
      if(ele!=null) {

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

          if (DVCS.ExclCuts_xcG(gam, ele, VMISS, VmissP, VmissG, Vhadr, Vhad2)){

            dvcscounts[run_number]++

            def number_of_photons = gamma_selector.applyCuts_Stefan(event).size()
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

            //count max lumi and min lumi of inbending and outbending
            def beamCharge = event.beamCharge
            if (minbeamCharge[run_number]>beamCharge){
              minbeamCharge[run_number] = beamCharge
              println("debug: minimum updated in the run $run_number!")
              println(event.run_number + " run, " + event.event_number+"th events, min "+minbeamCharge[run_number] + ", current " + beamCharge + ", max "+maxbeamCharge[run_number] +" in nC.")
            }
            if (maxbeamCharge[run_number]<beamCharge){
              maxbeamCharge[run_number] = beamCharge
              println("debug: maximum updated in the run $run_number!")
              println(event.run_number + " run, " + event.event_number+"th events, min "+minbeamCharge[run_number] + ", current " + beamCharge + ", max "+maxbeamCharge[run_number] +" in nC.")
            }
            if (dvcscounts[run_number].intdiv(10000)){
              println("debug: having " + dvcscounts[run_number] + " dvcs events in the run " + run_number +"...")
              println(event.run_number + " run, " + event.event_number+"th events, min "+minbeamCharge[run_number] + ", current " + beamCharge + ", max "+maxbeamCharge[run_number] +" in nC.")
            }
          } // exclusivity cuts ended
        }//kine cuts ended
      }// event with e, p, g
    }// event with particles
  }
}