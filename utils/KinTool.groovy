package utils
import org.jlab.clas.physics.LorentzVector
import org.jlab.clas.physics.Vector3
import org.jlab.clas.pdg.PDGDatabase


class KinTool{

    //move somplace else

    static def calcQ2(LorentzVector beam, LorentzVector measured_el){
        LorentzVector VGS = new LorentzVector(beam)
        VGS.sub(measured_el)
	return -VGS.mass2()
    }

    static def calcXb(LorentzVector beam, LorentzVector measured_el){
        LorentzVector VGS = new LorentzVector(beam)
        VGS.sub(measured_el)
	return calcQ2(beam,measured_el)/(2.0*PDGDatabase.getParticleMass(2212)*VGS.e())
    }

    static def calcT(LorentzVector measured_prot){
	return 2.0*PDGDatabase.getParticleMass(2212)*(measured_prot.e()-PDGDatabase.getParticleMass(2212))
    }

    static def calcNu(LorentzVector beam, LorentzVector measured_el){
	return calcQ2(beam,measured_el)/(2*PDGDatabase.getParticleMass(2212)*calcXb(beam,measured_el))
    }
    
    static def calcY(LorentzVector beam, LorentzVector measured_el){
	return calcNu(beam,measured_el)/beam.e()
    }

    static def calcPhiTrento(LorentzVector beam, LorentzVector measured_el,LorentzVector measured_prot){
	def v3l = beam.vect().cross(measured_el.vect())
    LorentzVector VGS = new LorentzVector(beam)
    VGS.sub(measured_el)
	def v3h = measured_prot.vect().cross(VGS.vect())
	def trento = Math.toDegrees(Math.acos(v3l.dot(v3h)/(v3l.mag()*v3h.mag())))

	if(v3l.dot(measured_prot.vect())<0){trento=360-trento}
	return trento
    }

    static def calcPhiTrento2(LorentzVector beam, LorentzVector measured_el,LorentzVector measured_gam){

    LorentzVector VGS = new LorentzVector(beam)
    def v1 = VGS.vect().cross(measured_el.vect())
    def v2 = VGS.vect().cross(measured_gam.vect())
    def TrentoAng2 = KinTool.Vangle(v1,v2)
    if (VGS.vect().dot(v1.cross(v2))<0) TrentoAng2 = 360 - TrentoAng2
    return TrentoAng2
    }


    static def delta_meas_energy( Double beam,  LorentzVector measured_el ){
	def calc_e = beam/(1+ (beam/PDGDatabase.getParticleMass(2212))*(1-Math.cos(measured_el.theta())) );
	return (calc_e  - measured_el.e() )
    }

    static def delta_meas_theta( Double beam,  LorentzVector measured_el ){
	def calc_theta = Math.toDegrees(Math.acos( 1 + (PDGDatabase.getParticleMass(2212)/beam)*( 1 - beam/measured_el.e()) ))
	return Math.toDegrees((calc_theta  - measured_el.theta() ))
    }

    static def Vangle = {v1, v2 -> 
        if( v1.mag() * v2.mag() !=0 && v1.dot(v2)<v1.mag()*v2.mag() ) return Math.toDegrees( Math.acos(v1.dot(v2)/(v1.mag()*v2.mag()) ) ); 
        else return 0
    }

}


