package sangbaek
import org.jlab.groot.data.H1F
import java.util.concurrent.ConcurrentHashMap
import org.jlab.groot.data.TDirectory
import my.Sugar


Sugar.enable()

def hists_dvcs = new ConcurrentHashMap()
def hists_pi0 = new ConcurrentHashMap()

def parent = args[0]

def gen = "/dvcs_gen.hipo"
def rec = "/dvcs_EB.hipo"
def corrected = "/dvcs_corr.hipo"

def dir_structure_pi0 = ["/pi0/MC/gen/inb/andrey":"/MC/pi0_andrey_inb"+gen
						,"/pi0/MC/rec/inb/andrey":"/MC/pi0_andrey_inb"+rec
						,"/pi0/MC/gen/outb/andrey":"/MC/pi0_andrey_outb"+gen
						,"/pi0/MC/rec/outb/andrey":"/MC/pi0_andrey_outb"+rec
						,"/pi0/MC/gen/inb/maxime":"/MC/pi0_maxime_inb"+gen
						,"/pi0/MC/rec/inb/maxime":"/MC/pi0_maxime_inb"+rec
						,"/pi0/MC/gen/outb/maxime":"/MC/pi0_maxime_outb"+gen
						,"/pi0/MC/rec/outb/maxime":"/MC/pi0_maxime_outb"+rec
						,"/pi0/MC/gen/inb/harut":"/MC/pi0_harut_inb"+gen
						,"/pi0/MC/rec/inb/harut":"/MC/pi0_harut_inb"+rec
						,"/pi0/data/inb":"/data/inbending"+corrected
						,"/pi0/data/outb":"/data/outbending"+corrected
						]
def dir_structure_dvcs = ["/dvcs/MC/gen/inb/harut":"/MC/dvcs_harut_inb"+gen
						,"/dvcs/MC/rec/inb/harut":"/MC/dvcs_harut_inb"+rec
						,"/dvcs/MC/gen/inb/harut_bkg":"/MC/dvcs_harut_bkg_inb"+gen
						,"/dvcs/MC/rec/inb/harut_bkg":"/MC/dvcs_harut_bkg_inb"+rec
						,"/dvcs/data/inb":"/data/inbending"+corrected
						,"/dvcs/data/outb":"/data/outbending"+corrected
						]

TDirectory out_dvcs = new TDirectory()
out_dvcs.mkdir("/root")
out_dvcs.cd("/root")

TDirectory out_pi0 = new TDirectory()
H1F h_FD, h_FT

def particles = ["/ele", "/pro"]
def variables = ["/theta", "/phi", "/vz"]
def excl_levels = ["/epg", "/excl"]
def excl_levels_pi0 = ["/epg", "/pi0"]


def yields_FT, yields_FD


//dvcs
dir_structure_dvcs.each{key, val->
	TDirectory dir = new TDirectory()
	dir.readFile(parent+val)
	
	// //raw yields
	["-1", "0", "1"].each{heli-> //helicity
		if (key.contains("MC") && heli !="0") return
		out_dvcs.mkdir(key+"/rawyields/heli_$heli/FT")
		out_dvcs.mkdir(key+"/rawyields/heli_$heli/FD")					
	
		(1..24).each{it -> //binning
			yields_FT = "/root/dvcs/yields/heli_$heli/trento_gam_FT_xBQ2t_$it"
			yields_FD = "/root/dvcs/yields/heli_$heli/trento_xBQ2t_$it"
			h_FT = dir.getObject(yields_FT)
			if (h_FT){
				h_FT.setTitle(key+"/rawyields/heli_$heli/FT/trento_gam_FT_xBQ2t_$it")
				h_FT.setName(key+"/rawyields/heli_$heli/FT/trento_gam_FT_xBQ2t_$it")
				hists_dvcs[h_FT.getTitle()] = h_FT
			}
			h_FD = dir.getObject(yields_FD)
			if (h_FD){
				h_FD.setTitle(key+"/rawyields/heli_$heli/FD/trento_gam_FD_xBQ2t_$it")
				h_FD.setName(key+"/rawyields/heli_$heli/FD/trento_gam_FD_xBQ2t_$it")
				if (h_FT) h_FD.sub(h_FT)
				hists_dvcs[h_FD.getTitle()] = h_FD
			}
		}
	}
	// //raw yields end

	// save ele, pro vz, angular distribution
	excl_levels.each{excl->
		variables.each{var->
			(1..6).each{
				def h_ele = dir.getObject("/root"+excl+"/pid"+"/ele"+var+"_S$it")
				h_ele.setName(key+"/pid"+excl+"/ele"+var+"_S$it")
				h_ele.setTitle(key+"/pid"+excl+"/ele"+var+"_S$it")
				hists_dvcs[h_ele.getTitle()] = h_ele
			}
		}
	}

	excl_levels.each{excl->
		variables.each{var->
			(1..6).each{
				h_pro = dir.getObject("/root"+excl+"/pid"+"/pro"+var+"_fd_S$it")
				h_pro.setName(key+"/pid"+excl+"/pro"+var+"_fd_S$it")
				h_pro.setTitle(key+"/pid"+excl+"/pro"+var+"_fd_S$it")
				hists_dvcs[h_pro.getTitle()] = h_pro
			}
		}
	}
}

