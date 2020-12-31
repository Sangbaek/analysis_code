package sangbaek.dvcs

import org.jlab.clas.physics.LorentzVector
import org.jlab.clas.physics.Vector3
import org.jlab.groot.data.H1F
import org.jlab.groot.data.H2F
import exclusive.sangbaek.DVCS
import utils.KinTool
import event.Event
import event.EventConverter
import run.Run
import java.util.concurrent.ConcurrentHashMap
import org.jlab.clas.pdg.PDGDatabase

class dvcs_EB{

  //defining histograms
  def hists = new ConcurrentHashMap()

  // missing mass
  def h_mm2 = {new H1F("$it", "$it", 1500, -2, 4)}
  def h_mm2_2 = {new H1F("$it", "$it", 100, -0.2, 0.2)}
  def h_mm2_me = {new H2F("$it", "$it", 1000, -1, 3, 100, -0.1, 0.1)}

  // invaraiant mass
  def h_inv_mass_gg = {new H1F("$it", "$it", 1000, 0, 0.2)}
  def h_inv_mass_gg_gam_energy = {new H2F("$it","$it", 100,0,10, 1000,0,0.2)}
  def h_me_gam_energy = {new H2F("$it", "$it", 100, 0, 10, 100, -1, 3)}

  // angle between planes
  def h_angle = {new H1F("$it", "$it", 1900, -5 ,185)}

  // kinematic variables (correlation)
  def h_theta_mom = {new H2F("$it", "$it", 120, 0, 12, 100, 0, 100)}
  def h_phi_mom = {new H2F("$it", "$it", 120, 0, 12, 360, -180, 180)}
  def h_theta_phi = {new H2F("$it", "$it", 360, -180, 180, 100, 0, 100)}
  def h_theta_t = {new H2F("$it", "$it", 100, 0, 4, 100, 0, 100)}
  def h_phi_t = {new H2F("$it", "$it", 100, 0, 4, 360, -180, 180)}
  def h_theta_trento = {new H2F("$it", "$it", 360, 0, 360, 100, 0, 100)}
  def h_phi_trento = {new H2F("$it", "$it", 360, 0, 360, 360, -180, 180)}

  def h_t_trento =  {new H2F("$it", "$it", 360, 0, 360, 100, 0 , 4)}
  def h_t_trento_logarithmic =  {new H2F("$it", "$it", 360, 0, 360, 30, -4 , 0.6)}

  def h_t_t = {new H2F("$it", "$it", 100,0,4, 100,0,4)}
  def h_trento_trento = {new H2F("$it", "$it", 360, 0, 360, 360, 0, 360)}

  def h_Q2_xB_logarithmic = {new H2F("$it", "$it", 30, -1.31, -0.096, 30, 0, 1)}
  def h_Q2_xB = {new H2F("$it", "$it", 100, 0, 1,100, 0, 12)}
  def h_t_xB = {new H2F("$it", "$it", 100, 0, 1,100, 0, 4)}
  def h_Q2_t = {new H2F("$it", "$it", 100, 0, 4,100, 0, 12)}
  def h_Q2_theta = {new H2F("$it", "$it", 100, 0, 45, 100, 0, 12)}

  // polar angle
  def h_polar_rate = {new H1F("$it", "$it", 900, 0, 90)}
  // electron phi (sanity check)
  def h_azimuth_rate = {new H1F("$it","$it", 3600, 0, 360)}

  def h_cross_section = {new H1F("$it","$it", 30, 0, 360)}

  // count total events collected
  def h_events = {new H1F("$it","$it",12, 0,12)}
  def h_second_photons = {new H2F("$it","$it", 32,0,8, 6,0,6)}

  // sector dependence of kinematic variables 
  def h_W = {new H1F("$it","$it",100,0,10)}
  def h_t = {new H1F("$it","$it",100,-1,4)}
  def h_y = {new H1F("$it",100,0,1)}
  def h_Q2_W = {new H2F("$it","$it",100, 0, 10, 100, 0, 12)}

  // to check xB, Q2, -t, phi bin by bin
  def h_xB_bin = {new H1F("$it", "$it", 1200, 0, 1)}
  def h_t_bin = {new H1F("$it", "$it", 1200, 0, 4)}
  def h_Q2_bin = {new H1F("$it", "$it", 1200, 1, 12)}
  def h_phi_bin = {new H1F("$it", "$it", 1200, 0, 360)}

  // kinematic correction
  def h_gam_energy_corr = {new H2F("$it", "$it", 100, 0, 10, 100, 0, 10)}
  def h_gam_energy_corr_diff = {new H2F("$it", "$it", 100, 0, 10, 100, -1, 1)}

  //binning
  // def xB_array = [0, 0.1, 0.15, 0.2, 0.3, 0.4, 1]
  // def t_array = [0, 0.09, 0.13, 0.18, 0.23, 0.3, 0.39, 0.52, 0.72, 1.1, 2]
  // def Q2_array = [1, 1.7, 2.22, 2.7, 3.5, 11]

  // def xB_bin = {xB ->
  //   int xBbin = xB_array.findIndexOf{ xB < it} -1
  //   if (xBbin == -2) xBbin = xBbin + xB_array.size() +1 //length
  //   return xBbin
  // }

  // def Q2_bin = {Q2 ->
  //   int Q2bin = Q2_array.findIndexOf{ Q2 < it} -1
  //   if (Q2bin == -2) Q2bin = Q2bin + Q2_array.size() +1 //length
  //   return Q2bin
  // }

  // def t_bin = {t ->
  //   int tbin = t_array.findIndexOf{ t < it} -1
  //   if (tbin == -2) tbin = tbin + t_array.size() +1 //length
  //   return tbin
  // }

  def xB_array = [0, 0.16, 0.26]
  def Q2_arrays = [[1, 1.75], [1, 2.4], [1, 3.25]]
  def t_arrays = [[0, 0.15, 0.25, 0.45], [0, 0.22, 0.4, 0.80], [0, 0.40, 0.70, 1.15]]

  def binxBQ2t = {xB, Q2, t ->
    int xBbin = xB_array.findIndexOf{ xB < it} -1
    if (xBbin == -2) xBbin = xBbin + xB_array.size() +1 //length

    def Q2_array = Q2_arrays[xBbin]
    def t_array = t_arrays[xBbin]

    int Q2bin = Q2_array.findIndexOf{ Q2 < it} -1
    if (Q2bin == -2) Q2bin = Q2bin + Q2_array.size() +1 //length

    int tbin = t_array.findIndexOf{ t < it} -1
    if (tbin == -2) tbin = tbin + t_array.size() +1 //length

    int xBtbin = xB_array.size() * tbin + xBbin + 1
    int xBQ2tbin = xB_array.size() * t_array.size() * Q2bin + xBtbin

    return xBQ2tbin
  }

  // pid histograms
  def h_vz = {new H1F("$it", "$it", 800,-40,40)}     //vz
  def h_vz_mom = {new H2F("$it", "$it",110,0,11,800,-40,40)}     //vz vs p
  def h_vz_theta = {new H2F("$it", "$it",100,0,100,800,-40,40)} //vz vs p
  def h_pcalecal = {new H2F("$it","$it",100,0,0.5,100,0,0.5)}   //ecal/p vs pcal/p
  def h_Sampl_mom =  {new H2F("$it", "$it",110,0,11,100,0,1)}   //Sampling fraction vs p

  def h_theta_phi_ft = {new H2F("$it", "$it", 360, -180, 180, 100, 1, 6)}
  def h_theta_mom_ft = {new H2F("$it", "$it", 120, 0, 12, 100, 1, 6)}

  def phi_convention = {phi ->
    phi=phi + 180
    if (phi>180) phi = phi - 360
    if (phi<-180) phi = phi + 360
    return phi
  }

  def beam = LorentzVector.withPID(11, 0, 0, 10.6)
  def target = LorentzVector.withPID(2212, 0, 0, 0)
  def M = PDGDatabase.getParticleMass(2212)
  def Mpi0 = PDGDatabase.getParticleMass(111)

