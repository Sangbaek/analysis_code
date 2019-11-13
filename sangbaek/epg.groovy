import org.jlab.io.hipo.HipoDataSource
import org.jlab.detector.base.DetectorType
import org.jlab.clas.physics.Particle
import org.jlab.clas.physics.Vector3
import org.jlab.groot.data.H1F
import org.jlab.groot.data.H2F
import org.jlab.groot.data.TDirectory
import exclusive.sangbaek.DVCS

def hmm2_ep = new H1F("hmm2_ep", "missing mass squared, ep", 200,-2,4)
def hmm2_eg = new H1F("hmm2_eg", "missing mass squared, eg", 200,-2,4)
def hmm2_epg = new H1F("hmm2_epg", "missing mass squared, epg", 200,-0.2,0.2)
def hangle_epg = new H1F("hangle_epg", "Angle between gamma and epX", 200,-5 ,75)
def hangle_ep_eg = new H1F("hangle_ep_eg", "Angle between two planes, ep and eg", 380,-5,185)

def h_kine_ele = new H2F("h_kine_ele", "e Kinematics", 200,0,40, 200, 0, 10.6)
def h_kine_pro = new H2F("h_kine_pro", "p Kinematics", 200,0,120, 200, 0, 10.6)
def h_kine_gam = new H2F("h_kine_gam", "#gamma Kinematics", 200,0,40, 200, 0, 10.6)
def h_Q2_xB = new H2F("h_Q2_xB", "Q^2 - xB",100,0,1,100,0,12);

def beam = new Particle(11, 0,0,5)//7.546)
def target = new Particle(2212, 0,0,0)

def h_ele_rate = new H1F("h_ele_rate", "h_ele_rate",20,0,90)
def h_pro_rate = new H1F("h_pro_rate", "h_pro_rate",20,0,90)
def h_gam_rate = new H1F("h_gam_rate", "h_gam_rate",20,0,90)

def h_totalevent = new H1F("h_totalevent","total events",1,0,1)
def totalevent = 0

for(fname in args) {
def reader = new HipoDataSource()
reader.open(fname)


while(reader.hasEvent()) {
  totalevent++
  def event = reader.getNextEvent()
  if (event.hasBank("REC::Particle") && event.hasBank("REC::Calorimeter")) {
    def (ele, pro, gam) = DVCS.getEPG(event)*.particle
    def Vangle = {v1, v2 -> 
       if( v1.mag() * v2.mag() !=0 && v1.dot(v2)<v1.mag()*v2.mag() ) return Math.toDegrees( Math.acos(v1.dot(v2)/(v1.mag()*v2.mag()) ) ); 
    }

    if(ele!=null) {
      def epX = new Particle(beam)
      epX.combine(target, 1)
      epX.combine(ele,-1)
      epX.combine(pro,-1)

      def egX = new Particle(beam)
      egX.combine(target, 1)
      egX.combine(ele,-1)
      egX.combine(gam,-1)

      def epgX = new Particle(beam)
      epgX.combine(target, 1)
      epgX.combine(ele,-1)
      epgX.combine(pro,-1)
      epgX.combine(gam,-1)

      def GS = new Particle(beam)
      GS.combine(ele,-1)

      // def VG1 = gam.vector()
      def VGS = GS.vector()
      // def VMISS = epgX.vector()
      // def VmissP = egX.vector()
      // def VmissG = epX.vector()

      mom_gam = gam.vector().vect()
      mom_epX = epX.vector().vect()

      norm_ep = ele.vector().vect().cross(pro.vector().vect())
      norm_eg = ele.vector().vect().cross(gam.vector().vect())

      // if (Math.toDegrees(ele.phi())>0 && Math.toDegrees(ele.phi())<4.5){
      h_ele_rate.fill(Math.toDegrees(ele.theta()))
      // }
      // if (Math.toDegrees(pro.phi())>0 && Math.toDegrees(pro.phi())<4.5){
      h_pro_rate.fill(Math.toDegrees(pro.theta()))
      // }
      // if (Math.toDegrees(pro.phi())>0 && Math.toDegrees(gam.phi())<4.5){      
      h_gam_rate.fill(Math.toDegrees(gam.theta()))
      // }
      hmm2_ep.fill(epX.mass2())
      hmm2_eg.fill(egX.mass2())
      hmm2_epg.fill(epgX.mass2())
      hangle_epg.fill(Vangle(mom_gam,mom_epX))
      hangle_ep_eg.fill(Vangle(norm_ep,norm_eg))
      h_kine_ele.fill(Math.toDegrees(ele.vector().vect().theta()),ele.vector().vect().mag())
      h_kine_pro.fill(Math.toDegrees(pro.vector().vect().theta()),pro.vector().vect().mag())
      h_kine_gam.fill(Math.toDegrees(gam.vector().vect().theta()),gam.vector().vect().mag())
      h_Q2_xB.fill(-VGS.mass2()/(2*0.938*VGS.e()),-VGS.mass2());
    }
  }
}

reader.close()
}

h_totalevent.setBinContent(0,totalevent)

lumi = (double) 1.0558*0.0001
xsec = (double) 9.0285*100000
tot_rate = lumi * xsec
phi_acceptance = (double) 4.5/360
ratio = (double) totalevent/tot_rate
ratio = (double) ratio/phi_acceptance
h_ele_rate.divide(ratio)
h_pro_rate.divide(ratio)
h_gam_rate.divide(ratio)

def out = new TDirectory()
out.mkdir('/spec')
out.cd('/spec')
out.addDataSet(h_totalevent)

out.mkdir('/epg')
out.cd('/epg')
out.addDataSet(hmm2_ep)
out.addDataSet(hmm2_epg)
out.addDataSet(hmm2_eg)
out.addDataSet(hangle_epg)
out.addDataSet(hangle_ep_eg)
out.addDataSet(h_kine_ele)
out.addDataSet(h_kine_pro)
out.addDataSet(h_kine_gam)
out.addDataSet(h_Q2_xB)

out.mkdir('/rates')
out.cd('/rates')
out.addDataSet(h_ele_rate)
out.addDataSet(h_pro_rate)
out.addDataSet(h_gam_rate)

out.writeFile('dvcs_out.hipo')