hists_dvcs.each{
	println(it.key)
	out_dvcs.writeDataSet(it.value)
}
out_dvcs.writeFile('dvcs_sorted.hipo')


//pi0
dir_structure_pi0.each{key, val->
	TDirectory dir = new TDirectory()
	dir.readFile(parent+val)
	
	// //raw yields
	["-1", "0", "1"].each{heli-> //helicity
		if (key.contains("MC") && heli !="0") return
		out_pi0.mkdir(key+"/rawyields/heli_$heli/FT")
		out_pi0.mkdir(key+"/rawyields/heli_$heli/FD")					
	
		(1..24).each{it -> //binning
			yields_FT = "/root/pi0/yields/heli_$heli/trento_gam_FT_xBQ2t_$it"
			yields_FD = "/root/pi0/yields/heli_$heli/trento_xBQ2t_$it"
			h_FT = dir.getObject(yields_FT)
			if (h_FT){
				h_FT.setTitle(key+"/rawyields/heli_$heli/FT/trento_gam_FT_xBQ2t_$it")
				h_FT.setName(key+"/rawyields/heli_$heli/FT/trento_gam_FT_xBQ2t_$it")
				hists_pi0[h_FT.getTitle()] = h_FT
			}
			h_FD = dir.getObject(yields_FD)
			if (h_FD){
				h_FD.setTitle(key+"/rawyields/heli_$heli/FD/trento_gam_FD_xBQ2t_$it")
				h_FD.setName(key+"/rawyields/heli_$heli/FD/trento_gam_FD_xBQ2t_$it")
				if (h_FT) h_FD.sub(h_FT)
				hists_pi0[h_FD.getTitle()] = h_FD
			}
		}
	}
	// //raw yields end

	// save ele, pro vz, angular distribution
	excl_levels_pi0.each{excl->
		variables.each{var->
			(1..6).each{
				def h_ele = dir.getObject("/root"+excl+"/pid"+"/ele"+var+"_S$it")
				h_ele.setName(key+"/pid"+excl+"/ele"+var+"_S$it")
				h_ele.setTitle(key+"/pid"+excl+"/ele"+var+"_S$it")
				hists_pi0[h_ele.getTitle()] = h_ele
			}
		}
	}

	excl_levels_pi0.each{excl->
		variables.each{var->
			(1..6).each{
				h_pro = dir.getObject("/root"+excl+"/pid"+"/pro"+var+"_fd_S$it")
				h_pro.setName(key+"/pid"+excl+"/pro"+var+"_fd_S$it")
				h_pro.setTitle(key+"/pid"+excl+"/pro"+var+"_fd_S$it")
				hists_pi0[h_pro.getTitle()] = h_pro
			}
		}
	}
}

hists_pi0.each{
	println(it.key)
	out_pi0.writeDataSet(it.value)
}
out_pi0.writeFile('pi0_sorted.hipo')