  def processEvent(event){

    hists.computeIfAbsent("/events/events", h_events).fill(0.5)  

    if (event.npart>0) {

      hists.computeIfAbsent("/events/events", h_events).fill(1.5)  

      (0..<event.npart).findAll{event.pid[it]==2212}.each{ind->
        def prot = new Vector3(*[event.px, event.py, event.pz].collect{it[ind]})
        def prot_phi = Math.toDegrees(prot.phi())
        if (prot_phi<0) prot_phi=360+prot_phi
        if (event.status[ind]>=4000){
          hists.computeIfAbsent("/all/pro/theta_CD", h_polar_rate).fill(Math.toDegrees(prot.theta()))
          hists.computeIfAbsent("/all/pro/phi_CD", h_azimuth_rate).fill(prot_phi)
        }
        else if (event.status[ind]<4000){
          hists.computeIfAbsent("/all/pro/theta_FD", h_polar_rate).fill(Math.toDegrees(prot.theta()))
          hists.computeIfAbsent("/all/pro/phi_FD", h_azimuth_rate).fill(prot_phi)
        }
      }      
      // get epg coincidence, no exclusive cut applied. electron cut from Brandon's package
      def dsets = DVCS.getEPG_EB(event)
      def (ele, pro, gam) = dsets*.particle.collect{it ? it.vector() : null} 
      // process only if there's a epg set in coincidence
      if(ele!=null) {
        // event number histograms
        hists.computeIfAbsent("/events/events", h_events).fill(2.5)  

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
        //calc tcol tmin
        def E = beam.e()
        def tmin = M*M*xB*xB/(1-xB+xB*M*M/Q2)
        def tcol = Q2*(Q2-2*xB*M*E)/xB/(Q2-2*M*E)
        // fill t dependence on 2 fold binning (xB, Q2)
        int xBbin = 1 + 2 * Math.floor(xB/0.2)
        int Q2bin = 1 + 2 * Math.floor(Q2/2)
        def helicity = -event.helicity

        def xBQ2tbin = binxBQ2t(xB, Q2, t2)
        int phibin = (int) TrentoAng2/12

        def eidep=0
        def eodep = 0
        def pcaldep = 0
        if( event.ecal_inner_status.contains(ele_ind) )  eidep = event.ecal_inner_energy[ele_ind]
        if( event.ecal_outer_status.contains(ele_ind) )  eodep = event.ecal_outer_energy[ele_ind]
        if( event.pcal_status.contains(ele_ind) )        pcaldep = event.pcal_energy[ele_ind]
        def edep = eidep + eodep + pcaldep

        // check deviation from elastic
        def ele_phi = Math.toDegrees(ele.phi())
        if (ele_phi<0) ele_phi=360+ele_phi
        def pro_phi = Math.toDegrees(pro.phi())
        if (pro_phi<0) pro_phi=360+pro_phi
        def gam_phi = Math.toDegrees(gam.phi())
        if (gam_phi<0) gam_phi=360+gam_phi

        //electron pid
        hists.computeIfAbsent("/epg/pid/ele/vz_mom_S"+ele_sec, h_vz_mom).fill(ele.p(), event.vz[ele_ind])
        hists.computeIfAbsent("/epg/pid/ele/vz_theta_S"+ele_sec, h_vz_theta).fill(Math.toDegrees(ele.theta()), event.vz[ele_ind])
        hists.computeIfAbsent("/epg/pid/ele/pcalecal_S"+ele_sec, h_pcalecal).fill(eidep/ele.p(), pcaldep/ele.p())
        hists.computeIfAbsent("/epg/pid/ele/pcalecaldep_S"+ele_sec, h_pcalecal).fill(pcaldep, eidep+eodep)
        hists.computeIfAbsent("/epg/pid/ele/Sampl_mom_S"+ele_sec, h_Sampl_mom).fill(ele.p(), edep/ele.p())
        hists.computeIfAbsent("/epg/pid/ele/theta_phi_S"+ele_sec, h_theta_phi).fill(Math.toDegrees(ele.phi()), Math.toDegrees(ele.theta()))
        hists.computeIfAbsent("/epg/pid/ele/theta_mom_S"+ele_sec, h_theta_mom).fill(ele.p(), Math.toDegrees(ele.theta()))
        hists.computeIfAbsent("/epg/pid/ele/theta_S"+ele_sec, h_polar_rate).fill(Math.toDegrees(ele.theta()))
        hists.computeIfAbsent("/epg/pid/ele/phi_S"+ele_sec, h_azimuth_rate).fill(ele_phi)
        hists.computeIfAbsent("/epg/pid/ele/vz_S"+ele_sec, h_vz).fill(event.vz[ele_ind])

        //proton pid
        def pro_string = ''
        if (pro_status>=4000) pro_string = 'cd'
        else if (pro_status>=2000) pro_string = 'fd_S'+pro_sec 

        hists.computeIfAbsent("/epg/pid/pro/vz_mom_"+pro_string, h_vz_mom).fill(pro.p(), event.vz[pro_ind])
        hists.computeIfAbsent("/epg/pid/pro/vzdiff_mom_"+pro_string, h_vz_mom).fill(pro.p(), event.vz[pro_ind]-event.vz[ele_ind])
        hists.computeIfAbsent("/epg/pid/pro/vz_theta_"+pro_string, h_vz_theta).fill(Math.toDegrees(pro.theta()), event.vz[pro_ind])
        hists.computeIfAbsent("/epg/pid/pro/theta_phi_"+pro_string, h_theta_phi).fill(Math.toDegrees(pro.phi()), Math.toDegrees(pro.theta()))
        hists.computeIfAbsent("/epg/pid/pro/theta_mom_"+pro_string, h_theta_mom).fill(pro.p(), Math.toDegrees(pro.theta()))
        hists.computeIfAbsent("/epg/pid/pro/theta_"+pro_string, h_polar_rate).fill(Math.toDegrees(pro.theta()))
        hists.computeIfAbsent("/epg/pid/pro/phi_"+pro_string, h_azimuth_rate).fill(pro_phi)
        hists.computeIfAbsent("/epg/pid/pro/vz_"+pro_string, h_vz).fill(event.vz[pro_ind])

        //gamma pid
        def gam_string = ''
        if (gam_status<4000 && gam_status>=2000) gam_string = 'fd_S'+gam_sec
        else if (gam_status>=1000 && gam_status<2000) gam_string = 'ft' 

        if (gam_string == 'ft'){
          hists.computeIfAbsent("/epg/pid/gam/theta_phi_"+gam_string, h_theta_phi_ft).fill(Math.toDegrees(gam.phi()), Math.toDegrees(gam.theta()))
          hists.computeIfAbsent("/epg/pid/gam/theta_mom_"+gam_string, h_theta_mom_ft).fill(gam.p(), Math.toDegrees(gam.theta()))
        }
        else{
          hists.computeIfAbsent("/epg/pid/gam/theta_phi_"+gam_string, h_theta_phi).fill(Math.toDegrees(gam.phi()), Math.toDegrees(gam.theta()))
          hists.computeIfAbsent("/epg/pid/gam/theta_mom_"+gam_string, h_theta_mom).fill(gam.p(), Math.toDegrees(gam.theta()))
        }
        hists.computeIfAbsent("/epg/pid/gam/theta_"+gam_string, h_polar_rate).fill(Math.toDegrees(gam.theta()))
        hists.computeIfAbsent("/epg/pid/gam/phi_"+gam_string, h_azimuth_rate).fill(gam_phi)

        hists.computeIfAbsent("/epg/pid/elast/ep_theta", h_trento_trento).fill(pro_phi, ele_phi)
        hists.computeIfAbsent("/epg/pid/elast/ep_phi_diff", h_azimuth_rate).fill(Math.abs(pro_phi-ele_phi))
        hists.computeIfAbsent("/epg/pid/elast/ep_polar", h_polar_rate).fill(Math.toDegrees(pro.theta()), Math.toDegrees(ele.theta()))

        // excl cuts
        hists.computeIfAbsent("/epg/cuts/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
        hists.computeIfAbsent("/epg/cuts/missing_energy", h_mm2).fill(VMISS.e())
        hists.computeIfAbsent("/epg/cuts/missing_mass_epg", h_mm2).fill(VMISS.mass2())
        hists.computeIfAbsent("/epg/cuts/missing_mass_eg", h_mm2).fill(VmissP.mass2())
        hists.computeIfAbsent("/epg/cuts/missing_mass_ep", h_mm2).fill(VmissG.mass2())
        hists.computeIfAbsent("/epg/cuts/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
        hists.computeIfAbsent("/epg/cuts/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
        hists.computeIfAbsent("/epg/cuts/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
        hists.computeIfAbsent("/epg/cuts/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
        hists.computeIfAbsent("/epg/cuts/me_gam_energy", h_me_gam_energy).fill(gam.e(), VMISS.e())

        hists.computeIfAbsent("/epg/kin_corr/gam_energy_corr_4vec", h_gam_energy_corr).fill(gam.e(), nu + t/2/M)
        hists.computeIfAbsent("/epg/kin_corr/gam_energy_corr_virtual", h_gam_energy_corr).fill(gam.e(), nu + t2/2/M)
        hists.computeIfAbsent("/epg/kin_corr/gam_energy_corr_diff_4vec", h_gam_energy_corr_diff).fill(gam.e(), nu + t/2/M - gam.e())
        hists.computeIfAbsent("/epg/kin_corr/gam_energy_corr_diff_virtual", h_gam_energy_corr_diff).fill(gam.e(), nu + t2/2/M - gam.e())

        // kinematic range
        hists.computeIfAbsent("/epg/binning/Q2_xB", h_Q2_xB).fill(xB,Q2)
        hists.computeIfAbsent("/epg/binning/t_trento", h_t_trento).fill(TrentoAng2, t2)
        hists.computeIfAbsent("/epg/binning/Q2_t", h_Q2_t).fill(t2,Q2)
        hists.computeIfAbsent("/epg/binning/Q2_xB_logarithmic", h_Q2_xB_logarithmic).fill(Math.log10(xB), Math.log10(Q2))
        hists.computeIfAbsent("/epg/binning/t_trento_logarithmic", h_t_trento_logarithmic).fill(TrentoAng2, Math.log10(t2))
        hists.computeIfAbsent("/epg/binning/t_xB", h_t_xB).fill(xB,t2)
        hists.computeIfAbsent("/epg/binning/Q2_theta", h_Q2_theta).fill(Math.toDegrees(ele.theta()),Q2);
        hists.computeIfAbsent("/epg/binning/Q2_xB_sec"+ele_sec, h_Q2_xB).fill(xB,Q2)
        hists.computeIfAbsent("/epg/binning/W_sec"+ele_sec, h_W).fill(W)
        hists.computeIfAbsent("/epg/binning/t_sec"+ele_sec, h_t).fill(t2)
        hists.computeIfAbsent("/epg/binning/phi_sec"+ele_sec, h_cross_section).fill(TrentoAng2) 
        hists.computeIfAbsent("/epg/binning/y_sec"+ele_sec, h_y).fill(KinTool.calcY(beam, ele))
        hists.computeIfAbsent("/epg/binning/Q2_W_sec"+ele_sec, h_Q2_W).fill(W, Q2)
        if (W>2)  hists.computeIfAbsent("/epg/binning/Q2_xB_W>2", h_Q2_xB).fill(xB,Q2)
        else hists.computeIfAbsent("/epg/binning/Q2_xB_W<2", h_Q2_xB).fill(xB,Q2)
        // Trento like angle from ep and eg plane
        hists.computeIfAbsent("/epg/binning/angle_ep_eg", h_angle).fill(KinTool.Vangle(ele.vect().cross(pro.vect()), ele.vect().cross(gam.vect())))

        def pro_phi_convention = phi_convention(Math.toDegrees(pro.phi()-ele.phi()))
        def gam_phi_convention = phi_convention(Math.toDegrees(gam.phi()-ele.phi()))

        hists.computeIfAbsent("/epg/corr/tmin", h_Q2_xB).fill(xB,Q2,tmin)
        hists.computeIfAbsent("/epg/corr/tcol", h_Q2_xB).fill(xB,Q2,tcol)

        hists.computeIfAbsent("/epg/corr/pro_theta_mom_xB_${xBbin}_Q2_${Q2bin}", h_theta_mom).fill(pro.p(), Math.toDegrees(pro.theta()))
        hists.computeIfAbsent("/epg/corr/pro_phi_mom_xB_${xBbin}_Q2_${Q2bin}", h_phi_mom).fill(pro.p(), pro_phi_convention)
        hists.computeIfAbsent("/epg/corr/pro_theta_phi_xB_${xBbin}_Q2_${Q2bin}", h_theta_phi).fill(pro_phi_convention, Math.toDegrees(pro.theta()))
        hists.computeIfAbsent("/epg/corr/gam_phi_mom_xB_${xBbin}_Q2_${Q2bin}", h_phi_mom).fill(gam.p(), gam_phi_convention)
        hists.computeIfAbsent("/epg/corr/gam_theta_mom_xB_${xBbin}_Q2_${Q2bin}", h_theta_mom).fill(gam.p(), Math.toDegrees(gam.theta()))
        hists.computeIfAbsent("/epg/corr/gam_theta_phi_xB_${xBbin}_Q2_${Q2bin}", h_theta_phi).fill(gam_phi_convention, Math.toDegrees(gam.theta()))

        hists.computeIfAbsent("/epg/corr/pro_theta_t_xB_${xBbin}_Q2_${Q2bin}", h_theta_t).fill(t2, Math.toDegrees(pro.theta()))
        hists.computeIfAbsent("/epg/corr/pro_phi_t_xB_${xBbin}_Q2_${Q2bin}", h_phi_t).fill(t2, pro_phi_convention)
        hists.computeIfAbsent("/epg/corr/pro_theta_trento_xB_${xBbin}_Q2_${Q2bin}", h_theta_trento).fill(TrentoAng2, Math.toDegrees(pro.theta()))
        hists.computeIfAbsent("/epg/corr/pro_phi_trento_xB_${xBbin}_Q2_${Q2bin}", h_phi_trento).fill(TrentoAng2, pro_phi_convention)
        hists.computeIfAbsent("/epg/corr/gam_theta_t_xB_${xBbin}_Q2_${Q2bin}", h_theta_t).fill(t2, Math.toDegrees(gam.theta()))
        hists.computeIfAbsent("/epg/corr/gam_phi_t_xB_${xBbin}_Q2_${Q2bin}", h_phi_t).fill(t2, gam_phi_convention)
        hists.computeIfAbsent("/epg/corr/gam_theta_trento_xB_${xBbin}_Q2_${Q2bin}", h_theta_trento).fill(TrentoAng2, Math.toDegrees(gam.theta()))
        hists.computeIfAbsent("/epg/corr/gam_phi_trento_xB_${xBbin}_Q2_${Q2bin}", h_phi_trento).fill(TrentoAng2, gam_phi_convention)

        hists.computeIfAbsent("/epg/corr/t_t", h_t_t).fill(t, t2)
        hists.computeIfAbsent("/epg/corr/trento_trento", h_trento_trento).fill(TrentoAng, TrentoAng2)

        // check hidden pi0
        def gam_hidden = VMISS
        gam_hidden.setE(gam_hidden.p())
        def pi0_hidden = gam_hidden + gam
        hists.computeIfAbsent("/epg/pi0/inv_mass_hidden", h_inv_mass_gg).fill(pi0_hidden.mass())

        hists.computeIfAbsent("/epg/yields/heli_$helicity/Q2_xB_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
        hists.computeIfAbsent("/epg/yields/heli_$helicity/t_xB_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
        hists.computeIfAbsent("/epg/yields/heli_$helicity/trento_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
        hists.computeIfAbsent("/epg/yields/heli_$helicity/xB_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_xB_bin).fill(xB)
        hists.computeIfAbsent("/epg/yields/heli_$helicity/Q2_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_Q2_bin).fill(Q2)
        hists.computeIfAbsent("/epg/yields/heli_$helicity/t_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_t_bin).fill(t2)
        hists.computeIfAbsent("/epg/yields/heli_$helicity/phi_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_phi_bin).fill(TrentoAng2)
        
        if (pro_status>=4000){
          hists.computeIfAbsent("/epg/yields/heli_$helicity/Q2_xB_pro_CD_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
          hists.computeIfAbsent("/epg/yields/heli_$helicity/t_xB_pro_CD_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
          hists.computeIfAbsent("/epg/yields/heli_$helicity/trento_pro_CD_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
        }

        if (gam_status<2000){
          hists.computeIfAbsent("/epg/yields/heli_$helicity/Q2_xB_gam_FT_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
          hists.computeIfAbsent("/epg/yields/heli_$helicity/t_xB_gam_FT_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
          hists.computeIfAbsent("/epg/yields/heli_$helicity/trento_gam_FT_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
        }

        if (pro_status>=4000 && gam_status<2000){
          hists.computeIfAbsent("/epg/yields/heli_$helicity/Q2_xB_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
          hists.computeIfAbsent("/epg/yields/heli_$helicity/t_xB_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
          hists.computeIfAbsent("/epg/yields/heli_$helicity/trento_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
        }

        if (DVCS.KineCuts_xcG(xB, Q2, W, ele, gam, pro) || (event.mc_status && gam.e()>0.4)){

          hists.computeIfAbsent("/events/events", h_events).fill(3.5)  

          //excl cuts
          hists.computeIfAbsent("/excl/cuts/kine_only/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
          hists.computeIfAbsent("/excl/cuts/kine_only/missing_energy", h_mm2).fill(VMISS.e())
          hists.computeIfAbsent("/excl/cuts/kine_only/missing_mass_epg", h_mm2).fill(VMISS.mass2())
          hists.computeIfAbsent("/excl/cuts/kine_only/missing_mass_eg", h_mm2).fill(VmissP.mass2())
          hists.computeIfAbsent("/excl/cuts/kine_only/missing_mass_ep", h_mm2).fill(VmissG.mass2())
          hists.computeIfAbsent("/excl/cuts/kine_only/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
          hists.computeIfAbsent("/excl/cuts/kine_only/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
          hists.computeIfAbsent("/excl/cuts/kine_only/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
          hists.computeIfAbsent("/excl/cuts/kine_only/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
          hists.computeIfAbsent("/excl/cuts/kine_only/me_gam_energy", h_me_gam_energy).fill(gam.e(), VMISS.e())

          if (KinTool.Vangle(gam.vect(),ele.vect())>10){
            hists.computeIfAbsent("/excl/cuts/cone_angle/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
            hists.computeIfAbsent("/excl/cuts/cone_angle/missing_energy", h_mm2).fill(VMISS.e())
            hists.computeIfAbsent("/excl/cuts/cone_angle/missing_mass_epg", h_mm2).fill(VMISS.mass2())
            hists.computeIfAbsent("/excl/cuts/cone_angle/missing_mass_eg", h_mm2).fill(VmissP.mass2())
            hists.computeIfAbsent("/excl/cuts/cone_angle/missing_mass_ep", h_mm2).fill(VmissG.mass2())
            hists.computeIfAbsent("/excl/cuts/cone_angle/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
            hists.computeIfAbsent("/excl/cuts/cone_angle/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
            hists.computeIfAbsent("/excl/cuts/cone_angle/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
            hists.computeIfAbsent("/excl/cuts/cone_angle/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
          }

          if (VMISS.e()<1.2 && VMISS.e()>-0.5){
            hists.computeIfAbsent("/excl/cuts/missing_energy/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
            hists.computeIfAbsent("/excl/cuts/missing_energy/missing_energy", h_mm2).fill(VMISS.e())
            hists.computeIfAbsent("/excl/cuts/missing_energy/missing_mass_epg", h_mm2).fill(VMISS.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_energy/missing_mass_eg", h_mm2).fill(VmissP.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_energy/missing_mass_ep", h_mm2).fill(VmissG.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_energy/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
            hists.computeIfAbsent("/excl/cuts/missing_energy/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
            hists.computeIfAbsent("/excl/cuts/missing_energy/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
            hists.computeIfAbsent("/excl/cuts/missing_energy/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
          }

          if (VMISS.mass2() <0.04 && VMISS.mass2() >-0.04){
            hists.computeIfAbsent("/excl/cuts/missing_mass_epg/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
            hists.computeIfAbsent("/excl/cuts/missing_mass_epg/missing_energy", h_mm2).fill(VMISS.e())
            hists.computeIfAbsent("/excl/cuts/missing_mass_epg/missing_mass_epg", h_mm2).fill(VMISS.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_mass_epg/missing_mass_eg", h_mm2).fill(VmissP.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_mass_epg/missing_mass_ep", h_mm2).fill(VmissG.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_mass_epg/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
            hists.computeIfAbsent("/excl/cuts/missing_mass_epg/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
            hists.computeIfAbsent("/excl/cuts/missing_mass_epg/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
            hists.computeIfAbsent("/excl/cuts/missing_mass_epg/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
          }

          if (VmissP.mass2() < 1.7 && VmissP.mass2() > 0.1){
            hists.computeIfAbsent("/excl/cuts/missing_mass_eg/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
            hists.computeIfAbsent("/excl/cuts/missing_mass_eg/missing_energy", h_mm2).fill(VMISS.e())
            hists.computeIfAbsent("/excl/cuts/missing_mass_eg/missing_mass_epg", h_mm2).fill(VMISS.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_mass_eg/missing_mass_eg", h_mm2).fill(VmissP.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_mass_eg/missing_mass_ep", h_mm2).fill(VmissG.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_mass_eg/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
            hists.computeIfAbsent("/excl/cuts/missing_mass_eg/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
            hists.computeIfAbsent("/excl/cuts/missing_mass_eg/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
            hists.computeIfAbsent("/excl/cuts/missing_mass_eg/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
          }

          if (VmissG.mass2() < 1 && VmissG.mass2() > -1){
            hists.computeIfAbsent("/excl/cuts/missing_mass_ep/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
            hists.computeIfAbsent("/excl/cuts/missing_mass_ep/missing_energy", h_mm2).fill(VMISS.e())
            hists.computeIfAbsent("/excl/cuts/missing_mass_ep/missing_mass_epg", h_mm2).fill(VMISS.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_mass_ep/missing_mass_eg", h_mm2).fill(VmissP.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_mass_ep/missing_mass_ep", h_mm2).fill(VmissG.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_mass_ep/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
            hists.computeIfAbsent("/excl/cuts/missing_mass_ep/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
            hists.computeIfAbsent("/excl/cuts/missing_mass_ep/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
            hists.computeIfAbsent("/excl/cuts/missing_mass_ep/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
          }

          if (Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()) < 0.12){
            hists.computeIfAbsent("/excl/cuts/missing_pt/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
            hists.computeIfAbsent("/excl/cuts/missing_pt/missing_energy", h_mm2).fill(VMISS.e())
            hists.computeIfAbsent("/excl/cuts/missing_pt/missing_mass_epg", h_mm2).fill(VMISS.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_pt/missing_mass_eg", h_mm2).fill(VmissP.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_pt/missing_mass_ep", h_mm2).fill(VmissG.mass2())
            hists.computeIfAbsent("/excl/cuts/missing_pt/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
            hists.computeIfAbsent("/excl/cuts/missing_pt/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
            hists.computeIfAbsent("/excl/cuts/missing_pt/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
            hists.computeIfAbsent("/excl/cuts/missing_pt/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
          }

          if (KinTool.Vangle(gam.vect(),VmissG.vect()) < 1.1){
            hists.computeIfAbsent("/excl/cuts/recon_gam_cone_angle/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
            hists.computeIfAbsent("/excl/cuts/recon_gam_cone_angle/missing_energy", h_mm2).fill(VMISS.e())
            hists.computeIfAbsent("/excl/cuts/recon_gam_cone_angle/missing_mass_epg", h_mm2).fill(VMISS.mass2())
            hists.computeIfAbsent("/excl/cuts/recon_gam_cone_angle/missing_mass_eg", h_mm2).fill(VmissP.mass2())
            hists.computeIfAbsent("/excl/cuts/recon_gam_cone_angle/missing_mass_ep", h_mm2).fill(VmissG.mass2())
            hists.computeIfAbsent("/excl/cuts/recon_gam_cone_angle/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
            hists.computeIfAbsent("/excl/cuts/recon_gam_cone_angle/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
            hists.computeIfAbsent("/excl/cuts/recon_gam_cone_angle/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
            hists.computeIfAbsent("/excl/cuts/recon_gam_cone_angle/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
          }

          if (KinTool.Vangle(Vhad2,Vhadr) < 4){
            hists.computeIfAbsent("/excl/cuts/coplanarity/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
            hists.computeIfAbsent("/excl/cuts/coplanarity/missing_energy", h_mm2).fill(VMISS.e())
            hists.computeIfAbsent("/excl/cuts/coplanarity/missing_mass_epg", h_mm2).fill(VMISS.mass2())
            hists.computeIfAbsent("/excl/cuts/coplanarity/missing_mass_eg", h_mm2).fill(VmissP.mass2())
            hists.computeIfAbsent("/excl/cuts/coplanarity/missing_mass_ep", h_mm2).fill(VmissG.mass2())
            hists.computeIfAbsent("/excl/cuts/coplanarity/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
            hists.computeIfAbsent("/excl/cuts/coplanarity/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
            hists.computeIfAbsent("/excl/cuts/coplanarity/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
            hists.computeIfAbsent("/excl/cuts/coplanarity/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
          }

          if (DVCS.ExclCuts_xcG(gam, ele, VMISS, VmissP, VmissG, Vhadr, Vhad2)){

            println("debug1::dvcs detected")
            println("debug2::run"+event.run_number+ "\t event "+event.event_number)
            hists.computeIfAbsent("/events/events", h_events).fill(4.5)  

            def number_of_photons = (0..<event.npart).findAll{event.pid[it]==22}.size()
            hists.computeIfAbsent("/pi0/number_of_photons", h_events).fill(number_of_photons)
            if (number_of_photons>1){
              def gam2_ind = (0..<event.npart).findAll{event.pid[it]==22}.max{ind->
                if (ind!=gam_ind) new Vector3(*[event.px, event.py, event.pz].collect{it[ind]}).mag2()}
              def gam2 = LorentzVector.withPID(22, *[event.px, event.py, event.pz].collect{it[gam2_ind]})
              def pi0 = gam+gam2
              hists.computeIfAbsent("/pi0/number_of_photons_gam1_energy", h_second_photons).fill(gam.e(), number_of_photons)
              hists.computeIfAbsent("/pi0/number_of_photons_gam2_energy", h_second_photons).fill(gam2.e(), number_of_photons)              
              hists.computeIfAbsent("/pi0/inv_mass_gg", h_inv_mass_gg).fill(pi0.mass())
              hists.computeIfAbsent("/pi0/inv_mass_gg_gam1_energy", h_inv_mass_gg_gam_energy).fill(gam.e(), pi0.mass())
              hists.computeIfAbsent("/pi0/inv_mass_gg_gam2_energy", h_inv_mass_gg_gam_energy).fill(gam2.e(), pi0.mass())
              hists.computeIfAbsent("/pi0/pi0_cone_angle",h_angle).fill(KinTool.Vangle(ele.vect(),pi0.vect()))
              hists.computeIfAbsent("/pi0/recon_pi0_cone_angle",h_angle).fill(KinTool.Vangle(VmissG.vect(),pi0.vect()))
              def costheta_pi0 = VGS.vect().dot(pi0.vect())/VGS.vect().mag()/pi0.vect().mag()
              def t_pi0 = (M*Q2+2*M*nu*nu-2*M*Math.sqrt(nu*nu+Q2)*Math.sqrt(pi0.e()*pi0.e()-Mpi0*Mpi0)*costheta_pi0)/(M+nu)
              def xBQ2tbin_pi0 = binxBQ2t(xB, Q2, t)//t_bin(t_pi0)
              if (pi0.mass()<0.2 && pi0.mass()>0.08)  {
                hists.computeIfAbsent("/pi0/kin_corr/t_pi0", h_t).fill(t_pi0)

                //electron pid
                hists.computeIfAbsent("/pi0/pid/ele/vz_mom_S"+ele_sec, h_vz_mom).fill(ele.p(), event.vz[ele_ind])
                hists.computeIfAbsent("/pi0/pid/ele/vz_theta_S"+ele_sec, h_vz_theta).fill(Math.toDegrees(ele.theta()), event.vz[ele_ind])
                hists.computeIfAbsent("/pi0/pid/ele/pcalecal_S"+ele_sec, h_pcalecal).fill(eidep/ele.p(), pcaldep/ele.p())
                hists.computeIfAbsent("/pi0/pid/ele/pcalecaldep_S"+ele_sec, h_pcalecal).fill(pcaldep, eidep+eodep)
                hists.computeIfAbsent("/pi0/pid/ele/Sampl_mom_S"+ele_sec, h_Sampl_mom).fill(ele.p(), edep/ele.p())
                hists.computeIfAbsent("/pi0/pid/ele/theta_phi_S"+ele_sec, h_theta_phi).fill(Math.toDegrees(ele.phi()), Math.toDegrees(ele.theta()))
                hists.computeIfAbsent("/pi0/pid/ele/theta_mom_S"+ele_sec, h_theta_mom).fill(ele.p(), Math.toDegrees(ele.theta()))
                hists.computeIfAbsent("/pi0/pid/ele/theta_S"+ele_sec, h_polar_rate).fill(Math.toDegrees(ele.theta()))
                hists.computeIfAbsent("/pi0/pid/ele/phi_S"+ele_sec, h_azimuth_rate).fill(ele_phi)
                hists.computeIfAbsent("/pi0/pid/ele/vz_S"+ele_sec, h_vz).fill(event.vz[ele_ind])

                //proton pid
                if (pro_status>=4000) pro_string = 'cd'
                else if (pro_status>=2000) pro_string = 'fd_S'+pro_sec 

                hists.computeIfAbsent("/pi0/pid/pro/vz_mom_"+pro_string, h_vz_mom).fill(pro.p(), event.vz[pro_ind])
                hists.computeIfAbsent("/pi0/pid/pro/vzdiff_mom_"+pro_string, h_vz_mom).fill(pro.p(), event.vz[pro_ind]-event.vz[ele_ind])
                hists.computeIfAbsent("/pi0/pid/pro/vz_theta_"+pro_string, h_vz_theta).fill(Math.toDegrees(pro.theta()), event.vz[pro_ind])
                hists.computeIfAbsent("/pi0/pid/pro/theta_phi_"+pro_string, h_theta_phi).fill(Math.toDegrees(pro.phi()), Math.toDegrees(pro.theta()))
                hists.computeIfAbsent("/pi0/pid/pro/theta_mom_"+pro_string, h_theta_mom).fill(pro.p(), Math.toDegrees(pro.theta()))
                hists.computeIfAbsent("/pi0/pid/pro/theta_"+pro_string, h_polar_rate).fill(Math.toDegrees(pro.theta()))
                hists.computeIfAbsent("/pi0/pid/pro/phi_"+pro_string, h_azimuth_rate).fill(pro_phi)
                hists.computeIfAbsent("/pi0/pid/pro/vz_"+pro_string, h_vz).fill(event.vz[pro_ind])

                //gamma pid
                if (gam_string == 'ft'){
                  hists.computeIfAbsent("/pi0/pid/gam/theta_phi_"+gam_string, h_theta_phi_ft).fill(Math.toDegrees(gam.phi()), Math.toDegrees(gam.theta()))
                  hists.computeIfAbsent("/pi0/pid/gam/theta_mom_"+gam_string, h_theta_mom_ft).fill(gam.p(), Math.toDegrees(gam.theta()))
                }
                else{
                  hists.computeIfAbsent("/pi0/pid/gam/theta_phi_"+gam_string, h_theta_phi).fill(Math.toDegrees(gam.phi()), Math.toDegrees(gam.theta()))
                  hists.computeIfAbsent("/pi0/pid/gam/theta_mom_"+gam_string, h_theta_mom).fill(gam.p(), Math.toDegrees(gam.theta()))
                }
                hists.computeIfAbsent("/pi0/pid/gam/theta_"+gam_string, h_polar_rate).fill(Math.toDegrees(gam.theta()))
                hists.computeIfAbsent("/pi0/pid/gam/phi_"+gam_string, h_azimuth_rate).fill(gam_phi)

                hists.computeIfAbsent("/pi0/pid/elast/ep_theta", h_trento_trento).fill(pro_phi, ele_phi)
                hists.computeIfAbsent("/pi0/pid/elast/ep_phi_diff", h_azimuth_rate).fill(Math.abs(pro_phi-ele_phi))
                hists.computeIfAbsent("/pi0/pid/elast/ep_polar", h_polar_rate).fill(Math.toDegrees(pro.theta()), Math.toDegrees(ele.theta()))

                // excl cuts
                hists.computeIfAbsent("/pi0/cuts/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
                hists.computeIfAbsent("/pi0/cuts/missing_energy", h_mm2).fill(VMISS.e())
                hists.computeIfAbsent("/pi0/cuts/missing_mass_epg", h_mm2).fill(VMISS.mass2())
                hists.computeIfAbsent("/pi0/cuts/missing_mass_eg", h_mm2).fill(VmissP.mass2())
                hists.computeIfAbsent("/pi0/cuts/missing_mass_ep", h_mm2).fill(VmissG.mass2())
                hists.computeIfAbsent("/pi0/cuts/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
                hists.computeIfAbsent("/pi0/cuts/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
                hists.computeIfAbsent("/pi0/cuts/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
                hists.computeIfAbsent("/pi0/cuts/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
                hists.computeIfAbsent("/pi0/cuts/me_gam_energy", h_me_gam_energy).fill(gam.e(), VMISS.e())

                hists.computeIfAbsent("/pi0/kin_corr/gam_energy_corr_4vec", h_gam_energy_corr).fill(gam.e(), nu + t/2/M)
                hists.computeIfAbsent("/pi0/kin_corr/gam_energy_corr_virtual", h_gam_energy_corr).fill(gam.e(), nu + t2/2/M)
                hists.computeIfAbsent("/pi0/kin_corr/gam_energy_corr_diff_4vec", h_gam_energy_corr_diff).fill(gam.e(), nu + t/2/M - gam.e())
                hists.computeIfAbsent("/pi0/kin_corr/gam_energy_corr_diff_virtual", h_gam_energy_corr_diff).fill(gam.e(), nu + t2/2/M - gam.e())

                // kinematic range
                hists.computeIfAbsent("/pi0/binning/Q2_xB", h_Q2_xB).fill(xB,Q2)
                hists.computeIfAbsent("/pi0/binning/t_trento", h_t_trento).fill(TrentoAng2, t2)
                hists.computeIfAbsent("/pi0/binning/Q2_t", h_Q2_t).fill(t2,Q2)
                hists.computeIfAbsent("/pi0/binning/Q2_xB_logarithmic", h_Q2_xB_logarithmic).fill(Math.log10(xB), Math.log10(Q2))
                hists.computeIfAbsent("/pi0/binning/t_trento_logarithmic", h_t_trento_logarithmic).fill(TrentoAng2, Math.log10(t2))
                hists.computeIfAbsent("/pi0/binning/t_xB", h_t_xB).fill(xB,t2)
                hists.computeIfAbsent("/pi0/binning/Q2_theta", h_Q2_theta).fill(Math.toDegrees(ele.theta()),Q2);
                hists.computeIfAbsent("/pi0/binning/Q2_xB_sec"+ele_sec, h_Q2_xB).fill(xB,Q2)
                hists.computeIfAbsent("/pi0/binning/W_sec"+ele_sec, h_W).fill(W)
                hists.computeIfAbsent("/pi0/binning/t_sec"+ele_sec, h_t).fill(t2)
                hists.computeIfAbsent("/pi0/binning/phi_sec"+ele_sec, h_cross_section).fill(TrentoAng2) 
                hists.computeIfAbsent("/pi0/binning/y_sec"+ele_sec, h_y).fill(KinTool.calcY(beam, ele))
                hists.computeIfAbsent("/pi0/binning/Q2_W_sec"+ele_sec, h_Q2_W).fill(W, Q2)
                // Trento like angle from ep and eg plane
                hists.computeIfAbsent("/pi0/binning/angle_ep_eg", h_angle).fill(KinTool.Vangle(ele.vect().cross(pro.vect()), ele.vect().cross(gam.vect())))

                hists.computeIfAbsent("/pi0/corr/tmin", h_Q2_xB).fill(xB,Q2,tmin)
                hists.computeIfAbsent("/pi0/corr/tcol", h_Q2_xB).fill(xB,Q2,tcol)

                hists.computeIfAbsent("/pi0/corr/pro_theta_mom_xB_${xBbin}_Q2_${Q2bin}", h_theta_mom).fill(pro.p(), Math.toDegrees(pro.theta()))
                hists.computeIfAbsent("/pi0/corr/pro_phi_mom_xB_${xBbin}_Q2_${Q2bin}", h_phi_mom).fill(pro.p(), pro_phi_convention)
                hists.computeIfAbsent("/pi0/corr/pro_theta_phi_xB_${xBbin}_Q2_${Q2bin}", h_theta_phi).fill(pro_phi_convention, Math.toDegrees(pro.theta()))
                hists.computeIfAbsent("/pi0/corr/gam_phi_mom_xB_${xBbin}_Q2_${Q2bin}", h_phi_mom).fill(gam.p(), gam_phi_convention)
                hists.computeIfAbsent("/pi0/corr/gam_theta_mom_xB_${xBbin}_Q2_${Q2bin}", h_theta_mom).fill(gam.p(), Math.toDegrees(gam.theta()))
                hists.computeIfAbsent("/pi0/corr/gam_theta_phi_xB_${xBbin}_Q2_${Q2bin}", h_theta_phi).fill(gam_phi_convention, Math.toDegrees(gam.theta()))

                hists.computeIfAbsent("/pi0/corr/pro_theta_t_xB_${xBbin}_Q2_${Q2bin}", h_theta_t).fill(t2, Math.toDegrees(pro.theta()))
                hists.computeIfAbsent("/pi0/corr/pro_phi_t_xB_${xBbin}_Q2_${Q2bin}", h_phi_t).fill(t2, pro_phi_convention)
                hists.computeIfAbsent("/pi0/corr/pro_theta_trento_xB_${xBbin}_Q2_${Q2bin}", h_theta_trento).fill(TrentoAng2, Math.toDegrees(pro.theta()))
                hists.computeIfAbsent("/pi0/corr/pro_phi_trento_xB_${xBbin}_Q2_${Q2bin}", h_phi_trento).fill(TrentoAng2, pro_phi_convention)
                hists.computeIfAbsent("/pi0/corr/gam_theta_t_xB_${xBbin}_Q2_${Q2bin}", h_theta_t).fill(t2, Math.toDegrees(gam.theta()))
                hists.computeIfAbsent("/pi0/corr/gam_phi_t_xB_${xBbin}_Q2_${Q2bin}", h_phi_t).fill(t2, gam_phi_convention)
                hists.computeIfAbsent("/pi0/corr/gam_theta_trento_xB_${xBbin}_Q2_${Q2bin}", h_theta_trento).fill(TrentoAng2, Math.toDegrees(gam.theta()))
                hists.computeIfAbsent("/pi0/corr/gam_phi_trento_xB_${xBbin}_Q2_${Q2bin}", h_phi_trento).fill(TrentoAng2, gam_phi_convention)

                hists.computeIfAbsent("/pi0/corr/t_t", h_t_t).fill(t, t2)
                hists.computeIfAbsent("/pi0/corr/trento_trento", h_trento_trento).fill(TrentoAng, TrentoAng2)

                // check hidden pi0
                hists.computeIfAbsent("/pi0/pi0/inv_mass_hidden", h_inv_mass_gg).fill(pi0_hidden.mass())

                hists.computeIfAbsent("/pi0/yields/heli_$helicity/Q2_xB_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
                hists.computeIfAbsent("/pi0/yields/heli_$helicity/t_xB_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
                hists.computeIfAbsent("/pi0/yields/heli_$helicity/trento_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
                hists.computeIfAbsent("/pi0/yields/heli_$helicity/xB_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_xB_bin).fill(xB)
                hists.computeIfAbsent("/pi0/yields/heli_$helicity/Q2_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_Q2_bin).fill(Q2)
                hists.computeIfAbsent("/pi0/yields/heli_$helicity/t_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_t_bin).fill(t2)
                hists.computeIfAbsent("/pi0/yields/heli_$helicity/phi_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_phi_bin).fill(TrentoAng2)
                
                if (pro_status>=4000){
                  hists.computeIfAbsent("/pi0/yields/heli_$helicity/Q2_xB_pro_CD_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
                  hists.computeIfAbsent("/pi0/yields/heli_$helicity/t_xB_pro_CD_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
                  hists.computeIfAbsent("/pi0/yields/heli_$helicity/trento_pro_CD_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
                }

                if (gam_status<2000){
                  hists.computeIfAbsent("/pi0/yields/heli_$helicity/Q2_xB_gam_FT_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
                  hists.computeIfAbsent("/pi0/yields/heli_$helicity/t_xB_gam_FT_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
                  hists.computeIfAbsent("/pi0/yields/heli_$helicity/trento_gam_FT_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
                }

                if (pro_status>=4000 && gam_status<2000){
                  hists.computeIfAbsent("/pi0/yields/heli_$helicity/Q2_xB_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
                  hists.computeIfAbsent("/pi0/yields/heli_$helicity/t_xB_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
                  hists.computeIfAbsent("/pi0/yields/heli_$helicity/trento_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
                }

                return
              }
              else if (number_of_photons>2){
                def gam3_ind = (0..<event.npart).findAll{event.pid[it]==22}.max{ind->
                  if (ind!=gam_ind && ind!=gam2_ind) new Vector3(*[event.px, event.py, event.pz].collect{it[ind]}).mag2()}
                def gam3 = LorentzVector.withPID(22, *[event.px, event.py, event.pz].collect{it[gam3_ind]})
                pi0 = gam+gam3
                hists.computeIfAbsent("/pi0/gam3/number_of_photons_gam1_energy", h_second_photons).fill(gam.e(), number_of_photons)
                hists.computeIfAbsent("/pi0/gam3/number_of_photons_gam2_energy", h_second_photons).fill(gam2.e(), number_of_photons)              
                hists.computeIfAbsent("/pi0/gam3/inv_mass_gg", h_inv_mass_gg).fill(pi0.mass())
                hists.computeIfAbsent("/pi0/gam3/inv_mass_gg_gam1_energy", h_inv_mass_gg_gam_energy).fill(gam.e(), pi0.mass())
                hists.computeIfAbsent("/pi0/gam3/inv_mass_gg_gam2_energy", h_inv_mass_gg_gam_energy).fill(gam2.e(), pi0.mass())
                hists.computeIfAbsent("/pi0/gam3/pi0_cone_angle",h_angle).fill(KinTool.Vangle(ele.vect(),pi0.vect()))
                hists.computeIfAbsent("/pi0/gam3/recon_pi0_cone_angle",h_angle).fill(KinTool.Vangle(VmissG.vect(),pi0.vect()))
                costheta_pi0 = VGS.vect().dot(pi0.vect())/VGS.vect().mag()/pi0.vect().mag()
                t_pi0 = (M*Q2+2*M*nu*nu-2*M*Math.sqrt(nu*nu+Q2)*Math.sqrt(pi0.e()*pi0.e()-Mpi0*Mpi0)*costheta_pi0)/(M+nu)
                //xBQ2tbin_pi0 = binxBQ2t(xB, Q2, t)//t_bin(t_pi0)
                if (pi0.mass()<0.2 && pi0.mass()>0.08)  {
                  hists.computeIfAbsent("/pi0/gam3/kin_corr/t_pi0", h_t).fill(t_pi0)

                  //electron pid
                  hists.computeIfAbsent("/pi0/gam3/pid/ele/vz_mom_S"+ele_sec, h_vz_mom).fill(ele.p(), event.vz[ele_ind])
                  hists.computeIfAbsent("/pi0/gam3/pid/ele/vz_theta_S"+ele_sec, h_vz_theta).fill(Math.toDegrees(ele.theta()), event.vz[ele_ind])
                  hists.computeIfAbsent("/pi0/gam3/pid/ele/pcalecal_S"+ele_sec, h_pcalecal).fill(eidep/ele.p(), pcaldep/ele.p())
                  hists.computeIfAbsent("/pi0/gam3/pid/ele/pcalecaldep_S"+ele_sec, h_pcalecal).fill(pcaldep, eidep+eodep)
                  hists.computeIfAbsent("/pi0/gam3/pid/ele/Sampl_mom_S"+ele_sec, h_Sampl_mom).fill(ele.p(), edep/ele.p())
                  hists.computeIfAbsent("/pi0/gam3/pid/ele/theta_phi_S"+ele_sec, h_theta_phi).fill(Math.toDegrees(ele.phi()), Math.toDegrees(ele.theta()))
                  hists.computeIfAbsent("/pi0/gam3/pid/ele/theta_mom_S"+ele_sec, h_theta_mom).fill(ele.p(), Math.toDegrees(ele.theta()))
                  hists.computeIfAbsent("/pi0/gam3/pid/ele/theta_S"+ele_sec, h_polar_rate).fill(Math.toDegrees(ele.theta()))
                  hists.computeIfAbsent("/pi0/gam3/pid/ele/phi_S"+ele_sec, h_azimuth_rate).fill(ele_phi)
                  hists.computeIfAbsent("/pi0/gam3/pid/ele/vz_S"+ele_sec, h_vz).fill(event.vz[ele_ind])

                  //proton pid
                  if (pro_status>=4000) pro_string = 'cd'
                  else if (pro_status>=2000) pro_string = 'fd_S'+pro_sec 

                  hists.computeIfAbsent("/pi0/gam3/pid/pro/vz_mom_"+pro_string, h_vz_mom).fill(pro.p(), event.vz[pro_ind])
                  hists.computeIfAbsent("/pi0/gam3/pid/pro/vzdiff_mom_"+pro_string, h_vz_mom).fill(pro.p(), event.vz[pro_ind]-event.vz[ele_ind])
                  hists.computeIfAbsent("/pi0/gam3/pid/pro/vz_theta_"+pro_string, h_vz_theta).fill(Math.toDegrees(pro.theta()), event.vz[pro_ind])
                  hists.computeIfAbsent("/pi0/gam3/pid/pro/theta_phi_"+pro_string, h_theta_phi).fill(Math.toDegrees(pro.phi()), Math.toDegrees(pro.theta()))
                  hists.computeIfAbsent("/pi0/gam3/pid/pro/theta_mom_"+pro_string, h_theta_mom).fill(pro.p(), Math.toDegrees(pro.theta()))
                  hists.computeIfAbsent("/pi0/gam3/pid/pro/theta_"+pro_string, h_polar_rate).fill(Math.toDegrees(pro.theta()))
                  hists.computeIfAbsent("/pi0/gam3/pid/pro/phi_"+pro_string, h_azimuth_rate).fill(pro_phi)
                  hists.computeIfAbsent("/pi0/gam3/pid/pro/vz_"+pro_string, h_vz).fill(event.vz[pro_ind])

                  //gamma pid
                  if (gam_string == 'ft'){
                    hists.computeIfAbsent("/pi0/gam3/pid/gam/theta_phi_"+gam_string, h_theta_phi_ft).fill(Math.toDegrees(gam.phi()), Math.toDegrees(gam.theta()))
                    hists.computeIfAbsent("/pi0/gam3/pid/gam/theta_mom_"+gam_string, h_theta_mom_ft).fill(gam.p(), Math.toDegrees(gam.theta()))
                  }
                  else{
                    hists.computeIfAbsent("/pi0/gam3/pid/gam/theta_phi_"+gam_string, h_theta_phi).fill(Math.toDegrees(gam.phi()), Math.toDegrees(gam.theta()))
                    hists.computeIfAbsent("/pi0/gam3/pid/gam/theta_mom_"+gam_string, h_theta_mom).fill(gam.p(), Math.toDegrees(gam.theta()))
                  }
                  hists.computeIfAbsent("/pi0/gam3/pid/gam/theta_"+gam_string, h_polar_rate).fill(Math.toDegrees(gam.theta()))
                  hists.computeIfAbsent("/pi0/gam3/pid/gam/phi_"+gam_string, h_azimuth_rate).fill(gam_phi)

                  hists.computeIfAbsent("/pi0/gam3/pid/elast/ep_theta", h_trento_trento).fill(pro_phi, ele_phi)
                  hists.computeIfAbsent("/pi0/gam3/pid/elast/ep_phi_diff", h_azimuth_rate).fill(Math.abs(pro_phi-ele_phi))
                  hists.computeIfAbsent("/pi0/gam3/pid/elast/ep_polar", h_polar_rate).fill(Math.toDegrees(pro.theta()), Math.toDegrees(ele.theta()))

                  // excl cuts
                  hists.computeIfAbsent("/pi0/gam3/cuts/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
                  hists.computeIfAbsent("/pi0/gam3/cuts/missing_energy", h_mm2).fill(VMISS.e())
                  hists.computeIfAbsent("/pi0/gam3/cuts/missing_mass_epg", h_mm2).fill(VMISS.mass2())
                  hists.computeIfAbsent("/pi0/gam3/cuts/missing_mass_eg", h_mm2).fill(VmissP.mass2())
                  hists.computeIfAbsent("/pi0/gam3/cuts/missing_mass_ep", h_mm2).fill(VmissG.mass2())
                  hists.computeIfAbsent("/pi0/gam3/cuts/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
                  hists.computeIfAbsent("/pi0/gam3/cuts/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
                  hists.computeIfAbsent("/pi0/gam3/cuts/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
                  hists.computeIfAbsent("/pi0/gam3/cuts/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
                  hists.computeIfAbsent("/pi0/gam3/cuts/me_gam_energy", h_me_gam_energy).fill(gam.e(), VMISS.e())

                  hists.computeIfAbsent("/pi0/gam3/kin_corr/gam_energy_corr_4vec", h_gam_energy_corr).fill(gam.e(), nu + t/2/M)
                  hists.computeIfAbsent("/pi0/gam3/kin_corr/gam_energy_corr_virtual", h_gam_energy_corr).fill(gam.e(), nu + t2/2/M)
                  hists.computeIfAbsent("/pi0/gam3/kin_corr/gam_energy_corr_diff_4vec", h_gam_energy_corr_diff).fill(gam.e(), nu + t/2/M - gam.e())
                  hists.computeIfAbsent("/pi0/gam3/kin_corr/gam_energy_corr_diff_virtual", h_gam_energy_corr_diff).fill(gam.e(), nu + t2/2/M - gam.e())

                  // kinematic range
                  hists.computeIfAbsent("/pi0/gam3/binning/Q2_xB", h_Q2_xB).fill(xB,Q2)
                  hists.computeIfAbsent("/pi0/gam3/binning/t_trento", h_t_trento).fill(TrentoAng2, t2)
                  hists.computeIfAbsent("/pi0/gam3/binning/Q2_t", h_Q2_t).fill(t2,Q2)
                  hists.computeIfAbsent("/pi0/gam3/binning/Q2_xB_logarithmic", h_Q2_xB_logarithmic).fill(Math.log10(xB), Math.log10(Q2))
                  hists.computeIfAbsent("/pi0/gam3/binning/t_trento_logarithmic", h_t_trento_logarithmic).fill(TrentoAng2, Math.log10(t2))
                  hists.computeIfAbsent("/pi0/gam3/binning/t_xB", h_t_xB).fill(xB,t2)
                  hists.computeIfAbsent("/pi0/gam3/binning/Q2_theta", h_Q2_theta).fill(Math.toDegrees(ele.theta()),Q2);
                  hists.computeIfAbsent("/pi0/gam3/binning/Q2_xB_sec"+ele_sec, h_Q2_xB).fill(xB,Q2)
                  hists.computeIfAbsent("/pi0/gam3/binning/W_sec"+ele_sec, h_W).fill(W)
                  hists.computeIfAbsent("/pi0/gam3/binning/t_sec"+ele_sec, h_t).fill(t2)
                  hists.computeIfAbsent("/pi0/gam3/binning/phi_sec"+ele_sec, h_cross_section).fill(TrentoAng2) 
                  hists.computeIfAbsent("/pi0/gam3/binning/y_sec"+ele_sec, h_y).fill(KinTool.calcY(beam, ele))
                  hists.computeIfAbsent("/pi0/gam3/binning/Q2_W_sec"+ele_sec, h_Q2_W).fill(W, Q2)
                  // Trento like angle from ep and eg plane
                  hists.computeIfAbsent("/pi0/gam3/binning/angle_ep_eg", h_angle).fill(KinTool.Vangle(ele.vect().cross(pro.vect()), ele.vect().cross(gam.vect())))

                  hists.computeIfAbsent("/pi0/gam3/corr/tmin", h_Q2_xB).fill(xB,Q2,tmin)
                  hists.computeIfAbsent("/pi0/gam3/corr/tcol", h_Q2_xB).fill(xB,Q2,tcol)

                  hists.computeIfAbsent("/pi0/gam3/corr/pro_theta_mom_xB_${xBbin}_Q2_${Q2bin}", h_theta_mom).fill(pro.p(), Math.toDegrees(pro.theta()))
                  hists.computeIfAbsent("/pi0/gam3/corr/pro_phi_mom_xB_${xBbin}_Q2_${Q2bin}", h_phi_mom).fill(pro.p(), pro_phi_convention)
                  hists.computeIfAbsent("/pi0/gam3/corr/pro_theta_phi_xB_${xBbin}_Q2_${Q2bin}", h_theta_phi).fill(pro_phi_convention, Math.toDegrees(pro.theta()))
                  hists.computeIfAbsent("/pi0/gam3/corr/gam_phi_mom_xB_${xBbin}_Q2_${Q2bin}", h_phi_mom).fill(gam.p(), gam_phi_convention)
                  hists.computeIfAbsent("/pi0/gam3/corr/gam_theta_mom_xB_${xBbin}_Q2_${Q2bin}", h_theta_mom).fill(gam.p(), Math.toDegrees(gam.theta()))
                  hists.computeIfAbsent("/pi0/gam3/corr/gam_theta_phi_xB_${xBbin}_Q2_${Q2bin}", h_theta_phi).fill(gam_phi_convention, Math.toDegrees(gam.theta()))

                  hists.computeIfAbsent("/pi0/gam3/corr/pro_theta_t_xB_${xBbin}_Q2_${Q2bin}", h_theta_t).fill(t2, Math.toDegrees(pro.theta()))
                  hists.computeIfAbsent("/pi0/gam3/corr/pro_phi_t_xB_${xBbin}_Q2_${Q2bin}", h_phi_t).fill(t2, pro_phi_convention)
                  hists.computeIfAbsent("/pi0/gam3/corr/pro_theta_trento_xB_${xBbin}_Q2_${Q2bin}", h_theta_trento).fill(TrentoAng2, Math.toDegrees(pro.theta()))
                  hists.computeIfAbsent("/pi0/gam3/corr/pro_phi_trento_xB_${xBbin}_Q2_${Q2bin}", h_phi_trento).fill(TrentoAng2, pro_phi_convention)
                  hists.computeIfAbsent("/pi0/gam3/corr/gam_theta_t_xB_${xBbin}_Q2_${Q2bin}", h_theta_t).fill(t2, Math.toDegrees(gam.theta()))
                  hists.computeIfAbsent("/pi0/gam3/corr/gam_phi_t_xB_${xBbin}_Q2_${Q2bin}", h_phi_t).fill(t2, gam_phi_convention)
                  hists.computeIfAbsent("/pi0/gam3/corr/gam_theta_trento_xB_${xBbin}_Q2_${Q2bin}", h_theta_trento).fill(TrentoAng2, Math.toDegrees(gam.theta()))
                  hists.computeIfAbsent("/pi0/gam3/corr/gam_phi_trento_xB_${xBbin}_Q2_${Q2bin}", h_phi_trento).fill(TrentoAng2, gam_phi_convention)

                  hists.computeIfAbsent("/pi0/gam3/corr/t_t", h_t_t).fill(t, t2)
                  hists.computeIfAbsent("/pi0/gam3/corr/trento_trento", h_trento_trento).fill(TrentoAng, TrentoAng2)

                  // check hidden pi0
                  hists.computeIfAbsent("/pi0/gam3/pi0/inv_mass_hidden", h_inv_mass_gg).fill(pi0_hidden.mass())

                  hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/Q2_xB_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
                  hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/t_xB_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
                  hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/trento_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
                  hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/xB_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_xB_bin).fill(xB)
                  hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/Q2_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_Q2_bin).fill(Q2)
                  hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/t_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_t_bin).fill(t2)
                  hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/phi_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_phi_bin).fill(TrentoAng2)
                  
                  if (pro_status>=4000){
                    hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/Q2_xB_pro_CD_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
                    hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/t_xB_pro_CD_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
                    hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/trento_pro_CD_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
                  }

                  if (gam_status<2000){
                    hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/Q2_xB_gam_FT_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
                    hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/t_xB_gam_FT_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
                    hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/trento_gam_FT_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
                  }

                  if (pro_status>=4000 && gam_status<2000){
                    hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/Q2_xB_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
                    hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/t_xB_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
                    hists.computeIfAbsent("/pi0/gam3/yields/heli_$helicity/trento_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
                  }
                
                  return
                }
              }
            }

            hists.computeIfAbsent("/events/events", h_events).fill(5.5)

            //electron pid
            hists.computeIfAbsent("/excl/pid/ele/vz_mom_S"+ele_sec, h_vz_mom).fill(ele.p(), event.vz[ele_ind])
            hists.computeIfAbsent("/excl/pid/ele/vz_theta_S"+ele_sec, h_vz_theta).fill(Math.toDegrees(ele.theta()), event.vz[ele_ind])
            hists.computeIfAbsent("/excl/pid/ele/pcalecal_S"+ele_sec, h_pcalecal).fill(eidep/ele.p(), pcaldep/ele.p())
            hists.computeIfAbsent("/excl/pid/ele/pcalecaldep_S"+ele_sec, h_pcalecal).fill(pcaldep, eidep+eodep)
            hists.computeIfAbsent("/excl/pid/ele/Sampl_mom_S"+ele_sec, h_Sampl_mom).fill(ele.p(), edep/ele.p())
            hists.computeIfAbsent("/excl/pid/ele/theta_phi_S"+ele_sec, h_theta_phi).fill(Math.toDegrees(ele.phi()), Math.toDegrees(ele.theta()))
            hists.computeIfAbsent("/excl/pid/ele/theta_mom_S"+ele_sec, h_theta_mom).fill(ele.p(), Math.toDegrees(ele.theta()))
            hists.computeIfAbsent("/excl/pid/ele/theta_S"+ele_sec, h_polar_rate).fill(Math.toDegrees(ele.theta()))
            hists.computeIfAbsent("/excl/pid/ele/phi_S"+ele_sec, h_azimuth_rate).fill(ele_phi)
            hists.computeIfAbsent("/excl/pid/ele/vz_S"+ele_sec, h_vz).fill(event.vz[ele_ind])

            //proton pid
            hists.computeIfAbsent("/excl/pid/pro/vz_mom_"+pro_string, h_vz_mom).fill(pro.p(), event.vz[pro_ind])
            hists.computeIfAbsent("/excl/pid/pro/vzdiff_mom_"+pro_string, h_vz_mom).fill(pro.p(), event.vz[pro_ind]-event.vz[ele_ind])
            hists.computeIfAbsent("/excl/pid/pro/vz_theta_"+pro_string, h_vz_theta).fill(Math.toDegrees(pro.theta()), event.vz[pro_ind])
            hists.computeIfAbsent("/excl/pid/pro/theta_phi_"+pro_string, h_theta_phi).fill(Math.toDegrees(pro.phi()), Math.toDegrees(pro.theta()))
            hists.computeIfAbsent("/excl/pid/pro/theta_mom_"+pro_string, h_theta_mom).fill(pro.p(), Math.toDegrees(pro.theta()))
            hists.computeIfAbsent("/excl/pid/pro/theta_"+pro_string, h_polar_rate).fill(Math.toDegrees(pro.theta()))
            hists.computeIfAbsent("/excl/pid/pro/phi_"+pro_string, h_azimuth_rate).fill(pro_phi)
            hists.computeIfAbsent("/excl/pid/pro/vz_"+pro_string, h_vz).fill(event.vz[pro_ind])

            //gamma pid
            if (gam_string == 'ft'){
              hists.computeIfAbsent("/excl/pid/gam/theta_phi_"+gam_string, h_theta_phi_ft).fill(Math.toDegrees(gam.phi()), Math.toDegrees(gam.theta()))
              hists.computeIfAbsent("/excl/pid/gam/theta_mom_"+gam_string, h_theta_mom_ft).fill(gam.p(), Math.toDegrees(gam.theta()))
            }
            else{
              hists.computeIfAbsent("/excl/pid/gam/theta_phi_"+gam_string, h_theta_phi).fill(Math.toDegrees(gam.phi()), Math.toDegrees(gam.theta()))
              hists.computeIfAbsent("/excl/pid/gam/theta_mom_"+gam_string, h_theta_mom).fill(gam.p(), Math.toDegrees(gam.theta()))
            }
            hists.computeIfAbsent("/excl/pid/gam/theta_"+gam_string, h_polar_rate).fill(Math.toDegrees(gam.theta()))
            hists.computeIfAbsent("/excl/pid/gam/phi_"+gam_string, h_azimuth_rate).fill(gam_phi)

            hists.computeIfAbsent("/excl/pid/elast/ep_theta", h_trento_trento).fill(pro_phi, ele_phi)
            hists.computeIfAbsent("/excl/pid/elast/ep_phi_diff", h_azimuth_rate).fill(Math.abs(pro_phi-ele_phi))
            hists.computeIfAbsent("/excl/pid/elast/ep_polar", h_polar_rate).fill(Math.toDegrees(pro.theta()), Math.toDegrees(ele.theta()))

            //excl cuts
            hists.computeIfAbsent("/dvcs/cuts/cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),ele.vect()))
            hists.computeIfAbsent("/dvcs/cuts/missing_energy", h_mm2).fill(VMISS.e())
            hists.computeIfAbsent("/dvcs/cuts/missing_mass_epg", h_mm2).fill(VMISS.mass2())
            hists.computeIfAbsent("/dvcs/cuts/missing_mass_eg", h_mm2).fill(VmissP.mass2())
            hists.computeIfAbsent("/dvcs/cuts/missing_mass_ep", h_mm2).fill(VmissG.mass2())
            hists.computeIfAbsent("/dvcs/cuts/missing_pt", h_mm2).fill(Math.sqrt(VMISS.px()*VMISS.px()+VMISS.py()*VMISS.py()))
            hists.computeIfAbsent("/dvcs/cuts/recon_gam_cone_angle", h_angle).fill(KinTool.Vangle(gam.vect(),VmissG.vect()))
            hists.computeIfAbsent("/dvcs/cuts/coplanarity", h_angle).fill(KinTool.Vangle(Vhad2,Vhadr))
            hists.computeIfAbsent("/dvcs/cuts/mm2epg_me", h_mm2_me).fill(VMISS.e(), VMISS.mass2())
            hists.computeIfAbsent("/dvcs/cuts/me_gam_energy", h_me_gam_energy).fill(gam.e(), VMISS.e())

            hists.computeIfAbsent("/dvcs/kin_corr/gam_energy_corr_4vec", h_gam_energy_corr).fill(gam.e(), nu + t/2/M)
            hists.computeIfAbsent("/dvcs/kin_corr/gam_energy_corr_virtual", h_gam_energy_corr).fill(gam.e(), nu + t2/2/M)
            hists.computeIfAbsent("/dvcs/kin_corr/gam_energy_corr_diff_4vec", h_gam_energy_corr_diff).fill(gam.e(), nu + t/2/M - gam.e())
            hists.computeIfAbsent("/dvcs/kin_corr/gam_energy_corr_diff_virtual", h_gam_energy_corr_diff).fill(gam.e(), nu + t2/2/M - gam.e())

            hists.computeIfAbsent("/dvcs/binning/Q2_xB", h_Q2_xB).fill(xB,Q2)
            hists.computeIfAbsent("/dvcs/binning/t_trento", h_t_trento).fill(TrentoAng2, t2)
            hists.computeIfAbsent("/dvcs/binning/Q2_t", h_Q2_t).fill(t2,Q2)
            hists.computeIfAbsent("/dvcs/binning/Q2_xB_logarithmic", h_Q2_xB_logarithmic).fill(Math.log10(xB), Math.log10(Q2))
            hists.computeIfAbsent("/dvcs/binning/t_trento_logarithmic", h_t_trento_logarithmic).fill(TrentoAng2, Math.log10(t2))
            hists.computeIfAbsent("/dvcs/binning/t_xB", h_t_xB).fill(xB,t2)
            hists.computeIfAbsent("/dvcs/binning/Q2_theta", h_Q2_theta).fill(Math.toDegrees(ele.theta()),Q2);
            hists.computeIfAbsent("/dvcs/binning/Q2_xB_sec"+ele_sec, h_Q2_xB).fill(xB,Q2)
            hists.computeIfAbsent("/dvcs/binning/W_sec"+ele_sec, h_W).fill(W)
            hists.computeIfAbsent("/dvcs/binning/t_sec"+ele_sec, h_t).fill(t2)
            hists.computeIfAbsent("/dvcs/binning/phi_sec"+ele_sec, h_cross_section).fill(TrentoAng2) 
            hists.computeIfAbsent("/dvcs/binning/y_sec"+ele_sec, h_y).fill(KinTool.calcY(beam, ele))
            hists.computeIfAbsent("/dvcs/binning/Q2_W_sec"+ele_sec, h_Q2_W).fill(W, Q2)
            // Trento like angle from ep and eg plane
            hists.computeIfAbsent("/dvcs/binning/angle_ep_eg", h_angle).fill(KinTool.Vangle(ele.vect().cross(pro.vect()), ele.vect().cross(gam.vect())))

            hists.computeIfAbsent("/dvcs/corr/tmin", h_Q2_xB).fill(xB,Q2,tmin)
            hists.computeIfAbsent("/dvcs/corr/tcol", h_Q2_xB).fill(xB,Q2,tcol)

            hists.computeIfAbsent("/dvcs/corr/pro_theta_mom_xB_${xBbin}_Q2_${Q2bin}", h_theta_mom).fill(pro.p(), Math.toDegrees(pro.theta()))
            hists.computeIfAbsent("/dvcs/corr/pro_phi_mom_xB_${xBbin}_Q2_${Q2bin}", h_phi_mom).fill(pro.p(), pro_phi_convention)
            hists.computeIfAbsent("/dvcs/corr/pro_theta_phi_xB_${xBbin}_Q2_${Q2bin}", h_theta_phi).fill(pro_phi_convention, Math.toDegrees(pro.theta()))
            hists.computeIfAbsent("/dvcs/corr/gam_phi_mom_xB_${xBbin}_Q2_${Q2bin}", h_phi_mom).fill(gam.p(), gam_phi_convention)
            hists.computeIfAbsent("/dvcs/corr/gam_theta_mom_xB_${xBbin}_Q2_${Q2bin}", h_theta_mom).fill(gam.p(), Math.toDegrees(gam.theta()))
            hists.computeIfAbsent("/dvcs/corr/gam_theta_phi_xB_${xBbin}_Q2_${Q2bin}", h_theta_phi).fill(gam_phi_convention, Math.toDegrees(gam.theta()))

            hists.computeIfAbsent("/dvcs/corr/pro_theta_t_xB_${xBbin}_Q2_${Q2bin}", h_theta_t).fill(t2, Math.toDegrees(pro.theta()))
            hists.computeIfAbsent("/dvcs/corr/pro_phi_t_xB_${xBbin}_Q2_${Q2bin}", h_phi_t).fill(t2, pro_phi_convention)
            hists.computeIfAbsent("/dvcs/corr/pro_theta_trento_xB_${xBbin}_Q2_${Q2bin}", h_theta_trento).fill(TrentoAng2, Math.toDegrees(pro.theta()))
            hists.computeIfAbsent("/dvcs/corr/pro_phi_trento_xB_${xBbin}_Q2_${Q2bin}", h_phi_trento).fill(TrentoAng2, pro_phi_convention)
            hists.computeIfAbsent("/dvcs/corr/gam_theta_t_xB_${xBbin}_Q2_${Q2bin}", h_theta_t).fill(t2, Math.toDegrees(gam.theta()))
            hists.computeIfAbsent("/dvcs/corr/gam_phi_t_xB_${xBbin}_Q2_${Q2bin}", h_phi_t).fill(t2, gam_phi_convention)
            hists.computeIfAbsent("/dvcs/corr/gam_theta_trento_xB_${xBbin}_Q2_${Q2bin}", h_theta_trento).fill(TrentoAng2, Math.toDegrees(gam.theta()))
            hists.computeIfAbsent("/dvcs/corr/gam_phi_trento_xB_${xBbin}_Q2_${Q2bin}", h_phi_trento).fill(TrentoAng2, gam_phi_convention)

            hists.computeIfAbsent("/dvcs/corr/t_t", h_t_t).fill(t, t2)
            hists.computeIfAbsent("/dvcs/corr/trento_trento", h_trento_trento).fill(TrentoAng, TrentoAng2)

            // check CD contents
            if (pro_status>=4000){
              hists.computeIfAbsent("/events/events", h_events).fill(6.5)  
            }
            else if (pro_status<4000 && pro_status>2000){
              hists.computeIfAbsent("/events/events", h_events).fill(7.5)
            }

            // check hidden pi0
            hists.computeIfAbsent("/dvcs/pi0/inv_mass_hidden", h_inv_mass_gg).fill(pi0_hidden.mass())

            hists.computeIfAbsent("/dvcs/yields/heli_$helicity/Q2_xB_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
            hists.computeIfAbsent("/dvcs/yields/heli_$helicity/t_xB_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
            hists.computeIfAbsent("/dvcs/yields/heli_$helicity/trento_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
            hists.computeIfAbsent("/dvcs/yields/heli_$helicity/xB_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_xB_bin).fill(xB)
            hists.computeIfAbsent("/dvcs/yields/heli_$helicity/Q2_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_Q2_bin).fill(Q2)
            hists.computeIfAbsent("/dvcs/yields/heli_$helicity/t_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_t_bin).fill(t2)
            hists.computeIfAbsent("/dvcs/yields/heli_$helicity/phi_xBQ2t_${xBQ2tbin}_phi_${phibin}", h_phi_bin).fill(TrentoAng2)
            
            if (pro_status>=4000){
              hists.computeIfAbsent("/dvcs/yields/heli_$helicity/Q2_xB_pro_CD_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
              hists.computeIfAbsent("/dvcs/yields/heli_$helicity/t_xB_pro_CD_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
              hists.computeIfAbsent("/dvcs/yields/heli_$helicity/trento_pro_CD_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
            }

            if (gam_status<2000){
              hists.computeIfAbsent("/dvcs/yields/heli_$helicity/Q2_xB_gam_FT_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
              hists.computeIfAbsent("/dvcs/yields/heli_$helicity/t_xB_gam_FT_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
              hists.computeIfAbsent("/dvcs/yields/heli_$helicity/trento_gam_FT_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
            }

            if (pro_status>=4000 && gam_status<2000){
              hists.computeIfAbsent("/dvcs/yields/heli_$helicity/Q2_xB_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_Q2_xB).fill(xB,Q2)
              hists.computeIfAbsent("/dvcs/yields/heli_$helicity/t_xB_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_t_xB).fill(xB,t2)
              hists.computeIfAbsent("/dvcs/yields/heli_$helicity/trento_pro_CD_gam_FT_xBQ2t_${xBQ2tbin}", h_cross_section).fill(TrentoAng2)
            }
          } // exclusivity cuts ended
        }//kine cuts ended
      }// event with e, p, g
    }// event with particles
  }
}