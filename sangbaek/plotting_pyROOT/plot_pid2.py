#!/usr/bin/python

import sys
import ROOT
import numpy as np
from matplotlib import pyplot as plt
from array import array
from copy import deepcopy

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetTitleSize(.1,"T")

# ROOT.gStyle.SetTitleOffset(.05,"T")
ROOT.TGaxis.SetMaxDigits(3)
ff1 = ROOT.TFile(sys.argv[1])
if (len(sys.argv)>2):
	ff2 = ROOT.TFile(sys.argv[2])
if (len(sys.argv)>3):
	ff3 = ROOT.TFile(sys.argv[3])
	ff4 = ROOT.TFile(sys.argv[4])

def draw_elecSampling(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',2400,2000)
	# c1.Divide(3,2)

	for i in range(0,6):
		c1.cd(i+1)
		if i==0:
			h1= ff1.Get("root_epg_pid_ele_Sampl_mom_S"+str(i+1))
			h1.Add(ff2.Get("root_epg_pid_ele_Sampl_mom_S"+str(i+1)))
		else:
			h1.Add(ff1.Get("root_epg_pid_ele_Sampl_mom_S"+str(i+1)))
			h1.Add(ff2.Get("root_epg_pid_ele_Sampl_mom_S"+str(i+1)))
	# h1.SetTitle("SF. vs. momentum, all #font[12]{e'} in wagon")
	# h1.SetTitle("SF. vs. momentum, #font[12]{e'} in DVCS candidates")
	h1.SetTitle("")
	h1.GetXaxis().SetTitle("electron momentum (GeV/c)")
	h1.GetYaxis().SetTitle("Sampling Fraction")
	h1.GetXaxis().SetRangeUser(0, 10)
	h1.GetYaxis().SetRangeUser(0, 0.35)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetZaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetLabelSize(0.04)
	h1.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLeftMargin(0.15)
	ROOT.gPad.SetRightMargin(0.14)
	ROOT.gPad.SetLogz()
	h1.Draw("colz")
	c1.Print("elec_Sampl.pdf")
# 
def draw_elecPCALECAL(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',2400,2000)

	for i in range(0,6):
		c1.cd(i+1)
		if i==0:
			h1= ff1.Get("root_excl_pid_ele_pcalecal_S"+str(i+1))
			h1.Add(ff2.Get("root_excl_pid_ele_pcalecal_S"+str(i+1)))
		else:
			h1.Add(ff1.Get("root_excl_pid_ele_pcalecal_S"+str(i+1)))
			h1.Add(ff2.Get("root_excl_pid_ele_pcalecal_S"+str(i+1)))
	# h1.SetTitle("Edep/p, PCAL vs. ECAL Inner, all #font[12]{e'} in wagon")
	# h1.SetTitle("Edep/p, PCAL vs. ECAL Inner, #font[12]{e'} in DVCS candidates")
	h1.SetTitle("")
	h1.GetXaxis().SetTitle("Edep/p, ECAL Inner")
	h1.GetYaxis().SetTitle("Edep/p, PCAL ")
	h1.GetXaxis().SetRangeUser(0, 0.3)
	h1.GetYaxis().SetRangeUser(0, 0.3)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetZaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetLabelSize(0.04)
	h1.GetZaxis().SetLabelSize(0.04)
	# h1.GetZaxis().SetNoExponent()
	h1.GetZaxis().SetMaxDigits(1)
	# h1.GetZaxis().SetRangeUser(0,31000)
	c1.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	ROOT.gPad.SetRightMargin(0.14)
	h1.Draw("colz")
	c1.Print("elec_PCALECAL.pdf")


def draw_elecKinematics(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',1600,1200)
	c1.Divide(2,2)

	h1 = ff1.Get("root_excl_pid_ele_vz_mom_S"+str(0+1))
	h2 = ff1.Get("root_excl_pid_ele_vz_theta_S"+str(0+1))
	h3 = ff1.Get("root_excl_pid_ele_theta_phi_S"+str(0+1))
	h4 = ff1.Get("root_excl_pid_ele_theta_mom_S"+str(0+1))

	for i in range(1,6):
		h1.Add(ff1.Get("root_excl_pid_ele_vz_mom_S"+str(i+1)))
		h2.Add(ff1.Get("root_excl_pid_ele_vz_theta_S"+str(i+1)))
		h3.Add(ff1.Get("root_excl_pid_ele_theta_phi_S"+str(i+1)))
		h4.Add(ff1.Get("root_excl_pid_ele_theta_mom_S"+str(i+1)))

	for i in range(0,6):
		h1.Add(ff2.Get("root_excl_pid_ele_vz_mom_S"+str(i+1)))
		h2.Add(ff2.Get("root_excl_pid_ele_vz_theta_S"+str(i+1)))
		h3.Add(ff2.Get("root_excl_pid_ele_theta_phi_S"+str(i+1)))
		h4.Add(ff2.Get("root_excl_pid_ele_theta_mom_S"+str(i+1)))


	c1.cd(1)
	h1.SetTitle("#font[12]{e'}, #font[12]{vz} vs. #font[12]{p} all sectors in FD")
	h1.GetXaxis().SetTitle("#font[12]{e'},  #font[12]{p} (GeV/c)")
	h1.GetYaxis().SetTitle("#font[12]{e'},  #font[12]{vz} (cm)")
	h1.GetXaxis().SetRangeUser(1, 8)
	h1.GetYaxis().SetRangeUser(-18, 12)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetZaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetLabelSize(0.04)
	h1.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	h1.Draw("colz")

	c1.cd(2)
	h2.SetTitle("#font[12]{e'}, #font[12]{vz} vs. #theta all sectors in FD")
	h2.GetXaxis().SetTitle("#font[12]{e'},  #theta (#circ)")
	h2.GetYaxis().SetTitle("#font[12]{e'},  #font[12]{vz} (cm)")
	h2.GetXaxis().SetRangeUser(0, 40)
	h2.GetYaxis().SetRangeUser(-18, 12)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetYaxis().SetTitleSize(0.05)
	h2.GetZaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.04)
	h2.GetYaxis().SetLabelSize(0.04)
	h2.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	h2.Draw("colz")

	c1.cd(3)
	h3.SetTitle("#font[12]{e'}, #theta vs. #phi all sectors in FD")
	h3.GetXaxis().SetTitle("#font[12]{e'},  #phi (#circ)")
	h3.GetYaxis().SetTitle("#font[12]{e'},  #theta (#circ)")
	h3.GetYaxis().SetRangeUser(0, 40)
	h3.GetXaxis().SetTitleSize(0.05)
	h3.GetYaxis().SetTitleSize(0.05)
	h3.GetZaxis().SetTitleSize(0.05)
	h3.GetXaxis().SetLabelSize(0.04)
	h3.GetYaxis().SetLabelSize(0.04)
	h3.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	h3.Draw("colz")

	c1.cd(4)
	h4.SetTitle("#font[12]{e'}, #theta vs. #font[12]{p} all sectors in FD")
	h4.GetXaxis().SetTitle("#font[12]{e'},  #font[12]{p} (GeV/c)")
	h4.GetYaxis().SetTitle("#font[12]{e'},  #theta (#circ)")
	h4.GetXaxis().SetRangeUser(1, 8)
	h4.GetYaxis().SetRangeUser(0, 40)
	h4.GetXaxis().SetTitleSize(0.05)
	h4.GetYaxis().SetTitleSize(0.05)
	h4.GetZaxis().SetTitleSize(0.05)
	h4.GetXaxis().SetLabelSize(0.04)
	h4.GetYaxis().SetLabelSize(0.04)
	h4.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	h4.Draw("colz")

	c1.Print("elec_kinematics.pdf")

def draw_protKinematics_FD(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',2400,1200)
	c1.Divide(3,2)

	h1 = ff1.Get("root_excl_pid_pro_vz_mom_fd_S"+str(0+1))
	h2 = ff1.Get("root_excl_pid_pro_vzdiff_mom_fd_S"+str(0+1))
	h3 = ff1.Get("root_excl_pid_pro_vz_theta_fd_S"+str(0+1))
	h4 = ff1.Get("root_excl_pid_pro_theta_phi_fd_S"+str(0+1))
	h5 = ff1.Get("root_excl_pid_pro_theta_mom_fd_S"+str(0+1))

	for i in range(1,6):
		h1.Add(ff1.Get("root_excl_pid_pro_vz_mom_fd_S"+str(i+1)))
		h2.Add(ff1.Get("root_excl_pid_pro_vzdiff_mom_fd_S"+str(i+1)))
		h3.Add(ff1.Get("root_excl_pid_pro_vz_theta_fd_S"+str(i+1)))
		h4.Add(ff1.Get("root_excl_pid_pro_theta_phi_fd_S"+str(i+1)))
		h5.Add(ff1.Get("root_excl_pid_pro_theta_mom_fd_S"+str(i+1)))
	for i in range(0,6):
		h1.Add(ff2.Get("root_excl_pid_pro_vz_mom_fd_S"+str(i+1)))
		h2.Add(ff2.Get("root_excl_pid_pro_vzdiff_mom_fd_S"+str(i+1)))
		h3.Add(ff2.Get("root_excl_pid_pro_vz_theta_fd_S"+str(i+1)))
		h4.Add(ff2.Get("root_excl_pid_pro_theta_phi_fd_S"+str(i+1)))
		h5.Add(ff2.Get("root_excl_pid_pro_theta_mom_fd_S"+str(i+1)))

	label = "all sectors in FD"

	c1.cd(1)
	h1.SetTitle("#font[12]{p'}, #font[12]{vz} vs. #font[12]{p} "+label)
	h1.GetXaxis().SetTitle("#font[12]{p'}, #font[12]{p} (GeV/c)")
	h1.GetYaxis().SetTitle("#font[12]{p'}, #font[12]{vz} (cm)")
	h1.GetXaxis().SetRangeUser(0, 6)
	h1.GetYaxis().SetRangeUser(-18, 12)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetZaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetLabelSize(0.04)
	h1.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h1.Draw("colz")

	c1.cd(2)
	h2.SetTitle("#font[12]{p'}, #font[12]{vz(p')}-#font[12]{vz(e')} vs. #font[12]{p} "+label)
	h2.GetXaxis().SetTitle("#font[12]{p'}, #font[12]{p} (GeV/c)")
	h2.GetYaxis().SetTitle("#font[12]{p'}, #font[12]{vz_{p'}} - #font[12]{vz_{e'}} (cm)")
	h2.GetXaxis().SetRangeUser(0, 6)
	h2.GetYaxis().SetRangeUser(-7, 7)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetYaxis().SetTitleSize(0.05)
	h2.GetZaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.04)
	h2.GetYaxis().SetLabelSize(0.04)
	h2.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h2.Draw("colz")

	c1.cd(3)
	h3.SetTitle("#font[12]{p'}, #font[12]{vz} vs. #theta "+label)
	h3.GetXaxis().SetTitle("#font[12]{p'}, #theta (#circ)")
	h3.GetYaxis().SetTitle("#font[12]{p'}, #font[12]{vz} (cm)")
	h3.GetXaxis().SetRangeUser(0, 40)
	h3.GetYaxis().SetRangeUser(-18, 12)
	h3.GetXaxis().SetTitleSize(0.05)
	h3.GetYaxis().SetTitleSize(0.05)
	h3.GetZaxis().SetTitleSize(0.05)
	h3.GetXaxis().SetLabelSize(0.04)
	h3.GetYaxis().SetLabelSize(0.04)
	h3.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h3.Draw("colz")

	c1.cd(4)
	h4.SetTitle("#font[12]{p'} #theta vs. #phi "+label)
	h4.GetXaxis().SetTitle("#font[12]{p'}, #phi (#circ)")
	h4.GetYaxis().SetTitle("#font[12]{p'}, #theta (#circ)")
	h4.GetYaxis().SetRangeUser(0, 50)
	h4.GetXaxis().SetTitleSize(0.05)
	h4.GetYaxis().SetTitleSize(0.05)
	h4.GetZaxis().SetTitleSize(0.05)
	h4.GetXaxis().SetLabelSize(0.04)
	h4.GetYaxis().SetLabelSize(0.04)
	h4.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h4.Draw("colz")

	c1.cd(5)
	h5.SetTitle("#font[12]{p'} #theta vs. #font[12]{p} "+label)
	h5.GetXaxis().SetTitle("#font[12]{p'}, #font[12]{p} (GeV/c)")
	h5.GetYaxis().SetTitle("#font[12]{p'}, #theta (#circ)")
	h5.GetXaxis().SetRangeUser(0, 6)
	h5.GetYaxis().SetRangeUser(0, 50)
	h5.GetXaxis().SetTitleSize(0.05)
	h5.GetYaxis().SetTitleSize(0.05)
	h5.GetZaxis().SetTitleSize(0.05)
	h5.GetXaxis().SetLabelSize(0.04)
	h5.GetYaxis().SetLabelSize(0.04)
	h5.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h5.Draw("colz")

	c1.Print("prot_kinematics_FD.pdf")

def draw_protKinematics_CD(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',2400,1200)
	c1.Divide(3,2)


	h1 = ff1.Get("root_excl_pid_pro_vz_mom_cd")
	h1.Add(ff2.Get("root_excl_pid_pro_vz_mom_cd"))
	h2 = ff1.Get("root_excl_pid_pro_vzdiff_mom_cd")
	h2.Add(ff2.Get("root_excl_pid_pro_vzdiff_mom_cd"))
	h3 = ff1.Get("root_excl_pid_pro_vz_theta_cd")
	h3.Add(ff2.Get("root_excl_pid_pro_vz_theta_cd"))
	h4 = ff1.Get("root_excl_pid_pro_theta_phi_cd")
	h4.Add(ff2.Get("root_excl_pid_pro_theta_phi_cd"))
	h5 = ff1.Get("root_excl_pid_pro_theta_mom_cd")
	h5.Add(ff2.Get("root_excl_pid_pro_theta_mom_cd"))

	label = "in CD"

	c1.cd(1)
	h1.SetTitle("#font[12]{p'}, #font[12]{vz} vs. #font[12]{p} "+label)
	h1.GetXaxis().SetTitle("#font[12]{p'}, #font[12]{p} (GeV/c)")
	h1.GetYaxis().SetTitle("#font[12]{p'}, #font[12]{vz} (cm)")
	h1.GetXaxis().SetRangeUser(0, 4)
	h1.GetYaxis().SetRangeUser(-10, 5)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetZaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetLabelSize(0.04)
	h1.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h1.Draw("colz")

	c1.cd(2)
	h2.SetTitle("#font[12]{p'}, #font[12]{vz(p')}-#font[12]{vz(e')} vs. #font[12]{p} "+label)
	h2.GetXaxis().SetTitle("#font[12]{p'}, #font[12]{p} (GeV/c)")
	h2.GetYaxis().SetTitle("#font[12]{p'}, #font[12]{vz_{p'}} - #font[12]{vz_{e'}} (cm)")
	h2.GetXaxis().SetRangeUser(0, 4)
	h2.GetYaxis().SetRangeUser(-10, 10)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetYaxis().SetTitleSize(0.05)
	h2.GetZaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.04)
	h2.GetYaxis().SetLabelSize(0.04)
	h2.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h2.Draw("colz")

	c1.cd(3)
	h3.SetTitle("#font[12]{p'}, #font[12]{vz} vs. #theta "+label)
	h3.GetXaxis().SetTitle("#font[12]{p'} #theta (#circ)")
	h3.GetYaxis().SetTitle("#font[12]{p'} vz (cm)")
	h3.GetXaxis().SetRangeUser(35, 70)
	h3.GetYaxis().SetRangeUser(-18, 12)
	h3.GetXaxis().SetTitleSize(0.05)
	h3.GetYaxis().SetTitleSize(0.05)
	h3.GetZaxis().SetTitleSize(0.05)
	h3.GetXaxis().SetLabelSize(0.04)
	h3.GetYaxis().SetLabelSize(0.04)
	h3.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h3.Draw("colz")

	c1.cd(4)
	h4.SetTitle("#font[12]{p'}, #theta vs. #phi "+label)
	h4.GetXaxis().SetTitle("#font[12]{p'} #phi (#circ)")
	h4.GetYaxis().SetTitle("#font[12]{p'} #theta (#circ)")
	h4.GetYaxis().SetRangeUser(35, 70)
	h4.GetXaxis().SetTitleSize(0.05)
	h4.GetYaxis().SetTitleSize(0.05)
	h4.GetZaxis().SetTitleSize(0.05)
	h4.GetXaxis().SetLabelSize(0.04)
	h4.GetYaxis().SetLabelSize(0.04)
	h4.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h4.Draw("colz")

	c1.cd(5)
	h5.SetTitle("#font[12]{p'}, #theta vs. #font[12]{p} "+label)
	h5.GetXaxis().SetTitle("#font[12]{p'}, #font[12]{p} (GeV/c)")
	h5.GetYaxis().SetTitle("#font[12]{p'}, #theta (#circ)")
	h5.GetXaxis().SetRangeUser(0, 4)
	h5.GetYaxis().SetRangeUser(35, 70)
	h5.GetXaxis().SetTitleSize(0.05)
	h5.GetYaxis().SetTitleSize(0.05)
	h5.GetZaxis().SetTitleSize(0.05)
	h5.GetXaxis().SetLabelSize(0.04)
	h5.GetYaxis().SetLabelSize(0.04)
	h5.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h5.Draw("colz")

	c1.Print("prot_kinematics_CD.pdf")

def draw_photKinematics_FD(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',2400,1200)
	c1.Divide(2,1)

	h1 = ff1.Get("root_excl_pid_gam_theta_phi_fd_S"+str(0+1))
	h2 = ff1.Get("root_excl_pid_gam_theta_mom_fd_S"+str(0+1))

	for i in range(1,6):
		h1.Add(ff1.Get("root_excl_pid_gam_theta_phi_fd_S"+str(i+1)))
		h2.Add(ff1.Get("root_excl_pid_gam_theta_mom_fd_S"+str(i+1)))
	for i in range(0,6):
		h1.Add(ff2.Get("root_excl_pid_gam_theta_phi_fd_S"+str(i+1)))
		h2.Add(ff2.Get("root_excl_pid_gam_theta_mom_fd_S"+str(i+1)))

	label = "all sectors in FD"

	c1.cd(1)
	h1.SetTitle("#font[12]{#gamma}, #theta vs. #phi "+label)
	h1.GetXaxis().SetTitle("#font[12]{#gamma}, #phi (#circ)")
	h1.GetYaxis().SetTitle("#font[12]{#gamma}, #theta (#circ)")
	h1.GetYaxis().SetRangeUser(0, 40)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetZaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetLabelSize(0.04)
	h1.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h1.Draw("colz")

	c1.cd(2)
	h2.SetTitle("#font[12]{#gamma}, #theta vs. #font[12]{p} "+label)
	h2.GetXaxis().SetTitle("#font[12]{#gamma}, #font[12]{p} (GeV/c)")
	h2.GetYaxis().SetTitle("#font[12]{#gamma}, #theta (#circ)")
	h2.GetXaxis().SetRangeUser(2, 9)
	h2.GetYaxis().SetRangeUser(0, 40)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetYaxis().SetTitleSize(0.05)
	h2.GetZaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.04)
	h2.GetYaxis().SetLabelSize(0.04)
	h2.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h2.Draw("colz")

	c1.Print("phot_kinematics_FD.pdf")

def draw_photKinematics_FT(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',2400,1200)
	c1.Divide(2,1)

	h1 = ff1.Get("root_excl_pid_gam_theta_phi_ft")
	h1.Add(ff2.Get("root_excl_pid_gam_theta_phi_ft"))
	h2 = ff1.Get("root_excl_pid_gam_theta_mom_ft")
	h2.Add(ff2.Get("root_excl_pid_gam_theta_mom_ft"))

	label = "in FT"

	c1.cd(1)
	h1.SetTitle("#font[12]{#gamma}, #theta vs. #phi "+label)
	h1.GetXaxis().SetTitle("#font[12]{#gamma}, #phi (#circ)")
	h1.GetYaxis().SetTitle("#font[12]{#gamma}, #theta (#circ)")
	h1.GetYaxis().SetRangeUser(1, 6)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetZaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetLabelSize(0.04)
	h1.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h1.Draw("colz")

	c1.cd(2)
	h2.SetTitle("#font[12]{#gamma}, #theta vs. #font[12]{p} "+label)
	h2.GetXaxis().SetTitle("#font[12]{#gamma}, #font[12]{p} (GeV/c)")
	h2.GetYaxis().SetTitle("#font[12]{#gamma}, #theta (#circ)")
	h2.GetXaxis().SetRangeUser(2, 9)
	h2.GetYaxis().SetRangeUser(1, 6)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetYaxis().SetTitleSize(0.05)
	h2.GetZaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.04)
	h2.GetYaxis().SetLabelSize(0.04)
	h2.GetZaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLogz()
	ROOT.gPad.SetLeftMargin(0.15)
	h2.Draw("colz")

	c1.Print("phot_kinematics_FT.pdf")


def draw_exclCuts(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',1100,1000)
	c1.Divide(2,2)

	h1 = ff1.Get("root_excl_cuts_none_cone_angle")
	h2 = ff1.Get("root_excl_cuts_none_recon_gam_cone_angle")
	h3 = ff1.Get("root_excl_cuts_none_coplanarity")
	h4 = ff1.Get("root_excl_cuts_none_missing_energy")
	h5 = ff1.Get("root_excl_cuts_none_missing_mass_epg")
	h6 = ff1.Get("root_excl_cuts_none_missing_mass_eg")
	h7 = ff1.Get("root_excl_cuts_none_missing_mass_ep")
	h8 = ff1.Get("root_excl_cuts_none_missing_pt")
	h1.Add(ff2.Get("root_excl_cuts_none_cone_angle"))
	h2.Add(ff2.Get("root_excl_cuts_none_recon_gam_cone_angle"))
	h3.Add(ff2.Get("root_excl_cuts_none_coplanarity"))
	h4.Add(ff2.Get("root_excl_cuts_none_missing_energy"))
	h5.Add(ff2.Get("root_excl_cuts_none_missing_mass_epg"))
	h6.Add(ff2.Get("root_excl_cuts_none_missing_mass_eg"))
	h7.Add(ff2.Get("root_excl_cuts_none_missing_mass_ep"))
	h8.Add(ff2.Get("root_excl_cuts_none_missing_pt"))

	i1 = ff1.Get("root_excl_cuts_all_cone_angle")
	i2 = ff1.Get("root_excl_cuts_all_recon_gam_cone_angle")
	i3 = ff1.Get("root_excl_cuts_all_coplanarity")
	i4 = ff1.Get("root_excl_cuts_all_missing_energy")
	i5 = ff1.Get("root_excl_cuts_all_missing_mass_epg")
	i6 = ff1.Get("root_excl_cuts_all_missing_mass_eg")
	i7 = ff1.Get("root_excl_cuts_all_missing_mass_ep")
	i8 = ff1.Get("root_excl_cuts_all_missing_pt")
	i1.Add(ff2.Get("root_excl_cuts_all_cone_angle"))
	i2.Add(ff2.Get("root_excl_cuts_all_recon_gam_cone_angle"))
	i3.Add(ff2.Get("root_excl_cuts_all_coplanarity"))
	i4.Add(ff2.Get("root_excl_cuts_all_missing_energy"))
	i5.Add(ff2.Get("root_excl_cuts_all_missing_mass_epg"))
	i6.Add(ff2.Get("root_excl_cuts_all_missing_mass_eg"))
	i7.Add(ff2.Get("root_excl_cuts_all_missing_mass_ep"))
	i8.Add(ff2.Get("root_excl_cuts_all_missing_pt"))

	# c1.cd(1)
	# h1.SetTitle("")
	# h1.GetXaxis().SetTitle("")
	# # h1.GetXaxis().SetTitle("#theta_{e#gamma} (#circ)")
	# h1.GetXaxis().SetRangeUser(0, 40)
	# h1.SetLineColor(ROOT.kBlue)
	# h1.GetXaxis().SetLabelSize(0.07)
	# h1.GetYaxis().SetLabelSize(0.05)
	# h1.GetXaxis().SetTitleSize(0.07)
	# ROOT.gPad.SetBottomMargin(0.12)
	# h1.GetXaxis().SetNdivisions(-508, ROOT.kTRUE);

	# h1.Draw()
	# i1.SetLineColor(ROOT.kRed)
	# i1.Draw("SAME")

	# c1.cd(2)
	# h2.SetTitle("")
	# h2.GetXaxis().SetTitle("")
	# # h2.GetXaxis().SetTitle("#theta_{#gamma_{det}#gamma_{rec}} (#circ)")
	# h2.GetXaxis().SetRangeUser(-1, 10)
	# h2.SetLineColor(ROOT.kBlue)
	# h2.GetXaxis().SetLabelSize(0.07)
	# h2.GetYaxis().SetLabelSize(0.05)
	# h2.GetXaxis().SetTitleSize(0.07)
	# ROOT.gPad.SetBottomMargin(0.12)
	# h2.GetYaxis().SetNdivisions(505, ROOT.kTRUE);
	# h2.Draw()
	# i2.SetLineColor(ROOT.kRed)
	# i2.Draw("SAME")

	# c1.cd(3)
	# h3.SetTitle("")
	# h3.GetXaxis().SetTitle("#Delta#phi (#circ)")
	# h3.GetXaxis().SetTitle("")
	# h3.GetXaxis().SetRangeUser(-1, 10)
	# h3.SetLineColor(ROOT.kBlue)
	# h3.GetXaxis().SetLabelSize(0.07)
	# h3.GetYaxis().SetLabelSize(0.05)
	# h3.GetXaxis().SetTitleSize(0.07)
	# ROOT.gPad.SetBottomMargin(0.12)
	# h3.Draw()
	# i3.SetLineColor(ROOT.kRed)
	# i3.Draw("SAME")

	# c1.cd(4)
	# h4.SetTitle("")
	# # h4.GetXaxis().SetTitle("ME_{ep#gamma} (GeV)")
	# h4.GetXaxis().SetRangeUser(-1, 1.5)
	# h4.SetLineColor(ROOT.kBlue)
	# h4.GetXaxis().SetLabelSize(0.07)
	# h4.GetYaxis().SetLabelSize(0.05)
	# h4.GetXaxis().SetTitleSize(0.07)
	# ROOT.gPad.SetBottomMargin(0.12)
	# h4.Draw()
	# i4.SetLineColor(ROOT.kRed)
	# i4.Draw("SAME")

	c1.cd(1)
	h5.SetTitle("")
	# h5.GetXaxis().SetTitle("MM^{2}_{ep#gamma} (GeV^{2})")
	h5.GetXaxis().SetTitle("")
	h5.GetXaxis().SetRangeUser(-0.1, 0.1)
	h5.SetLineColor(ROOT.kBlue)
	h5.GetXaxis().SetLabelSize(0.07)
	h5.GetYaxis().SetLabelSize(0.05)
	h5.GetXaxis().SetTitleSize(0.07)
	h5.GetXaxis().SetNdivisions(-504, ROOT.kTRUE);
	ROOT.gPad.SetBottomMargin(0.12)
	h5.Draw()
	i5.SetLineColor(ROOT.kRed)
	i5.Draw("SAME")

	c1.cd(2)
	h6.SetTitle("")
	# h6.GetXaxis().SetTitle("MM^{2}_{e#gamma} (GeV^{2})")
	h6.GetXaxis().SetTitle("")
	h6.GetXaxis().SetRangeUser(-1, 2.5)
	h6.SetLineColor(ROOT.kBlue)
	h6.GetXaxis().SetLabelSize(0.07)
	h6.GetYaxis().SetLabelSize(0.05)
	h6.GetXaxis().SetTitleSize(0.07)
	ROOT.gPad.SetBottomMargin(0.12)
	h6.Draw()
	i6.SetLineColor(ROOT.kRed)
	i6.Draw("SAME")

	c1.cd(3)
	h7.SetTitle("")
	# h7.GetXaxis().SetTitle("MM^{2}_{ep} (GeV^{2})")
	h7.GetXaxis().SetTitle("")
	h7.GetXaxis().SetRangeUser(-1, 1)
	h7.SetLineColor(ROOT.kBlue)
	h7.GetXaxis().SetLabelSize(0.07)
	h7.GetYaxis().SetLabelSize(0.05)
	h7.GetXaxis().SetTitleSize(0.07)
	ROOT.gPad.SetBottomMargin(0.12)
	h7.GetXaxis().SetNdivisions(-504, ROOT.kTRUE);
	h7.Draw()
	i7.SetLineColor(ROOT.kRed)
	i7.Draw("SAME")

	c1.cd(4)
	h8.SetTitle("")
	# h8.GetXaxis().SetTitle("MPt_{ep#gamma} (GeV/c)")
	h8.GetXaxis().SetTitle("")
	h8.GetXaxis().SetRangeUser(0, 0.8)
	h8.SetLineColor(ROOT.kBlue)
	h8.GetXaxis().SetLabelSize(0.07)
	h8.GetYaxis().SetLabelSize(0.05)
	h8.GetXaxis().SetTitleSize(0.07)
	ROOT.gPad.SetBottomMargin(0.12)
	h8.GetXaxis().SetNdivisions(-204, ROOT.kTRUE);
	h8.Draw()
	i8.SetLineColor(ROOT.kRed)
	i8.Draw("SAME")

	c1.Print("excl_cuts.pdf")

def draw_exclCutsMEMM(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',1600,600)
	c1.Divide(2,1)

	h1 = ff1.Get("root_excl_cuts_none_mm2epg_me")
	h1.Add(ff2.Get("root_excl_cuts_none_mm2epg_me"))
	h2 = ff1.Get("root_excl_cuts_all_mm2epg_me")
	h2.Add(ff2.Get("root_excl_cuts_all_mm2epg_me"))

	c1.cd(1)
	h1.SetTitle("no cut")
	h1.GetYaxis().SetTitle("MM^{2}_{ep#gamma} (GeV^{2})")
	h1.GetXaxis().SetTitle("ME_{ep#gamma} (GeV)")
	h1.GetXaxis().SetRangeUser(-1, 2)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLeftMargin(0.15)
	ROOT.gPad.SetRightMargin(0.18)
	ROOT.gPad.SetBottomMargin(0.12)
	ROOT.gPad.SetLogz()
	h1.Draw("colz")

	c1.cd(2)
	h2.SetTitle("all cuts")
	h2.GetYaxis().SetTitle("MM^{2}_{ep#gamma} (GeV^{2})")
	h2.GetXaxis().SetTitle("ME_{ep#gamma} (GeV)")
	h2.GetXaxis().SetRangeUser(-1, 2)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.04)
	h2.GetYaxis().SetTitleSize(0.05)
	h2.GetYaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLeftMargin(0.15)
	ROOT.gPad.SetRightMargin(0.18)
	ROOT.gPad.SetBottomMargin(0.12)
	ROOT.gPad.SetLogz()
	h2.Draw("colz")

	c1.Print("MM2ME.pdf")

def draw_twoPhotons(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',1600,600)
	c1.Divide(2,1)

	h1 = ff1.Get("root_dvcs_number_of_photons")
	h1.Add(ff2.Get("root_dvcs_number_of_photons"))
	h2 = ff1.Get("root_dvcs_pi0_h_inv_mass_gg")
	h2.Add(ff2.Get("root_dvcs_pi0_h_inv_mass_gg"))

	c1.cd(1)
	h1.SetTitle("Number of photons in exclusive events")
	h1.GetXaxis().SetTitle("Number of photons")
	h1.GetXaxis().SetRangeUser(1, 6)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.05)
	h1.GetXaxis().SetBinLabel(2,"1")
	h1.GetXaxis().SetBinLabel(3,"2")
	h1.GetXaxis().SetBinLabel(4,"3")
	h1.GetXaxis().SetBinLabel(5,"4")
	h1.GetXaxis().SetBinLabel(6,"5")
	# h1.GetXaxis().SetBinLabel(5,"6")
	ROOT.gPad.SetLogy()
	ROOT.gPad.SetBottomMargin(0.15)
	h1.Draw()

	c1.cd(2)
	h2.SetTitle("Invariant mass of two photons")
	h2.GetXaxis().SetTitle("IM_{#gamma_{1}#gamma_{2}} (GeV)")
	# h2.GetXaxis().SetRangeUser(-0.1, 0.2)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.05)
	ROOT.gPad.SetBottomMargin(0.15)
	h2.Draw()

	c1.Print("multi_photons.pdf")

def draw_twoPhotons2(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',1600,600)
	c1.Divide(2,1)

	h1 = ff1.Get("root_dvcs_pi0_number_of_photons_gam1_energy")
	h1.Add(ff2.Get("root_dvcs_pi0_number_of_photons_gam1_energy"))
	h2 = ff1.Get("root_dvcs_pi0_number_of_photons_gam2_energy")
	h2.Add(ff2.Get("root_dvcs_pi0_number_of_photons_gam2_energy"))

	c1.cd(1)
	h1.SetTitle("Number of photons vs. #gamma_{1} energy")
	h1.GetXaxis().SetTitle("E_{#gamma1} (GeV)")
	h1.GetYaxis().SetTitle("Number of photons")
	h1.GetXaxis().SetRangeUser(0, 8)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.05)
	h1.GetYaxis().SetRangeUser(2, 6)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetLabelSize(0.1)
	h1.GetYaxis().SetBinLabel(3,"2")
	h1.GetYaxis().SetBinLabel(4,"3")
	h1.GetYaxis().SetBinLabel(5,"4")
	h1.GetYaxis().SetBinLabel(6,"5")
	ROOT.gPad.SetBottomMargin(0.15)
	ROOT.gPad.SetLogz()
	# ROOT.gPad.SetLeftMargin(0.2)
	h1.Draw("colz")

	c1.cd(2)
	h2.SetTitle("Number of photons vs. #gamma_{2} energy")
	h2.GetXaxis().SetTitle("E_{#gamma2} (GeV)")
	h2.GetYaxis().SetTitle("Number of photons")
	h2.GetXaxis().SetRangeUser(0, 8)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.05)
	h2.GetYaxis().SetRangeUser(2, 6)
	h2.GetYaxis().SetTitleSize(0.05)
	h2.GetYaxis().SetLabelSize(0.1)
	h2.GetYaxis().SetBinLabel(3,"2")
	h2.GetYaxis().SetBinLabel(4,"3")
	h2.GetYaxis().SetBinLabel(5,"4")
	h2.GetYaxis().SetBinLabel(6,"5")
	h2.GetYaxis().SetLabelSize(0.1)
	ROOT.gPad.SetBottomMargin(0.15)
	ROOT.gPad.SetLogz()
	h2.Draw("colz")

	c1.cd(2)
	h2.SetTitle("Number of photons vs. #gamma_{3} energy")
	h2.GetXaxis().SetTitle("E_{#gamma2} (GeV)")
	h2.GetYaxis().SetTitle("Number of photons")
	h2.GetXaxis().SetRangeUser(0, 8)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.05)
	h2.GetYaxis().SetRangeUser(2, 6)
	h2.GetYaxis().SetTitleSize(0.05)
	h2.GetYaxis().SetLabelSize(0.1)
	h2.GetYaxis().SetBinLabel(3,"2")
	h2.GetYaxis().SetBinLabel(4,"3")
	h2.GetYaxis().SetBinLabel(5,"4")
	h2.GetYaxis().SetBinLabel(6,"5")
	h2.GetYaxis().SetLabelSize(0.1)
	# ROOT.gPad.SetBottomMargin(0.15)
	ROOT.gPad.SetLogz()
	h2.Draw("colz")


	c1.Print("multi_photons2.pdf")

def draw_twoPhotons3(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',1600,600)
	c1.Divide(2,1)

	h1 = ff1.Get("root_dvcs_pi0_h_inv_mass_gg")
	h1.Add(ff2.Get("root_dvcs_pi0_h_inv_mass_gg"))
	h2 = ff1.Get("root_dvcs_pi0_gam3_h_inv_mass_gg")
	h2.Add(ff2.Get("root_dvcs_pi0_gam3_h_inv_mass_gg"))

	c1.cd(1)
	h1.SetTitle("Invariant mass of #gamma_{1}#gamma_{2}")
	h1.GetXaxis().SetTitle("IM_{#gamma_{1}#gamma_{2}} (GeV)")
	# h1.GetXaxis().SetRangeUser(-0.1, 0.2)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.05)
	ROOT.gPad.SetBottomMargin(0.15)
	h1.Draw()

	c1.cd(2)
	h2.SetTitle("Invariant mass of #gamma_{1}#gamma_{3}")
	h2.GetXaxis().SetTitle("IM_{#gamma_{1}#gamma_{3}} (GeV)")
	# h2.GetXaxis().SetRangeUser(-0.1, 0.2)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.05)
	ROOT.gPad.SetBottomMargin(0.15)
	h2.Draw()

	c1.Print("pi0_inv_mass.pdf")

def draw_corrPlot_tcoltmin(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',1600,600)
	c1.Divide(2,1)

	h1 = ff1.Get("root_dvcs_corr_tcol")
	h2 = ff1.Get("root_dvcs_corr_tmin")
	h3 = ff1.Get("root_dvcs_binning_h_Q2_xB")
	h1.Add(ff2.Get("root_dvcs_corr_tcol"))
	h2.Add(ff2.Get("root_dvcs_corr_tmin"))
	h3.Add(ff2.Get("root_dvcs_binning_h_Q2_xB"))

	h1.Divide(h3)
	h2.Divide(h3)

	c1.cd(1)
	h1.SetTitle("-t_{col} distribution over (x_{B}, Q^{2})")
	h1.GetXaxis().SetTitle("x_{B}")
	h1.GetYaxis().SetTitle("Q^{2} (GeV/c)^{2}")
	h1.GetZaxis().SetTitle("-t_{col} (GeV^{2})")
	ROOT.gPad.SetRightMargin(0.18)
	h1.GetZaxis().SetTitleOffset(1)
	h1.Draw("colz")

	c1.cd(2)
	h2.SetTitle("-t_{min} distribution over (x_{B}, Q^{2})")
	h2.GetXaxis().SetTitle("x_{B}")
	h2.GetYaxis().SetTitle("Q^{2} (GeV/c)^{2}")
	h2.GetZaxis().SetTitle("-t_{min} (GeV^{2})")
	ROOT.gPad.SetRightMargin(0.18)
	h2.GetZaxis().SetTitleOffset(1.2)
	h2.Draw("colz")

	c1.Print("tcoltmin.pdf")

def draw_binning(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',1800,600)
	c1.Divide(3,1)

	h1 = ff1.Get("root_dvcs_binning_h_Q2_xB")
	h1.Add(ff2.Get("root_dvcs_binning_h_Q2_xB"))
	h2 = ff1.Get("root_dvcs_binning_h_t_xB")
	h2.Add(ff2.Get("root_dvcs_binning_h_t_xB"))
	h3 = ff1.Get("root_dvcs_binning_h_t_trento")
	h3.Add(ff2.Get("root_dvcs_binning_h_t_trento"))

	xB_edges = [0.16, 0.26]
	Q2_edges = [[1.75], [2.4], [3.25]]
	t_edges = [[0.15, 0.25, 0.45], [0.22, 0.4, 0.80], [0.40, 0.70, 1.15]]
	xBQ2line_xB = [ROOT.TLine(0.16, 0, 0.16, 4), ROOT.TLine(0.26, 0.5, 0.26, 8)]
	xBQ2line_Q2 = [ROOT.TLine(0.05, 1.75, 0.16, 1.75), ROOT.TLine(0.16, 2.4, 0.26, 2.4), ROOT.TLine(0.26, 3.25, 0.75, 3.25)]
	xBtline_xB = [ROOT.TLine(0.16, 0, 0.16, 1.5), ROOT.TLine(0.26, 0, 0.26, 1.5)]
	xBtline_t = [ROOT.TLine(0.05, 0.15, 0.16, 0.15), ROOT.TLine(0.16, 0.22, 0.26, 0.22), ROOT.TLine(0.26, 0.4, 0.75, 0.4), 
				ROOT.TLine(0.05, 0.25, 0.16, 0.25), ROOT.TLine(0.16, 0.4, 0.26, 0.4), ROOT.TLine(0.26, 0.7, 0.75, 0.7),
				ROOT.TLine(0.05, 0.45, 0.16, 0.45), ROOT.TLine(0.16, 0.8, 0.26, 0.8), ROOT.TLine(0.26, 1.15, 0.75, 1.15)]

	xBtbintext = [ROOT.TText(0.1,0.05,"1"),ROOT.TText(0.2,0.1,"2"),ROOT.TText(0.4,0.2,"3")
	,ROOT.TText(0.1,0.15,"4"),ROOT.TText(0.2,0.25,"5"),ROOT.TText(0.4,0.55,"6"),
	ROOT.TText(0.1,0.35,"7"),ROOT.TText(0.2,0.6,"8"),ROOT.TText(0.4,1,"9"),
	ROOT.TText(0.1,1,"10"),ROOT.TText(0.2,1.2,"11"),ROOT.TText(0.4,1.3,"12")]

	c1.cd(2)
	h1.SetTitle("")
	h1.GetXaxis().SetTitle("x_{B}")
	h1.GetYaxis().SetTitle("Q^{2} [(GeV/c)^{2}]")
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetLabelSize(0.04)
	h1.GetXaxis().SetRangeUser(0, 0.8)
	h1.GetYaxis().SetRangeUser(0, 12)
	ROOT.gPad.SetLeftMargin(0.15)
	ROOT.gPad.SetRightMargin(0.18)
	ROOT.gPad.SetBottomMargin(0.12)
	ROOT.gPad.SetLogz()
	h1.Draw("colz")
	for line in xBQ2line_Q2:
		line.Draw("SAME")
	for line in xBQ2line_xB:
		line.Draw("SAME")

	c1.cd(1)
	h2.SetTitle("")
	h2.GetXaxis().SetTitle("x_{B}")
	h2.GetYaxis().SetTitle("-t  [GeV^{2}]")
	h2.GetYaxis().SetRangeUser(0, 1.5)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.04)
	h2.GetYaxis().SetTitleSize(0.05)
	h2.GetYaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLeftMargin(0.15)
	ROOT.gPad.SetRightMargin(0.18)
	ROOT.gPad.SetBottomMargin(0.12)
	ROOT.gPad.SetLogz()
	h2.Draw("colz")
	for line in xBtline_t:
		line.Draw("SAME")
	for line in xBtline_xB:
		line.Draw("SAME")
	for text in xBtbintext:
		text.SetTextAlign(21)
		text.Draw("SAME")

	c1.cd(3)
	h3.SetTitle("")
	h3.GetYaxis().SetTitle("-t  [GeV^{2}]")
	h3.GetXaxis().SetTitle("#phi  [#circ]")
	h3.GetYaxis().SetRangeUser(0, 4)
	h3.GetXaxis().SetTitleSize(0.05)
	h3.GetXaxis().SetLabelSize(0.04)
	h3.GetYaxis().SetTitleSize(0.05)
	h3.GetYaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLeftMargin(0.15)
	ROOT.gPad.SetRightMargin(0.18)
	ROOT.gPad.SetBottomMargin(0.12)
	ROOT.gPad.SetLogz()
	h3.Draw("colz")

	c1.Print("binning.pdf")

def draw_logBinning(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',1600,600)
	c1.Divide(2,1)

	h1 = ff1.Get("root_dvcs_binning_h_Q2_xB_logarithmic")
	h1.Add(ff2.Get("root_dvcs_binning_h_Q2_xB_logarithmic"))
	h2 = ff1.Get("root_dvcs_binning_h_t_trento_logarithmic")
	h2.Add(ff2.Get("root_dvcs_binning_h_t_trento_logarithmic"))

	c1.cd(1)
	h1.SetTitle("x_{B}, Q^{2} binning")
	h1.GetXaxis().SetTitle("log_{10}(x_{B})")
	h1.GetYaxis().SetTitle("log_{10}(Q^{2}/1 (GeV/c)^{2})")
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLeftMargin(0.15)
	ROOT.gPad.SetRightMargin(0.18)
	ROOT.gPad.SetBottomMargin(0.12)
	ROOT.gPad.SetLogz()
	h1.Draw("colz")

	c1.cd(2)
	h2.SetTitle("-t, #phi binning")
	h2.GetXaxis().SetTitle("#phi (#circ)")
	h2.GetYaxis().SetTitle("log_{10}(-t /1 GeV^{2})")
	h2.GetYaxis().SetRangeUser(-2, 0.6)
	h2.GetXaxis().SetTitleSize(0.05)
	h2.GetXaxis().SetLabelSize(0.04)
	h2.GetYaxis().SetTitleSize(0.05)
	h2.GetYaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLeftMargin(0.15)
	ROOT.gPad.SetRightMargin(0.18)
	ROOT.gPad.SetBottomMargin(0.12)
	ROOT.gPad.SetLogz()
	h2.Draw("colz")

	c1.Print("logBinning.pdf")

def draw_kinCorrGamma(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',800,600)

	h1 = ff1.Get("root_excl_cuts_all_h_me_gam_energy")
	h1.Add(ff2.Get("root_excl_cuts_all_h_me_gam_energy"))

	c1.cd(1)
	h1.SetTitle("ME_{ep#gamma} vs. E_{#gamma} (MC, recon. from dvcsgen)")
	h1.GetYaxis().SetTitle("ME_{ep#gamma} (GeV)")
	h1.GetXaxis().SetTitle("E_{#gamma} (GeV)")
	h1.GetXaxis().SetRangeUser(3, 10)
	h1.GetYaxis().SetRangeUser(-1, 1.5)
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetLabelSize(0.04)
	ROOT.gPad.SetLeftMargin(0.15)
	ROOT.gPad.SetRightMargin(0.18)
	ROOT.gPad.SetBottomMargin(0.12)
	ROOT.gPad.SetLogz()
	h1.Draw("colz")

	c1.Print("MEgamE.pdf")

# def draw_rawYields(ff1,ff2):

# 	xB_array = [0, 0.1, 0.15, 0.2, 0.3, 0.4, 1]
# 	Q2_array = [1, 1.7, 2.22, 2.7, 3.5, 11]
# 	t_array = [0, 0.09, 0.13, 0.18, 0.23, 0.3, 0.39, 0.52, 0.72, 1.1, 2]

# 	xBQ2bin = [[1,2,4,7,7, None], [3,3,5,8,12, 16], [None, 3, 6, 9, 13, 16], [None, None, 6, 10, 14, 16], [None, None, None, 11, 15, 17]]	

# 	Integral = 0 

# 	hall = {}
# 	hdummy = ROOT.TH1F("","",24,0,360)

# 	for Q2bin in range(0,5):
# 		for xBbin in range(0,6):
# 			for tbin in range(0,10):

# 				if (xBQ2bin[Q2bin][xBbin] is None):
# 					continue

# 				hist = []
# 				h1 = 0

# 				if (ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist.append(ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist.append(ff1.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist.append(ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist.append(ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist.append(ff2.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist.append(ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (hist):
# 					h1 = hist[0]
# 					if (len(hist)>1):
# 						for hi in hist[1:]:
# 							h1.Add(hi)
# 				else:
# 					continue
# 				if ((xBQ2bin[Q2bin][xBbin], tbin) not in hall):
# 					hall[xBQ2bin[Q2bin][xBbin], tbin] = h1
# 				else:
# 					hall[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)

# 	for ind_xBQ2 in range(1,18):
# 		c1 = ROOT.TCanvas('c'+str(ind_xBQ2),'c'+str(ind_xBQ2),1024,592)
# 		c1.Divide(4,3)
# 		for tbin in range(0,10):
# 			c1.cd(tbin+1)
# 			if ((not (ind_xBQ2, tbin) in hall)):
# 				# hdummy.Draw()
# 				c1.Update()
# 			else:
# 				hall[ind_xBQ2, tbin].SetTitle("Raw Yields, xBQ2 "+str(ind_xBQ2)+" t "+str(tbin))
# 				Integral = Integral + hall[ind_xBQ2, tbin].Integral()
# 				hall[ind_xBQ2, tbin].GetXaxis().SetTitle("#phi (#circ)")
# 				hall[ind_xBQ2, tbin].GetXaxis().SetTitleSize(0.05)
# 				hall[ind_xBQ2, tbin].GetYaxis().SetTitleSize(0.05)
# 				hall[ind_xBQ2, tbin].GetXaxis().SetLabelSize(0.04)
# 				hall[ind_xBQ2, tbin].GetYaxis().SetLabelSize(0.04)
# 				hall[ind_xBQ2, tbin].Draw()
# 				c1.Update()
# 		c1.Print("rawyields_xBQ2_"+str(ind_xBQ2)+".pdf")
# 	print("total events: "+str(Integral))

# def draw_BSA(ff1, ff2):

# 	xB_array = [0, 0.1, 0.15, 0.2, 0.3, 0.4, 1]
# 	Q2_array = [1, 1.7, 2.22, 2.7, 3.5, 11]
# 	t_array = [0, 0.09, 0.13, 0.18, 0.23, 0.3, 0.39, 0.52, 0.72, 1.1, 2]

# 	xBQ2bin = [[1,2,4,7,7, None], [3,3,5,8,12, 16], [None, 3, 6, 9, 13, 16], [None, None, 6, 10, 14, 16], [None, None, None, 11, 15, 17]]	
# 	hplus = {}
# 	hminus = {}
# 	BSA = {}
# 	grtl = {}

# 	entries = {}
# 	xB_sum = {}
# 	Q2_sum = {}
# 	t_sum = {}

# 	data = {}
# 	Integral = 0 
# 	for Q2bin in range(0,5):
# 		for xBbin in range(0,6):
# 			for tbin in range(0,10):

# 				if (xBQ2bin[Q2bin][xBbin] is None):
# 					continue

# 				h1 = ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))
# 				h2 = ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))
# 				h3 = ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))
# 				h4 = ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))

# 				if (h1 and h3):
# 					h1.Add(h3)
# 				elif (not h1 and h3):
# 					h1 = h3
# 				elif (not h1 and not h3):
# 					continue
# 				if (h2 and h4):
# 					h2.Add(h4)
# 				elif (not h2 and h4):
# 					h2 = h4
# 				elif (not h2 and not h4):
# 					continue

# 				h1.Rebin()
# 				h2.Rebin()

# 				Integral = Integral + h1.Integral() + h2.Integral()
# 				if ((xBQ2bin[Q2bin][xBbin], tbin) in hplus):
# 					hplus[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)
# 				else: 
# 					hplus[xBQ2bin[Q2bin][xBbin], tbin] = h1
# 				if ((xBQ2bin[Q2bin][xBbin], tbin) in hminus):
# 					hminus[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)
# 				else: 
# 					hminus[xBQ2bin[Q2bin][xBbin], tbin] = h2

# 	for ind_xBQ2 in range(1,18):
# 		for tbin in range(0,10):
# 			if ((not (ind_xBQ2, tbin) in hplus) or (not (ind_xBQ2, tbin) in hminus)):
# 				continue
# 			bsatitle = "BSA xBQ2 "+str(ind_xBQ2)+" t "+str(tbin)	
# 			BSA_hist = ROOT.TH1F(bsatitle, bsatitle, 12, 0, 360)
# 			for binx in range(0,12):
# 				nplus = hplus[ind_xBQ2,tbin].GetBinContent(binx)
# 				nminus = hminus[ind_xBQ2,tbin].GetBinContent(binx)
# 				ntotal = nplus + nminus
# 				ndiff = nplus - nminus
# 				if (nplus < 3 or nminus < 3):
# 					continue
# 				BSA_hist.SetBinContent(binx, 1/0.8*ndiff/ntotal)
# 				BSA_hist.SetBinError(binx, 1/0.8*np.sqrt(4*nplus*nminus/(nplus+nminus)**3))
# 			Fitf = ROOT.TF1("fitf_xBQ2_"+str(ind_xBQ2)+"_t_"+str(tbin), "[alpha]*sin(TMath::DegToRad()*x)/(1+[beta]*cos(TMath::DegToRad()*x))",0.,360.)
# 			data[ind_xBQ2, tbin] = [BSA_hist, Fitf]
# 			BSA_hist.Fit(Fitf.GetName())
# 			BSA_hist.Draw()

# 	for ind_xBQ2 in range(1,18):
# 		c1 = ROOT.TCanvas("c1_xBQ2_"+str(ind_xBQ2),"c1_xBQ2_"+str(ind_xBQ2),1024,592)
# 		c1.Divide(4,3)
# 		t_array2 = array('f', [])
# 		e_t_array = array('f', [])
# 		alpha_array = array('f', [])
# 		e_alpha_array = array('f', [])
# 		for tbin in range(0,10):
# 			c1.cd(tbin+1)
# 			ROOT.gPad.SetLeftMargin(0.16)
# 			if (not (ind_xBQ2, tbin) in data):
# 				continue
# 			data[ind_xBQ2, tbin][0].Fit(data[ind_xBQ2, tbin][1].GetName())
# 			data[ind_xBQ2, tbin][0].GetYaxis().SetTitle("BSA")
# 			data[ind_xBQ2, tbin][0].GetXaxis().SetTitle("#phi (#circ)")
# 			data[ind_xBQ2, tbin][0].GetXaxis().SetTitleSize(0.05)
# 			data[ind_xBQ2, tbin][0].GetYaxis().SetTitleSize(0.05)
# 			data[ind_xBQ2, tbin][0].GetXaxis().SetLabelSize(0.04)
# 			data[ind_xBQ2, tbin][0].GetYaxis().SetLabelSize(0.04)
# 			data[ind_xBQ2, tbin][0].Draw()

# 			if (data[ind_xBQ2, tbin][1].GetParError(0) < 0.1):
# 				t_array2.append(t_array[tbin]*0.5 + t_array[tbin+1]*0.5 + (9-ind_xBQ2)*0.005)
# 				alpha_array.append(data[ind_xBQ2, tbin][1].GetParameter(0))
# 				e_t_array.append(0)
# 				e_alpha_array.append(data[ind_xBQ2, tbin][1].GetParError(0))
# 			c1.Update()

# 		c1.cd(11)
# 		ROOT.gPad.SetLeftMargin(0.16)
# 		c1.cd(12)
# 		ROOT.gPad.SetLeftMargin(0.16)		
# 		gr = ROOT.TGraphErrors( len(t_array2), t_array2, alpha_array, e_t_array, e_alpha_array)
# 		gr.SetTitle( '#alpha vs. -t at xBQ2_'+str(ind_xBQ2) )
# 		gr.SetMarkerColor( 4 )
# 		gr.SetMarkerStyle( 21 )
# 		gr.SetMarkerSize( 0.25* gr.GetMarkerSize() )
# 		grtl[ind_xBQ2] = gr
# 		gr.GetYaxis().SetTitle("#alpha")
# 		gr.GetXaxis().SetTitle("-t (GeV^{2})")
# 		gr.GetXaxis().SetTitleSize(0.05)
# 		gr.GetYaxis().SetTitleSize(0.05)
# 		gr.GetXaxis().SetLabelSize(0.04)
# 		gr.GetYaxis().SetLabelSize(0.04)
# 		gr.Draw( 'ALP' )

# 		c1.Print("bsa_xBQ2_"+str(ind_xBQ2)+".pdf")

# 	c2 = ROOT.TCanvas("c2","c2",640,480)
# 	mg = ROOT.TMultiGraph("alpha vs. -t", "alpha vs. -t")
# 	mg.SetTitle("#alpha vs. -t (x_{B} = 0.09); -t (GeV^{2}); #alpha");
# 	grtl[1].SetMarkerColor( ROOT.kBlack )
# 	grtl[1].SetLineColor( ROOT.kBlack )
# 	mg.Add(grtl[1])
# 	mg.SetMinimum(-0.2)
# 	mg.SetMaximum(0.5)
# 	mg.Draw("AP")
# 	legend = ROOT.TLegend(.65, .77, 0.95, .83)
# 	legend.AddEntry(grtl[1], "1, x_{B} 0.09, Q^{2} 1.17")
# 	legend.Draw()
# 	c2.Print("alpha_1.pdf")

# 	c2.cd()
# 	mg = ROOT.TMultiGraph("alpha vs. -t", "alpha vs. -t")
# 	mg.SetTitle("#alpha vs. -t (x_{B} = 0.13); -t (GeV^{2}); #alpha");
# 	grtl[2].SetMarkerColor( ROOT.kRed )
# 	grtl[2].SetLineColor( ROOT.kRed )
# 	grtl[3].SetMarkerColor( ROOT.kBlack )
# 	grtl[3].SetLineColor( ROOT.kBlack )
# 	mg.Add(grtl[3])
# 	mg.Add(grtl[2])
# 	mg.SetMinimum(-0.2)
# 	mg.SetMaximum(0.5)
# 	mg.Draw("AP")
# 	legend = ROOT.TLegend(.65, .74, 0.95, .86)
# 	legend.AddEntry(grtl[3], "3, x_{B} 0.13, Q^{2} 1.91")
# 	legend.AddEntry(grtl[2], "2, x_{B} 0.12, Q^{2} 1.34")
# 	legend.Draw()
# 	c2.Print("alpha_23.pdf")

# 	c2.cd()
# 	mg = ROOT.TMultiGraph("alpha vs. -t", "alpha vs. -t")
# 	mg.SetTitle("#alpha vs. -t (x_{B} = 0.17); -t (GeV^{2}); #alpha");
# 	grtl[4].SetMarkerColor( ROOT.kBlue )
# 	grtl[4].SetLineColor( ROOT.kBlue )
# 	grtl[5].SetMarkerColor( ROOT.kRed )
# 	grtl[5].SetLineColor( ROOT.kRed )
# 	grtl[6].SetMarkerColor( ROOT.kBlack )
# 	grtl[6].SetLineColor( ROOT.kBlack )
# 	mg.Add(grtl[6])
# 	mg.Add(grtl[5])
# 	mg.Add(grtl[4])
# 	mg.SetMinimum(-0.2)
# 	mg.SetMaximum(0.5)
# 	mg.Draw("AP")
# 	legend = ROOT.TLegend(.65, .71, 0.95, .89)
# 	legend.AddEntry(grtl[6], "6, x_{B} 0.18, Q^{2} 2.50")
# 	legend.AddEntry(grtl[5], "5, x_{B} 0.17, Q^{2} 1.93")
# 	legend.AddEntry(grtl[4], "4, x_{B} 0.17, Q^{2} 1.35")
# 	legend.Draw()
# 	c2.Print("alpha_456.pdf")

# 	c2.cd()
# 	mg = ROOT.TMultiGraph("alpha vs. -t", "alpha vs. -t")
# 	mg.SetTitle("#alpha vs. -t (x_{B} = 0.24); -t (GeV^{2}); #alpha");
# 	grtl[7].SetMarkerColor( ROOT.kViolet )
# 	grtl[7].SetLineColor( ROOT.kViolet )
# 	grtl[8].SetMarkerColor( ROOT.kGreen + 4 )
# 	grtl[8].SetLineColor( ROOT.kGreen + 4 )
# 	grtl[9].SetMarkerColor( ROOT.kBlue )
# 	grtl[9].SetLineColor( ROOT.kBlue )
# 	grtl[10].SetMarkerColor( ROOT.kRed )
# 	grtl[10].SetLineColor( ROOT.kRed )
# 	grtl[11].SetMarkerColor( ROOT.kBlack )
# 	grtl[11].SetLineColor( ROOT.kBlack )
# 	mg.Add(grtl[11])
# 	mg.Add(grtl[10])
# 	mg.Add(grtl[9])
# 	mg.Add(grtl[8])
# 	mg.Add(grtl[7])
# 	mg.SetMinimum(-0.2)
# 	mg.SetMaximum(0.5)
# 	mg.Draw("AP")
# 	legend = ROOT.TLegend(.65, .65, 0.95, .95)
# 	legend.AddEntry(grtl[11], "11, x_{B} 0.26, Q^{2} 3.87")
# 	legend.AddEntry(grtl[10], "10, x_{B} 0.24, Q^{2} 3.1")
# 	legend.AddEntry(grtl[9], "9, x_{B} 0.24, Q^{2} 2.45")
# 	legend.AddEntry(grtl[8], "8, x_{B} 0.24, Q^{2} 1.93")
# 	legend.AddEntry(grtl[7], "7, x_{B} 0.22, Q^{2} 1.49")
# 	legend.Draw()
# 	c2.Print("alpha_7891011.pdf")

# 	c2.cd()
# 	mg = ROOT.TMultiGraph("alpha vs. -t", "alpha vs. -t")
# 	mg.SetTitle("#alpha vs. -t (x_{B} = 0.034); -t (GeV^{2}); #alpha");
# 	grtl[12].SetMarkerColor( ROOT.kGreen + 4 )
# 	grtl[12].SetLineColor( ROOT.kGreen + 4 )
# 	grtl[13].SetMarkerColor( ROOT.kBlue )
# 	grtl[13].SetLineColor( ROOT.kBlue )
# 	grtl[14].SetMarkerColor( ROOT.kRed )
# 	grtl[14].SetLineColor( ROOT.kRed )
# 	grtl[15].SetMarkerColor( ROOT.kBlack )
# 	grtl[15].SetLineColor( ROOT.kBlack )
# 	mg.Add(grtl[15])
# 	mg.Add(grtl[14])
# 	mg.Add(grtl[13])
# 	mg.Add(grtl[12])
# 	mg.SetMinimum(-0.2)
# 	mg.SetMaximum(0.5)
# 	mg.Draw("AP")
# 	legend = ROOT.TLegend(.65, .68, 0.95, .92)
# 	legend.AddEntry(grtl[15], "15, x_{B} 0.35, Q^{2} 4.36")
# 	legend.AddEntry(grtl[14], "14, x_{B} 0.35, Q^{2} 3.1")
# 	legend.AddEntry(grtl[13], "13, x_{B} 0.34, Q^{2} 2.49")
# 	legend.AddEntry(grtl[12], "12, x_{B} 0.32, Q^{2} 2.01")
# 	legend.Draw()
# 	c2.Print("alpha_12131415.pdf")


# 	c2.cd()
# 	mg = ROOT.TMultiGraph("alpha vs. -t", "alpha vs. -t")
# 	mg.SetTitle("#alpha vs. -t (x_{B} = 0.047); -t (GeV^{2}); #alpha");
# 	grtl[17].SetMarkerColor( ROOT.kBlack )
# 	grtl[17].SetLineColor( ROOT.kBlack )
# 	grtl[16].SetMarkerColor( ROOT.kRed )
# 	grtl[16].SetLineColor( ROOT.kRed )
# 	mg.Add(grtl[17])
# 	mg.Add(grtl[16])
# 	mg.SetMinimum(-0.2)
# 	mg.SetMaximum(0.5)
# 	mg.Draw("AP")
# 	legend = ROOT.TLegend(.65, .74, 0.95, .86)
# 	legend.AddEntry(grtl[17], "17, x_{B} 0.44, Q^{2} 3.08")
# 	legend.AddEntry(grtl[16], "16, x_{B} 0.50, Q^{2} 5.22")
# 	legend.Draw()
# 	c2.Print("alpha_1617.pdf")

# 	print("Integral: " + str(Integral))

# def draw_pi0subtraction(ff1,ff2,ff3,ff4):

# 	xB_array = [0, 0.1, 0.15, 0.2, 0.3, 0.4, 1]
# 	Q2_array = [1, 1.7, 2.22, 2.7, 3.5, 11]
# 	t_array = [0, 0.09, 0.13, 0.18, 0.23, 0.3, 0.39, 0.52, 0.72, 1.1, 2]

# 	xBQ2bin = [[1,2,4,7,7, None], [3,3,5,8,12, 16], [None, 3, 6, 9, 13, 16], [None, None, 6, 10, 14, 16], [None, None, None, 11, 15, 17]]	

# 	Integral = 0 

# 	hdata1g = {}
# 	hdata2g = {}
# 	hMC1g = {}
# 	hMC2g = {}

# 	for Q2bin in range(0,5):
# 		for xBbin in range(0,6):
# 			for tbin in range(0,10):

# 				if (xBQ2bin[Q2bin][xBbin] is None):
# 					continue

# 				hist1 = []
# 				hist2 = []
# 				hist3 = []
# 				h1 = 0

# 				if (ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff1.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff2.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

# 				if (ff1.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff1.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff1.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff1.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff2.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff2.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff2.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

# 				if (ff1.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

# 				if (hist1):
# 					h1 = hist1[0]
# 					if (len(hist1)>1):
# 						for hi in hist1[1:]:
# 							h1.Add(hi)
# 				else:
# 					continue

# 				if (hist2):
# 					for h2 in hist2:
# 						h1.Add(h2, -1)

# 				if (hist3):
# 					for h3 in hist3:
# 						h1.Add(h3, -1)

# 				if ((xBQ2bin[Q2bin][xBbin], tbin) not in hdata1g):
# 					hdata1g[xBQ2bin[Q2bin][xBbin], tbin] = h1
# 				else:
# 					hdata1g[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)

# 	for Q2bin in range(0,5):
# 		for xBbin in range(0,6):
# 			for tbin in range(0,10):

# 				if (xBQ2bin[Q2bin][xBbin] is None):
# 					continue

# 				hist2 = []
# 				hist3 = []
# 				h1 = 0

# 				if (ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff1.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff2.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

# 				if (ff1.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff1.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff1.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff1.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff2.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff2.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff2.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

# 				if (ff1.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff1.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff2.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

# 				if (hist2):
# 					h1 = hist2[0]
# 					if (len(hist2)>1):
# 						for hi in hist2[1:]:
# 							h1.Add(hi)
# 					if (hist3):
# 						for h3 in hist3:
# 							h1.Add(h3)

# 				elif (hist3):
# 					h1 = hist3[0]
# 					if (len(hist3)>1):
# 						for hi in hist3[1:]:
# 							h1.Add(hi)
# 				else:
# 					continue

# 				if ((xBQ2bin[Q2bin][xBbin], tbin) not in hdata2g):
# 					hdata2g[xBQ2bin[Q2bin][xBbin], tbin] = h1
# 				else:
# 					hdata2g[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)




# 	for Q2bin in range(0,5):
# 		for xBbin in range(0,6):
# 			for tbin in range(0,10):

# 				if (xBQ2bin[Q2bin][xBbin] is None):
# 					continue

# 				hist1 = []
# 				hist2 = []
# 				hist3 = []
# 				h1 = 0

# 				if (ff3.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff3.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff3.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff3.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff3.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff3.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff4.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff4.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist1.append(ff4.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

# 				if (ff3.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff3.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff3.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff3.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff3.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff3.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff4.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff4.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff4.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

# 				if (ff3.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff3.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff3.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

# 				if (hist1):
# 					h1 = hist1[0]
# 					if (len(hist1)>1):
# 						for hi in hist1[1:]:
# 							h1.Add(hi)
# 				else:
# 					continue

# 				if (hist2):
# 					for h2 in hist2:
# 						h1.Add(h2, -1)

# 				if (hist3):
# 					for h3 in hist3:
# 						h1.Add(h3, -1)

# 				if ((xBQ2bin[Q2bin][xBbin], tbin) not in hMC1g):
# 					hMC1g[xBQ2bin[Q2bin][xBbin], tbin] = h1
# 				else:
# 					hMC1g[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)

# 	for Q2bin in range(0,5):
# 		for xBbin in range(0,6):
# 			for tbin in range(0,10):

# 				if (xBQ2bin[Q2bin][xBbin] is None):
# 					continue

# 				hist2 = []
# 				hist3 = []
# 				h1 = 0

# 				if (ff3.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff3.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff3.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff3.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff3.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff3.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff4.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff4.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist2.append(ff4.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

# 				if (ff3.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff3.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff3.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
# 				if (ff4.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
# 					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

# 				if (hist2):
# 					h1 = hist2[0]
# 					if (len(hist2)>1):
# 						for hi in hist2[1:]:
# 							h1.Add(hi)
# 					if (hist3):
# 						for h3 in hist3:
# 							h1.Add(h3)

# 				elif (hist3):
# 					h1 = hist3[0]
# 					if (len(hist3)>1):
# 						for hi in hist3[1:]:
# 							h1.Add(hi)
# 				else:
# 					continue

# 				if ((xBQ2bin[Q2bin][xBbin], tbin) not in hMC2g):
# 					hMC2g[xBQ2bin[Q2bin][xBbin], tbin] = h1
# 				else:
# 					hMC2g[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)


# 	for ind_xBQ2 in range(1,18):
# 		c1 = ROOT.TCanvas('c'+str(ind_xBQ2),'c'+str(ind_xBQ2),1024,592)
# 		c1.Divide(4,3)
# 		for tbin in range(0,10):
# 			c1.cd(tbin+1)
# 			if ((not (ind_xBQ2, tbin) in hMC1g) or (not (ind_xBQ2, tbin) in hMC2g) or (not (ind_xBQ2, tbin) in hdata1g) or (not (ind_xBQ2, tbin) in hdata2g)   ):
# 				print(ind_xBQ2, tbin)
# 				print((ind_xBQ2, tbin) in hMC1g) 
# 				print((ind_xBQ2, tbin) in hMC2g) 
# 				print((ind_xBQ2, tbin) in hdata1g) 
# 				print((ind_xBQ2, tbin) in hdata2g)
# 				# hdummy.Draw()
# 				if ((ind_xBQ2, tbin) in hdata1g):
# 					hdata1g[ind_xBQ2, tbin].SetTitle("Raw Yields, xBQ2 "+str(ind_xBQ2)+" t "+str(tbin))
# 					Integral = Integral + hdata1g[ind_xBQ2, tbin].Integral()
# 					hdata1g[ind_xBQ2, tbin].GetXaxis().SetTitle("#phi (#circ)")
# 					hdata1g[ind_xBQ2, tbin].GetXaxis().SetTitleSize(0.05)
# 					hdata1g[ind_xBQ2, tbin].GetYaxis().SetTitleSize(0.05)
# 					hdata1g[ind_xBQ2, tbin].GetXaxis().SetLabelSize(0.04)
# 					hdata1g[ind_xBQ2, tbin].GetYaxis().SetLabelSize(0.04)
# 					hdata1g[ind_xBQ2, tbin].Draw()

# 				c1.Update()
# 			else:
# 				for binx in range(0,24):
# 					data1g = hdata1g[ind_xBQ2, tbin].GetBinContent(binx)
# 					data2g = hdata2g[ind_xBQ2, tbin].GetBinContent(binx)
# 					MC1g   = hMC1g[ind_xBQ2, tbin].GetBinContent(binx)
# 					MC2g   = hMC2g[ind_xBQ2, tbin].GetBinContent(binx)
# 					if (MC2g):
# 						estimate = data1g - data2g * MC1g/MC2g
# 						# hdata1g[ind_xBQ2, tbin].SetBinContent(binx,estimate)
# 						hdata2g[ind_xBQ2, tbin].SetBinContent(binx,data2g * MC1g/MC2g)
# 					else:
# 						hdata2g[ind_xBQ2, tbin].SetBinContent(binx,0)
# 				hdata1g[ind_xBQ2, tbin].SetTitle("Raw Yields, xBQ2 "+str(ind_xBQ2)+" t "+str(tbin))
# 				Integral = Integral + hdata1g[ind_xBQ2, tbin].Integral()
# 				hdata1g[ind_xBQ2, tbin].GetXaxis().SetTitle("#phi (#circ)")
# 				hdata1g[ind_xBQ2, tbin].GetXaxis().SetTitleSize(0.05)
# 				hdata1g[ind_xBQ2, tbin].GetYaxis().SetTitleSize(0.05)
# 				hdata1g[ind_xBQ2, tbin].GetXaxis().SetLabelSize(0.04)
# 				hdata1g[ind_xBQ2, tbin].GetYaxis().SetLabelSize(0.04)
# 				hdata1g[ind_xBQ2, tbin].Draw()
# 				hdata2g[ind_xBQ2, tbin].SetLineColor(ROOT.kRed)
# 				hdata2g[ind_xBQ2, tbin].Draw("SAME")
# 				c1.Update()
# 		c1.Print("rawyields_subtracted_xBQ2_"+str(ind_xBQ2)+".pdf")
# 	print("total events: "+str(Integral))


def draw_rawYields(ff1,ff2):

	Integral_inb = 0 
	Integral_outb = 0

	h_inb = {}
	h_outb = {}
	h_all = {}
	hdummy = ROOT.TH1F("","",24,0,360)

	placements = [0,1,2,3,7,8,9,13,14,15,19,20,21,4,5,6,10,11,12,16,17,18,22,23,24]
	placements_2 = [0,10,11,12,7,8,9,4,5,6,1,2,3]

	for xBQ2tbin in range(1,25):
		hist_inb = []
		hist_outb = []
		pi0_inb = []
		pi0_outb = []

		for heli in [-1, 0, 1]:
			if (ff1.Get("root_dvcs_heli_"+str(heli)+"_h_trento_xBQ2t_"+str(xBQ2tbin))):
				hist_inb.append(deepcopy(ff1.Get("root_dvcs_heli_"+str(heli)+"_h_trento_xBQ2t_"+str(xBQ2tbin))))
			if (ff2.Get("root_dvcs_heli_"+str(heli)+"_h_trento_xBQ2t_"+str(xBQ2tbin))):
				hist_outb.append(deepcopy(ff2.Get("root_dvcs_heli_"+str(heli)+"_h_trento_xBQ2t_"+str(xBQ2tbin))))

		h1 = hist_inb[0]
		if (len(hist_inb)>1):
			for hi in hist_inb[1:]:
				h1.Add(hi)
		h2 = hist_outb[0]
		if (len(hist_outb)>1):
			for ho in hist_outb[1:]:
				h2.Add(ho)
		
		h_inb[xBQ2tbin] = h1
		h_outb[xBQ2tbin] = h2
		h_all[xBQ2tbin] = deepcopy(h1)
		h_all[xBQ2tbin].Add(deepcopy(h2))

	# c1 = ROOT.TCanvas('c1','c1',600,600)
	# c2 = ROOT.TCanvas('c2','c2',1200,600)
	# c3 = ROOT.TCanvas('c3','c3',1200,600)
	c3 = ROOT.TCanvas('c3','c3',800,600)
	# c1.Divide(6,4)
	# c2.Divide(6,4)
	# c3.Divide(3,4,0,0)

	for xBQ2tbin in range(20,21):
		# c1.cd(placements[xBQ2tbin])
		# ROOT.gPad.SetLogy()
		# h_inb[xBQ2tbin].SetTitle("Raw Yields, inb, bin "+str(xBQ2tbin)+", entries: "+str(int(h_inb[xBQ2tbin].Integral())))
		Integral_inb = Integral_inb + h_inb[xBQ2tbin].Integral()
		# h_inb[xBQ2tbin].GetXaxis().SetTitle("#phi (#circ)")
		# h_inb[xBQ2tbin].GetXaxis().SetTitleSize(0.05)
		# h_inb[xBQ2tbin].GetYaxis().SetTitleSize(0.05)
		# h_inb[xBQ2tbin].GetXaxis().SetLabelSize(0.04)
		# h_inb[xBQ2tbin].GetYaxis().SetLabelSize(0.04)
		# h_inb[xBQ2tbin].GetYaxis().SetRangeUser(10,100000)
		# h_inb[xBQ2tbin].Draw()
		# c1.Update()
		# c2.cd(placements[xBQ2tbin])
		# ROOT.gPad.SetLogy()
		# h_outb[xBQ2tbin].SetTitle("Raw Yields, outb, bin  "+str(xBQ2tbin)+", entries: "+str(int(h_outb[xBQ2tbin].Integral())))
		Integral_outb = Integral_outb + h_outb[xBQ2tbin].Integral()
		# h_outb[xBQ2tbin].GetXaxis().SetTitle("#phi (#circ)")
		# h_outb[xBQ2tbin].GetXaxis().SetTitleSize(0.05)
		# h_outb[xBQ2tbin].GetYaxis().SetTitleSize(0.05)
		# h_outb[xBQ2tbin].GetXaxis().SetLabelSize(0.04)
		# h_outb[xBQ2tbin].GetYaxis().SetLabelSize(0.04)
		# h_outb[xBQ2tbin].GetYaxis().SetRangeUser(9.5,100000)
		# h_outb[xBQ2tbin].Draw()
		# c2.Update()
		c3.cd(placements_2[xBQ2tbin-12])
		ROOT.gPad.SetLogy()
		h_all[xBQ2tbin].GetXaxis().SetNdivisions(-506, ROOT.kTRUE);
		h_all[xBQ2tbin].SetTitle("")
		h_all[xBQ2tbin].GetXaxis().SetTitle("")
		h_all[xBQ2tbin].GetYaxis().SetTitle("")
		h_all[xBQ2tbin].GetXaxis().SetTitleSize(0)
		h_all[xBQ2tbin].GetYaxis().SetTitleSize(0)
		h_all[xBQ2tbin].GetXaxis().SetLabelSize(0)
		h_all[xBQ2tbin].GetYaxis().SetLabelSize(0)
		h_all[xBQ2tbin].GetYaxis().SetRangeUser(99,10000)
		# h_all[xBQ2tbin].GetYaxis().SetRangeUser(9,100000)
		# ROOT.gPad.SetLeftMargin(0)
		h_all[xBQ2tbin].Draw("eHIST")
		c3.Update()
	# c1.Print("rawyields_xBQ2t_inb.pdf")
	# c2.Print("rawyields_xBQ2t_outb.pdf")
	c3.Print("rawyields_xBQ2t_all.pdf")
	print("inbending: "+str(int(Integral_inb)))
	print("outbending: "+str(int(Integral_outb)))
	print("total: "+str(int(Integral_inb+Integral_outb)))
	print(h_inb[20].Integral())
	print(h_outb[20].Integral())
	print(h_inb[20].Integral()+h_outb[20].Integral())

def draw_BSA(ff1, ff2):

	hplus = {}
	hminus = {}
	BSA = {}
	grtl = {}

	entries = {}
	xB_sum = {}
	Q2_sum = {}
	t_sum = {}

	data = {}
	Integral_inb = 0
	Integral_outb = 0

	placements = [0,1,2,3,7,8,9,13,14,15,19,20,21,4,5,6,10,11,12,16,17,18,22,23,24]

	for xBQ2tbin in range(1,25):

		h1 = deepcopy(ff1.Get("root_dvcs_heli_1_h_trento_xBQ2t_"+str(xBQ2tbin)))
		h2 = deepcopy(ff1.Get("root_dvcs_heli_-1_h_trento_xBQ2t_"+str(xBQ2tbin)))

		Integral_inb = Integral_inb + h1.Integral() + h2.Integral()
		hplus["inb_"+str(xBQ2tbin)] = h1
		hminus["inb_"+str(xBQ2tbin)] = h2

		h3 = deepcopy(ff2.Get("root_dvcs_heli_1_h_trento_xBQ2t_"+str(xBQ2tbin)))
		h4 = deepcopy(ff2.Get("root_dvcs_heli_-1_h_trento_xBQ2t_"+str(xBQ2tbin)))

		Integral_outb = Integral_outb + h3.Integral() + h4.Integral()
		hplus["outb_"+str(xBQ2tbin)] = h3
		hminus["outb_"+str(xBQ2tbin)] = h4

	for xBQ2tbin in range(1,25):
			bsatitle_inb = "BSA, inb "+str(xBQ2tbin)+", entries: "+str(int(hplus["inb_"+str(xBQ2tbin)].Integral()+hminus["inb_"+str(xBQ2tbin)].Integral()))
			BSA_hist_inb = ROOT.TH1F(bsatitle_inb, bsatitle_inb, 30, 0, 360)
			bsatitle_outb = "BSA, outb "+str(xBQ2tbin)+", entries: "+str(int(hplus["outb_"+str(xBQ2tbin)].Integral()+hminus["outb_"+str(xBQ2tbin)].Integral()))
			BSA_hist_outb = ROOT.TH1F(bsatitle_outb, bsatitle_outb, 30, 0, 360)
			bsatitle_all = "BSA, all "+str(xBQ2tbin)+", entries: "+str(int(hplus["inb_"+str(xBQ2tbin)].Integral()+hminus["inb_"+str(xBQ2tbin)].Integral()+hplus["outb_"+str(xBQ2tbin)].Integral()+hminus["outb_"+str(xBQ2tbin)].Integral()))
			BSA_hist_all = ROOT.TH1F(bsatitle_all, bsatitle_all, 30, 0, 360)
			# hplus["inb_"+str(xBQ2tbin)].Rebin(3)
			# hminus["inb_"+str(xBQ2tbin)].Rebin(3)
			# hplus["outb_"+str(xBQ2tbin)].Rebin(3)
			# hminus["outb_"+str(xBQ2tbin)].Rebin(3)
			for binphi in range(1,31):
				nplus_inb = hplus["inb_"+str(xBQ2tbin)].GetBinContent(binphi)
				nminus_inb = hminus["inb_"+str(xBQ2tbin)].GetBinContent(binphi)
				ntotal_inb = nplus_inb + nminus_inb
				ndiff_inb = nplus_inb - nminus_inb
				BSA_hist_inb.GetYaxis().SetRangeUser(-0.45,0.45)
				BSA_hist_inb.SetBinContent(binphi, 1/0.869*ndiff_inb/ntotal_inb)
				BSA_hist_inb.SetBinError(binphi, 1/0.869*np.sqrt(4*nplus_inb*nminus_inb/(nplus_inb+nminus_inb)**3))
				nplus_outb = hplus["outb_"+str(xBQ2tbin)].GetBinContent(binphi)
				nminus_outb = hminus["outb_"+str(xBQ2tbin)].GetBinContent(binphi)
				ntotal_outb = nplus_outb + nminus_outb
				ndiff_outb = nplus_outb - nminus_outb
				BSA_hist_outb.GetYaxis().SetRangeUser(-0.45,0.45)
				BSA_hist_outb.SetBinContent(binphi, 1/0.869*ndiff_outb/ntotal_outb)
				BSA_hist_outb.SetBinError(binphi, 1/0.869*np.sqrt(4*nplus_outb*nminus_outb/(nplus_outb+nminus_outb)**3))
				nplus_all = hplus["inb_"+str(xBQ2tbin)].GetBinContent(binphi) + hplus["outb_"+str(xBQ2tbin)].GetBinContent(binphi)
				nminus_all = hminus["inb_"+str(xBQ2tbin)].GetBinContent(binphi) + hminus["outb_"+str(xBQ2tbin)].GetBinContent(binphi)
				ntotal_all = nplus_all + nminus_all
				ndiff_all = nplus_all - nminus_all
				BSA_hist_all.GetYaxis().SetRangeUser(-0.45,0.45)
				BSA_hist_all.SetBinContent(binphi, 1/0.869*ndiff_all/ntotal_all)
				BSA_hist_all.SetBinError(binphi, 1/0.869*np.sqrt(4*nplus_all*nminus_all/(nplus_all+nminus_all)**3))
			Fitf_inb = ROOT.TF1("fitf_inb_xBQ2t_"+str(xBQ2tbin), "[alpha]*sin(TMath::DegToRad()*x)/(1+[beta]*cos(TMath::DegToRad()*x))",0.,360.)
			data["inb_"+str(xBQ2tbin)] = [BSA_hist_inb, Fitf_inb]
			Fitf_outb = ROOT.TF1("fitf_outb_xBQ2t_"+str(xBQ2tbin), "[alpha]*sin(TMath::DegToRad()*x)/(1+[beta]*cos(TMath::DegToRad()*x))",0.,360.)
			data["outb_"+str(xBQ2tbin)] = [BSA_hist_outb, Fitf_outb]
			Fitf_all = ROOT.TF1("fitf_all_xBQ2t_"+str(xBQ2tbin), "[alpha]*sin(TMath::DegToRad()*x)/(1+[beta]*cos(TMath::DegToRad()*x))",0.,360.)
			data["all_"+str(xBQ2tbin)] = [BSA_hist_all, Fitf_all]

	c1_BSA = ROOT.TCanvas("c1_BSA","c1_BSA",1200,600)
	c1_BSA.Divide(6,4)
	c2_BSA = ROOT.TCanvas("c2_BSA","c2_BSA",1200,600)
	c2_BSA.Divide(6,4)
	c3_BSA = ROOT.TCanvas("c3_BSA","c3_BSA",1200,600)
	c3_BSA.Divide(6,4)
	for xBQ2tbin in range(1,25):
		c1_BSA.cd(placements[xBQ2tbin])
		ROOT.gPad.SetLeftMargin(0.16)
		data["inb_"+str(xBQ2tbin)][0].Fit(data["inb_"+str(xBQ2tbin)][1].GetName())
		data["inb_"+str(xBQ2tbin)][0].GetYaxis().SetTitle("BSA")
		data["inb_"+str(xBQ2tbin)][0].GetXaxis().SetTitle("#phi (#circ)")
		data["inb_"+str(xBQ2tbin)][0].GetXaxis().SetTitleSize(0.05)
		data["inb_"+str(xBQ2tbin)][0].GetYaxis().SetTitleSize(0.05)
		data["inb_"+str(xBQ2tbin)][0].GetXaxis().SetLabelSize(0.04)
		data["inb_"+str(xBQ2tbin)][0].GetYaxis().SetLabelSize(0.04)
		data["inb_"+str(xBQ2tbin)][0].Draw()
		c1_BSA.Update()
		c2_BSA.cd(placements[xBQ2tbin])
		ROOT.gPad.SetLeftMargin(0.16)
		data["outb_"+str(xBQ2tbin)][0].Fit(data["outb_"+str(xBQ2tbin)][1].GetName())
		data["outb_"+str(xBQ2tbin)][0].GetYaxis().SetTitle("BSA")
		data["outb_"+str(xBQ2tbin)][0].GetXaxis().SetTitle("#phi (#circ)")
		data["outb_"+str(xBQ2tbin)][0].GetXaxis().SetTitleSize(0.05)
		data["outb_"+str(xBQ2tbin)][0].GetYaxis().SetTitleSize(0.05)
		data["outb_"+str(xBQ2tbin)][0].GetXaxis().SetLabelSize(0.04)
		data["outb_"+str(xBQ2tbin)][0].GetYaxis().SetLabelSize(0.04)
		data["outb_"+str(xBQ2tbin)][0].Draw()
		c2_BSA.Update()
		c3_BSA.cd(placements[xBQ2tbin])
		ROOT.gPad.SetLeftMargin(0.16)
		data["all_"+str(xBQ2tbin)][0].Fit(data["all_"+str(xBQ2tbin)][1].GetName())
		data["all_"+str(xBQ2tbin)][0].GetYaxis().SetTitle("BSA")
		data["all_"+str(xBQ2tbin)][0].GetXaxis().SetTitle("#phi (#circ)")
		data["all_"+str(xBQ2tbin)][0].GetXaxis().SetTitleSize(0.05)
		data["all_"+str(xBQ2tbin)][0].GetYaxis().SetTitleSize(0.05)
		data["all_"+str(xBQ2tbin)][0].GetXaxis().SetLabelSize(0.04)
		data["all_"+str(xBQ2tbin)][0].GetYaxis().SetLabelSize(0.04)
		data["all_"+str(xBQ2tbin)][0].Draw()
		c3_BSA.Update()
	c1_BSA.Print("bsa_xBQ2t_inb.pdf")
	c2_BSA.Print("bsa_xBQ2t_outb.pdf")
	c3_BSA.Print("bsa_xBQ2t_all.pdf")

	print("inbending: "+str(int(Integral_inb)))
	print("outbending: "+str(int(Integral_outb)))
	print("total: "+str(int(Integral_inb+Integral_outb)))

def print_BSA(ff1, ff2):

	hplus = {}
	hminus = {}

	xB = {}
	Q2 = {}
	t = {}
	phi = {}

	BSA = {}
	grtl = {}

	entries = {}

	data = {}
	Integral_inb = 0
	Integral_outb = 0

	placements = [0,1,2,3,7,8,9,13,14,15,19,20,21,4,5,6,10,11,12,16,17,18,22,23,24]

	file = open("sangbaek_points.dat","w")

	for xBQ2tbin in range(1,25):

		h1 = deepcopy(ff1.Get("root_dvcs_heli_1_h_trento_xBQ2t_"+str(xBQ2tbin)))
		h2 = deepcopy(ff1.Get("root_dvcs_heli_-1_h_trento_xBQ2t_"+str(xBQ2tbin)))

		Integral_inb = Integral_inb + h1.Integral() + h2.Integral()
		hplus["inb_"+str(xBQ2tbin)] = h1
		hminus["inb_"+str(xBQ2tbin)] = h2

		h3 = deepcopy(ff2.Get("root_dvcs_heli_1_h_trento_xBQ2t_"+str(xBQ2tbin)))
		h4 = deepcopy(ff2.Get("root_dvcs_heli_-1_h_trento_xBQ2t_"+str(xBQ2tbin)))

		Integral_outb = Integral_outb + h3.Integral() + h4.Integral()
		hplus["outb_"+str(xBQ2tbin)] = h3
		hminus["outb_"+str(xBQ2tbin)] = h4

	for xBQ2tbin in range(1,25):
		for binphi in range(1,31):
			nplus_all = hplus["inb_"+str(xBQ2tbin)].GetBinContent(binphi) + hplus["outb_"+str(xBQ2tbin)].GetBinContent(binphi)
			nminus_all = hminus["inb_"+str(xBQ2tbin)].GetBinContent(binphi) + hminus["outb_"+str(xBQ2tbin)].GetBinContent(binphi)
			ntotal_all = nplus_all + nminus_all
			ndiff_all = nplus_all - nminus_all

			hist_xB = []
			hist_Q2 = []
			hist_t =[]
			hist_phi = []

			for heli in ["-1", "1"]:
				for rootfile in [ff1, ff2]:
					hist_xB.append(deepcopy(rootfile.Get("root_dvcs_heli_"+heli+"_h_xB_xBQ2t_"+str(xBQ2tbin)+"_phi_"+str(int(binphi-1)))))
					hist_Q2.append(deepcopy(rootfile.Get("root_dvcs_heli_"+heli+"_h_Q2_xBQ2t_"+str(xBQ2tbin)+"_phi_"+str(int(binphi-1)))))
					hist_t.append(deepcopy(rootfile.Get("root_dvcs_heli_"+heli+"_h_t_xBQ2t_"+str(xBQ2tbin)+"_phi_"+str(int(binphi-1)))))
					hist_phi.append(deepcopy(rootfile.Get("root_dvcs_heli_"+heli+"_h_phi_xBQ2t_"+str(xBQ2tbin)+"_phi_"+str(int(binphi-1)))))

			xB = hist_xB[0]
			Q2 = hist_Q2[0]
			t = hist_t[0]
			phi = hist_phi[0]

			for ind in range(1,4):
				xB.Add(hist_xB[ind])
				Q2.Add(hist_Q2[ind])
				t.Add(hist_t[ind])
				phi.Add(hist_phi[ind])

			xB = xB.GetMean()
			Q2 = Q2.GetMean()
			t = t.GetMean()
			phi = phi.GetMean()

			line = str(int(xBQ2tbin-1))+"\t" +str(int(binphi-1)) + "\t" + str(int(nplus_all))+"\t" + str(int(nminus_all))+ "\t" + '{:0.5f}'.format(xB) + "\t" + '{:0.5f}'.format(Q2) + "\t" +'{:0.5f}'.format(t) + "\t" + '{:0.5f}'.format(phi) + "\n"
			file.write(line)

	file.close()

def print_BSA_oneconfig(ff1):

	hplus = {}
	hminus = {}

	xB = {}
	Q2 = {}
	t = {}
	phi = {}

	BSA = {}
	grtl = {}

	entries = {}

	data = {}
	Integral_config = 0
	Integral_check = 0

	# c1 = ROOT.TCanvas("test", "test",1024,592)

	placements = [0,1,2,3,7,8,9,13,14,15,19,20,21,4,5,6,10,11,12,16,17,18,22,23,24]

	file = open("sangbaek_points_config.dat","w")

	for xBQ2tbin in range(1,25):

		h1 = deepcopy(ff1.Get("root_dvcs_heli_1_h_trento_xBQ2t_"+str(xBQ2tbin)))
		h2 = deepcopy(ff1.Get("root_dvcs_heli_-1_h_trento_xBQ2t_"+str(xBQ2tbin)))

		h1.Rebin(3)
		h2.Rebin(3)

		Integral_config = Integral_config + h1.Integral() + h2.Integral()

		bsatitle = "BSA xBQ2t "+str(int(xBQ2tbin))
		BSA_hist = ROOT.TH1F(bsatitle, bsatitle, 10, 0, 360)
		xBtitle = "xB xBQ2t "+str(int(xBQ2tbin))
		xB_hist = ROOT.TH1F(xBtitle, xBtitle, 1200, 0, 1)
		Q2title = "Q2 xBQ2t "+str(int(xBQ2tbin))
		Q2_hist = ROOT.TH1F(Q2title, Q2title, 1200, 1, 12)
		ttitle = "t xBQ2t "+str(int(xBQ2tbin))
		t_hist = ROOT.TH1F(ttitle, ttitle, 1200, 0, 4)

		for phibin in range(1,11):
			nplus = h1.GetBinContent(phibin)
			nminus = h2.GetBinContent(phibin)
			ntotal = nplus + nminus
			ndiff = nplus - nminus

			hist_xB = []
			hist_Q2 = []
			hist_t =[]
			hist_phi = []

			for heli in ["-1", "1"]:
				hist_xB.append(deepcopy(ff1.Get("root_dvcs_heli_"+heli+"_h_xB_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin-1)))))
				hist_Q2.append(deepcopy(ff1.Get("root_dvcs_heli_"+heli+"_h_Q2_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin-1)))))
				hist_t.append(deepcopy(ff1.Get("root_dvcs_heli_"+heli+"_h_t_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin-1)))))
				hist_phi.append(deepcopy(ff1.Get("root_dvcs_heli_"+heli+"_h_phi_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin-1)))))

			xB = hist_xB[0]
			Q2 = hist_Q2[0]
			t = hist_t[0]
			phi = hist_phi[0]

			xB.Add(hist_xB[1])
			Q2.Add(hist_Q2[1])
			t.Add(hist_t[1])
			phi.Add(hist_phi[1])

			xB_hist.Add(xB)
			Q2_hist.Add(Q2)
			t_hist.Add(t)

			xB = xB.GetMean()
			Q2 = Q2.GetMean()
			t = t.GetMean()
			phi = phi.GetMean()

			data["xB_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))] = '{:0.5f}'.format(xB)
			data["Q2_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))] = '{:0.5f}'.format(Q2)
			data["t_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))] = '{:0.5f}'.format(t)
			data["phi_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))] = '{:0.5f}'.format(phi)
			data["nplus_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))] = str(int(nplus))
			data["nminus_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))] = str(int(nminus))

			BSA_hist.SetBinContent(phibin, 1/0.869*ndiff/ntotal)
			BSA_hist.SetBinError(phibin, 1/0.869*np.sqrt(4*nplus*nminus/(nplus+nminus)**3))

		Fitf = ROOT.TF1("fitf_xBQ2t_"+str(int(xBQ2tbin)), "[alpha]*sin(TMath::DegToRad()*x)/(1+[beta]*cos(TMath::DegToRad()*x))",0.,360.)
		BSA_hist.Fit(Fitf.GetName())
		# if (xBQ2tbin==15):
		# 	BSA_hist.Draw()
		# 	c1.Print("test10bins.pdf")			
		data["xB_xBQ2t_"+str(int(xBQ2tbin))] = '{:0.5f}'.format(xB_hist.GetMean())
		data["Q2_xBQ2t_"+str(int(xBQ2tbin))] = '{:0.5f}'.format(Q2_hist.GetMean())
		data["t_xBQ2t_"+str(int(xBQ2tbin))] = '{:0.5f}'.format(t_hist.GetMean())
		data["alpha_xBQ2t_"+str(int(xBQ2tbin))] = '{:0.5f}'.format(Fitf.GetParameter(0))
		data["alpha_error_xBQ2t_"+str(int(xBQ2tbin))] = '{:0.5f}'.format(Fitf.GetParError(0))
		data["beta_xBQ2t_"+str(int(xBQ2tbin))] = '{:0.5f}'.format(Fitf.GetParameter(1))
		data["beta_error_xBQ2t_"+str(int(xBQ2tbin))] = '{:0.5f}'.format(Fitf.GetParError(1))
		Integral_check = xB_hist.Integral() + Integral_check
		print(Integral_check)


	for xBQ2tbin in range(1,25):
		for phibin in range(1,11):

			line = (str(int(xBQ2tbin-1))+ "\t" +str(int(phibin-1)) + "\t" + data["nplus_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))]
			+ "\t" + data["nminus_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))]
			+ "\t" + data["xB_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))]
			+ "\t" + data["Q2_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))]
			+ "\t" + data["t_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))]
			+ "\t" + data["phi_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin))]
			+ "\t" + data["xB_xBQ2t_"+str(int(xBQ2tbin))]
			+ "\t" + data["Q2_xBQ2t_"+str(int(xBQ2tbin))]
			+ "\t" + data["t_xBQ2t_"+str(int(xBQ2tbin))]
			+ "\t" + data["alpha_xBQ2t_"+str(int(xBQ2tbin))]
			+ "\t" + data["alpha_error_xBQ2t_"+str(int(xBQ2tbin))]
			+ "\t" + data["beta_xBQ2t_"+str(int(xBQ2tbin))]
			+ "\t" + data["beta_error_xBQ2t_"+str(int(xBQ2tbin))]
			+ "\n")
			file.write(line)
	file.close()
	print("integral of this config: "+str(int(Integral_config)))

def check_xBQ2t(ff1, ff2):

	Integral_inb = 0
	Integral_outb = 0
	Integral_all = 0


	placements = [0,1,2,3,7,8,9,13,14,15,19,20,21,4,5,6,10,11,12,16,17,18,22,23,24]

	for xBQ2tbin in range(1,25):


		bsatitle = "BSA xBQ2t "+str(int(xBQ2tbin))
		BSA_hist = ROOT.TH1F(bsatitle, bsatitle, 10, 0, 360)
		xBtitle = "xB xBQ2t "+str(int(xBQ2tbin))
		xB_hist = ROOT.TH1F(xBtitle, xBtitle, 1200, 0, 1)
		Q2title = "Q2 xBQ2t "+str(int(xBQ2tbin))
		Q2_hist = ROOT.TH1F(Q2title, Q2title, 1200, 1, 12)
		ttitle = "t xBQ2t "+str(int(xBQ2tbin))
		t_hist = ROOT.TH1F(ttitle, ttitle, 1200, 0, 4)

		for phibin in range(1,31):

			hist_xB = []
			hist_Q2 = []
			hist_t =[]

			for heli in ["-1", "0", "1"]:
				for rootfile in [ff1, ff2]:
					if (rootfile.Get("root_dvcs_heli_"+heli+"_h_xB_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin-1)))):
						hist_xB.append(deepcopy(rootfile.Get("root_dvcs_heli_"+heli+"_h_xB_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin-1)))))
					if (rootfile.Get("root_dvcs_heli_"+heli+"_h_Q2_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin-1)))):
						hist_Q2.append(deepcopy(rootfile.Get("root_dvcs_heli_"+heli+"_h_Q2_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin-1)))))
					if (rootfile.Get("root_dvcs_heli_"+heli+"_h_t_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin-1)))):
						hist_t.append(deepcopy(rootfile.Get("root_dvcs_heli_"+heli+"_h_t_xBQ2t_"+str(int(xBQ2tbin))+"_phi_"+str(int(phibin-1)))))

			xB_all = deepcopy(hist_xB[0])
			Q2_all = deepcopy(hist_Q2[0])
			t_all = deepcopy(hist_t[0])

			for ind in range(1, len(hist_xB)):
				xB_all.Add(hist_xB[ind])
				Q2_all.Add(hist_Q2[ind])
				t_all.Add(hist_t[ind])

			xB_hist.Add(xB_all)
			Q2_hist.Add(Q2_all)
			t_hist.Add(t_all)

			# Integral_inb = xB_inb.Integral() + Integral_inb
			# Integral_outb = xB_outb.Integral() + Integral_outb
		print("bin: " + str(int(xBQ2tbin)) + " <xB>: {:0.5f}".format(xB_all.GetMean()) + " <Q2>: {:0.5f}".format(Q2_all.GetMean()) + " <t>: {:0.5f}".format(t_all.GetMean()) )
		Integral_all = xB_hist.Integral() + Integral_all

	# print("integral inbending: "+str(int(Integral_inb)))
	# print("integral outbending: "+str(int(Integral_outb)))
	print("integral all: "+str(int(Integral_all)))


def draw_pi0subtraction(ff1,ff2,ff3,ff4):

	xB_array = [0, 0.1, 0.15, 0.2, 0.3, 0.4, 1]
	Q2_array = [1, 1.7, 2.22, 2.7, 3.5, 11]
	t_array = [0, 0.09, 0.13, 0.18, 0.23, 0.3, 0.39, 0.52, 0.72, 1.1, 2]

	xBQ2bin = [[1,2,4,7,7, None], [3,3,5,8,12, 16], [None, 3, 6, 9, 13, 16], [None, None, 6, 10, 14, 16], [None, None, None, 11, 15, 17]]	

	Integral = 0 

	hdata1g = {}
	hdata2g = {}
	hMC1g = {}
	hMC2g = {}

	for Q2bin in range(0,5):
		for xBbin in range(0,6):
			for tbin in range(0,10):

				if (xBQ2bin[Q2bin][xBbin] is None):
					continue

				hist1 = []
				hist2 = []
				hist3 = []
				h1 = 0

				if (ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff1.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff2.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

				if (ff1.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff1.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff1.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff1.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff2.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff2.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff2.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

				if (ff1.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

				if (hist1):
					h1 = hist1[0]
					if (len(hist1)>1):
						for hi in hist1[1:]:
							h1.Add(hi)
				else:
					continue

				if (hist2):
					for h2 in hist2:
						h1.Add(h2, -1)

				if (hist3):
					for h3 in hist3:
						h1.Add(h3, -1)

				if ((xBQ2bin[Q2bin][xBbin], tbin) not in hdata1g):
					hdata1g[xBQ2bin[Q2bin][xBbin], tbin] = h1
				else:
					hdata1g[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)

	for Q2bin in range(0,5):
		for xBbin in range(0,6):
			for tbin in range(0,10):

				if (xBQ2bin[Q2bin][xBbin] is None):
					continue

				hist2 = []
				hist3 = []
				h1 = 0

				if (ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff1.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff2.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

				if (ff1.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff1.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff1.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff1.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff2.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff2.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff2.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

				if (ff1.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff1.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff1.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff2.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff2.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

				if (hist2):
					h1 = hist2[0]
					if (len(hist2)>1):
						for hi in hist2[1:]:
							h1.Add(hi)
					if (hist3):
						for h3 in hist3:
							h1.Add(h3)

				elif (hist3):
					h1 = hist3[0]
					if (len(hist3)>1):
						for hi in hist3[1:]:
							h1.Add(hi)
				else:
					continue

				if ((xBQ2bin[Q2bin][xBbin], tbin) not in hdata2g):
					hdata2g[xBQ2bin[Q2bin][xBbin], tbin] = h1
				else:
					hdata2g[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)




	for Q2bin in range(0,5):
		for xBbin in range(0,6):
			for tbin in range(0,10):

				if (xBQ2bin[Q2bin][xBbin] is None):
					continue

				hist1 = []
				hist2 = []
				hist3 = []
				h1 = 0

				if (ff3.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff3.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff3.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff3.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff3.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff3.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff4.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff4.Get("root_dvcs_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist1.append(ff4.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

				if (ff3.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff3.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff3.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff3.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff3.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff3.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff4.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff4.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff4.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

				if (ff3.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff3.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff3.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

				if (hist1):
					h1 = hist1[0]
					if (len(hist1)>1):
						for hi in hist1[1:]:
							h1.Add(hi)
				else:
					continue

				if (hist2):
					for h2 in hist2:
						h1.Add(h2, -1)

				if (hist3):
					for h3 in hist3:
						h1.Add(h3, -1)

				if ((xBQ2bin[Q2bin][xBbin], tbin) not in hMC1g):
					hMC1g[xBQ2bin[Q2bin][xBbin], tbin] = h1
				else:
					hMC1g[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)

	for Q2bin in range(0,5):
		for xBbin in range(0,6):
			for tbin in range(0,10):

				if (xBQ2bin[Q2bin][xBbin] is None):
					continue

				hist2 = []
				hist3 = []
				h1 = 0

				if (ff3.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff3.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff3.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff3.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff3.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff3.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff4.Get("root_dvcs_pi0_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff4.Get("root_dvcs_pi0_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist2.append(ff4.Get("root_dvcs_pi0_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

				if (ff3.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff3.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff3.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff3.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_0_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))
				if (ff4.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))):
					hist3.append(ff4.Get("root_dvcs_pi0_gam3_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin)))

				if (hist2):
					h1 = hist2[0]
					if (len(hist2)>1):
						for hi in hist2[1:]:
							h1.Add(hi)
					if (hist3):
						for h3 in hist3:
							h1.Add(h3)

				elif (hist3):
					h1 = hist3[0]
					if (len(hist3)>1):
						for hi in hist3[1:]:
							h1.Add(hi)
				else:
					continue

				if ((xBQ2bin[Q2bin][xBbin], tbin) not in hMC2g):
					hMC2g[xBQ2bin[Q2bin][xBbin], tbin] = h1
				else:
					hMC2g[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)


	for ind_xBQ2 in range(1,18):
		c1 = ROOT.TCanvas('c'+str(ind_xBQ2),'c'+str(ind_xBQ2),1024,592)
		c1.Divide(4,3)
		for tbin in range(0,10):
			c1.cd(tbin+1)
			if ((not (ind_xBQ2, tbin) in hMC1g) or (not (ind_xBQ2, tbin) in hMC2g) or (not (ind_xBQ2, tbin) in hdata1g) or (not (ind_xBQ2, tbin) in hdata2g)   ):
				print(ind_xBQ2, tbin)
				print((ind_xBQ2, tbin) in hMC1g) 
				print((ind_xBQ2, tbin) in hMC2g) 
				print((ind_xBQ2, tbin) in hdata1g) 
				print((ind_xBQ2, tbin) in hdata2g)
				# hdummy.Draw()
				if ((ind_xBQ2, tbin) in hdata1g):
					hdata1g[ind_xBQ2, tbin].SetTitle("Raw Yields, xBQ2 "+str(ind_xBQ2)+" t "+str(tbin))
					Integral = Integral + hdata1g[ind_xBQ2, tbin].Integral()
					hdata1g[ind_xBQ2, tbin].GetXaxis().SetTitle("#phi (#circ)")
					hdata1g[ind_xBQ2, tbin].GetXaxis().SetTitleSize(0.05)
					hdata1g[ind_xBQ2, tbin].GetYaxis().SetTitleSize(0.05)
					hdata1g[ind_xBQ2, tbin].GetXaxis().SetLabelSize(0.04)
					hdata1g[ind_xBQ2, tbin].GetYaxis().SetLabelSize(0.04)
					hdata1g[ind_xBQ2, tbin].Draw()

				c1.Update()
			else:
				for binphi in range(0,24):
					data1g = hdata1g[ind_xBQ2, tbin].GetBinContent(binphi)
					data2g = hdata2g[ind_xBQ2, tbin].GetBinContent(binphi)
					MC1g   = hMC1g[ind_xBQ2, tbin].GetBinContent(binphi)
					MC2g   = hMC2g[ind_xBQ2, tbin].GetBinContent(binphi)
					if (MC2g):
						estimate = data1g - data2g * MC1g/MC2g
						# hdata1g[ind_xBQ2, tbin].SetBinContent(binphi,estimate)
						hdata2g[ind_xBQ2, tbin].SetBinContent(binphi,data2g * MC1g/MC2g)
					else:
						hdata2g[ind_xBQ2, tbin].SetBinContent(binphi,0)
				hdata1g[ind_xBQ2, tbin].SetTitle("Raw Yields, xBQ2 "+str(ind_xBQ2)+" t "+str(tbin))
				Integral = Integral + hdata1g[ind_xBQ2, tbin].Integral()
				hdata1g[ind_xBQ2, tbin].GetXaxis().SetTitle("#phi (#circ)")
				hdata1g[ind_xBQ2, tbin].GetXaxis().SetTitleSize(0.05)
				hdata1g[ind_xBQ2, tbin].GetYaxis().SetTitleSize(0.05)
				hdata1g[ind_xBQ2, tbin].GetXaxis().SetLabelSize(0.04)
				hdata1g[ind_xBQ2, tbin].GetYaxis().SetLabelSize(0.04)
				hdata1g[ind_xBQ2, tbin].Draw()
				hdata2g[ind_xBQ2, tbin].SetLineColor(ROOT.kRed)
				hdata2g[ind_xBQ2, tbin].Draw("SAME")
				c1.Update()
		c1.Print("rawyields_subtracted_xBQ2_"+str(ind_xBQ2)+".pdf")
	print("total events: "+str(Integral))

def draw_kinReach(ff1, ff2):
	c1 = ROOT.TCanvas('c1','c1',600,600)

	h1 = ff1.Get("root_dvcs_binning_h_Q2_xB")
	h1.Add(ff2.Get("root_dvcs_binning_h_Q2_xB"))

	curve1 =  ROOT.TF1("curve1","x*2*0.9382721*(5.75-0.8)",1/2/0.9382721/(5.75-0.8),0.295);
	curve2 =  ROOT.TF1("curve1","1",1/2/0.9382721/(5.75-0.8),0.122);
	curve3 =  ROOT.TF1("curve1","2*5.75*0.9382721*x/(1+0.9382721*x/5.75/(1-0.93358))",0.118,0.42);
	curve4 =  ROOT.TF1("curve1","2*5.75*0.9382721*x/(1+0.9382721*x/5.75/(1-0.707107))",0.285,0.617);
	curve5 =  ROOT.TF1("curve1","(4 - 0.9382721*0.9382721)*x/(1 - x)",0.415,0.614);
	CLAS_curves =[curve1, curve2, curve3, curve4, curve5]

	c1.cd(1)
	h1.SetTitle("")
	h1.GetXaxis().SetTitle("x_{B}")
	h1.GetYaxis().SetTitle("Q^{2} [(GeV/c)^{2}]")
	h1.GetXaxis().SetTitleSize(0.05)
	h1.GetXaxis().SetLabelSize(0.04)
	h1.GetYaxis().SetTitleSize(0.05)
	h1.GetYaxis().SetLabelSize(0.04)
	h1.GetXaxis().SetRangeUser(0, 0.8)
	h1.GetYaxis().SetRangeUser(0, 12)
	ROOT.gPad.SetLeftMargin(0.15)
	ROOT.gPad.SetRightMargin(0.18)
	ROOT.gPad.SetBottomMargin(0.12)
	ROOT.gPad.SetLogz()
	h1.Draw("colz")

	for curve in CLAS_curves:
		curve.SetLineWidth(3)
		curve.SetLineColor(ROOT.kBlack)
		curve.Draw("same")
	c1.Print("kinreach.pdf")


# draw_elecSampling(ff1, ff2)
# draw_elecPCALECAL(ff1, ff2)
# draw_elecKinematics(ff1, ff2)
# draw_protKinematics_FD(ff1, ff2)
# draw_protKinematics_CD(ff1, ff2)
# draw_photKinematics_FD(ff1, ff2)
# draw_photKinematics_FT(ff1, ff2)
# draw_exclCuts(ff1, ff2)
# draw_exclCutsMEMM(ff1, ff2)
# draw_twoPhotons(ff1, ff2)
# draw_twoPhotons2(ff1, ff2)
# draw_twoPhotons3(ff1, ff2)
# draw_corrPlot_tcoltmin(ff1, ff2)
# draw_binning(ff1, ff2)
# draw_logBinning(ff1, ff2)
# draw_kinCorrGamma(ff1, ff2)
# draw_BSA(ff1, ff2)
# print_BSA(ff1, ff2)
# print_BSA_oneconfig(ff1)
draw_rawYields(ff1, ff2)
# draw_pi0subtraction(ff1, ff2, ff3, ff4)
# check_xBQ2t(ff1, ff2)
# draw_kinReach(ff1, ff2)