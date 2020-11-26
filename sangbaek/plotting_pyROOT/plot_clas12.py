#!/usr/bin/python

import sys
sys.argv.append('-b')
import ROOT
import numpy as np
from array import array

ff1 = ROOT.TFile(sys.argv[1])
ff2 = ROOT.TFile(sys.argv[2])

ROOT.gStyle.SetOptStat(0)
ROOT.TGaxis.SetMaxDigits(3);
ROOT.gStyle.SetPalette(1)

"""
Drawing raw yields
"""
# c1 = ROOT.TCanvas('c1','c1',1024,592)
# c1.Divide(3,3)

# xB_array = [0.1, 0.14, 0.17, 0.2, 0.23, 0.26, 0.29, 0.32, 0.35, 0.38, 0.42, 0.58]
# t_array = [0.09, 0.13, 0.18, 0.23, 0.3, 0.39, 0.52, 0.72, 1.1, 2]
# Integral = 0

# h2 = ROOT.TH1F("test","test",24,0,360)

# for i in range(1,190):
# 	c1.cd((i-1)%9+1)
# 	tbin = (i-1)%9
# 	xBQbin = (i-1)//9+1
# 	h1 = ff.Get("root_dvcs_h_phi_pro_CD_gam_FT_bin_"+str(21*tbin + xBQbin))
# 	if (not h1):
# 		h1 = h2.Clone(str(i))

# 	h1.SetTitle("bin"+str((i-1)//9+1)+"\t"+str(t_array[(i-1)%9])+"<-t<"+str(t_array[(i-1)%9+1])+" GeV ^{2}")
# 	h1.GetXaxis().SetTitle("#phi (#circ)");
# 	Integral = Integral + h1.Integral()
# 	if i%9 == 0:
# 		h1.Draw()
# 		c1.Update()
# 		if i == 9:
# 			c1.Print("clas12_dvcs_raw_yields.pdf(")
# 		elif i == 189:
# 			c1.Print("clas12_dvcs_raw_yields.pdf)")		
# 		else:
# 			c1.Print("clas12_dvcs_raw_yields.pdf")		
# 	else:
# 		h1.Draw()
# 		c1.Update()

# print(Integral)

"""
Drawing proton CDFD alignment check
"""

# c1 = ROOT.TCanvas('c1','c1',1600, 1200)
# c1.Divide(1,2)

# c1.cd(1)
# h1 = ff.Get("root_prot_prot_polar_FD")
# h1.SetTitle("")
# h1.GetXaxis().SetTitle("#theta (#circ)");
# # h1.GetYaxis().SetRangeUser(0,6);
# h1.SetLineColor(4)
# h2 = ff.Get("root_prot_prot_polar_CD")
# h2.SetTitle("")
# h2.GetXaxis().SetTitle("#theta (#circ)");
# h2.SetLineColor(2)
# h1.Draw("")
# h2.Draw("same")

# c1.cd(2)
# h1 = ff.Get("root_dvcs_prot_polar_FD")
# h1.SetTitle("")
# h1.GetXaxis().SetTitle("#theta (#circ)");
# # h1.GetYaxis().SetRangeUser(0,6);
# h1.SetLineColor(4)
# h2 = ff.Get("root_dvcs_prot_polar_CD")
# h2.SetTitle("")
# h2.GetXaxis().SetTitle("#theta (#circ)");
# h2.SetLineColor(2)
# h2.Draw("")
# h1.Draw("same")
# c1.Print("proton_CDFD.pdf")

"""
Drawing correlation plots
"""
# c1 = ROOT.TCanvas('c1','c1',906, 700)
# c1.Divide(4,6,0,0)
# h3 = ROOT.TH1F("dummy","dummy",100,0,4)
# for Q2 in range(0,6):
# 	for xB in range(0,4):
# 		c1.cd(4*(5-Q2)+xB+1)
# 		h1 = ff.Get("root_dvcs_corr_prot_phi_mom_xB_"+str(2*xB+1)+"_Q2_"+str(2*Q2+1))
# 		if (not h1):
# 			h1=h3.Clone(str(7*(9-xB)+Q2+1))
# 		h1.SetTitle("")
# 		h1.GetXaxis().SetTitle("");
# 		h1.GetXaxis().SetRangeUser(0,3.5)
# 		# h1.GetYaxis().SetRangeUser(0,35)
# 		h1.Draw("colz")
# 		c1.Update()
# c1.Print("dvcs_corr.pdf")

"""
Drawing BSA
"""
# h_t_t = ff1.Get("root_dvcs_corr_h_t_t")
# h_t_t.Add(ff2.Get("root_dvcs_corr_h_t_t"))
# c_t_t = ROOT.TCanvas("t_t", "t_t",640, 480)
# h_t_t.SetTitle("-t correlation")
# h_t_t.GetXaxis().SetTitle("-t using proton energy (GeV^{2})")
# h_t_t.GetYaxis().SetTitle("-t using photon (GeV^{2})")
# h_t_t.Draw("colz")
# c_t_t.SetLogz()
# c_t_t.Print("tt_corr.pdf")


# c_Q2_xB = ROOT.TCanvas("Q2_xB", "Q2_xB",640, 480)
# c_Q2_xB.SetLogz()
# c_Q2_xB.cd()

# h_Q2_xB_inb = ff1.Get("root_dvcs_binning_h_Q2_xB")
# h_Q2_xB_outb = ff2.Get("root_dvcs_binning_h_Q2_xB")
# h_Q2_xB_outb.Draw("colz")
# c_Q2_xB.Print("Q2_xB.pdf")

# h_Q2_xB_tmin = ff2.Get("root_dvcs_corr_tmin")
# h_Q2_xB_tmin.Divide(h_Q2_xB_outb)
# h_Q2_xB_tmin.Draw("colz")
# c_Q2_xB.Print("Q2_xB_tmin.pdf")

# h_Q2_xB_tcol = ff2.Get("root_dvcs_corr_tcol")
# h_Q2_xB_tcol.Divide(h_Q2_xB_outb)
# h_Q2_xB_tcol.Draw("colz")
# c_Q2_xB.Print("Q2_xB_tcol.pdf")

# h_Q2_xB_t1 = ff2.Get("root_dvcs_corr_h_Q2_xB_t1")
# h_Q2_xB_t1.Divide(h_Q2_xB_outb)
# h_Q2_xB_t1.Draw("colz")
# c_Q2_xB.Print("Q2_xB_t1.pdf")

# h_Q2_xB_t2 = ff2.Get("root_dvcs_corr_h_Q2_xB_t2")
# h_Q2_xB_t2.Divide(h_Q2_xB_outb)
# h_Q2_xB_t2.Draw("colz")
# c_Q2_xB.Print("Q2_xB_t2.pdf")

# xB_array = [0, 0.1, 0.15, 0.2, 0.3, 0.4, 1]
# Q2_array = [1, 1.7, 2.22, 2.7, 3.5, 11]
# t_array = [0, 0.09, 0.13, 0.18, 0.23, 0.3, 0.39, 0.52, 0.72, 1.1, 2]

# xBQ2bin = [[1,2,4,7,7, None], [3,3,5,8,12, 16], [None, 3, 6, 9, 13, 16], [None, None, 6, 10, 14, 16], [None, None, None, 11, 15, 17]]	
# hplus = {}
# hminus = {}
# BSA = {}
# grtl = {}

# entries = {}
# xB_sum = {}
# Q2_sum = {}
# t_sum = {}

# def xB_binning(xB):
# 	if xB<0.1:
# 		return 0
# 	elif xB<0.15:
# 		return 1
# 	elif xB<0.2:
# 		return 2
# 	elif xB<0.3:
# 		return 3
# 	elif xB<0.4:
# 		return 4
# 	else:
# 		return 5

# def Q2_binning(Q2):
# 	if Q2<1.7:
# 		return 0
# 	elif Q2<2.22:
# 		return 1
# 	elif Q2<2.7:
# 		return 2
# 	elif Q2<3.5:
# 		return 3
# 	else:
# 		return 4

# for xB in range(1, h_Q2_xB_outb.GetNbinsX()+1):
# 	for Q2 in range(1, h_Q2_xB_outb.GetNbinsY()+1):
# 		xBcen = h_Q2_xB_outb.GetXaxis().GetBinCenter(xB)
# 		Q2cen = h_Q2_xB_outb.GetXaxis().GetBinCenter(Q2)


# data = {}
# Integral = 0 
# for Q2bin in range(0,5):
# 	for xBbin in range(0,6):
# 		for tbin in range(0,10):

# 			if (xBQ2bin[Q2bin][xBbin] is None):
# 				continue

# 			h1 = ff1.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))
# 			h2 = ff1.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))
# 			h3 = ff2.Get("root_dvcs_heli_1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))
# 			h4 = ff2.Get("root_dvcs_heli_-1_h_trento_xB_"+str(xBbin)+"_Q2_"+str(Q2bin)+"_t_"+str(tbin))

# 			if (h1 and h3):
# 				h1.Add(h3)
# 			elif (not h1 and h3):
# 				h1 = h3
# 			elif (not h1 and not h3):
# 				continue
# 			if (h2 and h4):
# 				h2.Add(h4)
# 			elif (not h2 and h4):
# 				h2 = h4
# 			elif (not h2 and not h4):
# 				continue

# 			h1.Rebin()
# 			h2.Rebin()

# 			Integral = Integral + h1.Integral() + h2.Integral()
# 			if ((xBQ2bin[Q2bin][xBbin], tbin) in hplus):
# 				hplus[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)
# 			else: 
# 				hplus[xBQ2bin[Q2bin][xBbin], tbin] = h1
# 			if ((xBQ2bin[Q2bin][xBbin], tbin) in hminus):
# 				hminus[xBQ2bin[Q2bin][xBbin], tbin].Add(h1)
# 			else: 
# 				hminus[xBQ2bin[Q2bin][xBbin], tbin] = h2

# for ind_xBQ2 in range(1,18):
# 	for tbin in range(0,10):
# 		if ((not (ind_xBQ2, tbin) in hplus) or (not (ind_xBQ2, tbin) in hminus)):
# 			continue
# 		bsatitle = "bsa_xBQ2_"+str(ind_xBQ2)+"_t_"+str(tbin)	
# 		BSA_hist = ROOT.TH1F(bsatitle, bsatitle, 12, 0, 360)
# 		for binx in range(0,12):
# 			nplus = hplus[ind_xBQ2,tbin].GetBinContent(binx)
# 			nminus = hminus[ind_xBQ2,tbin].GetBinContent(binx)
# 			ntotal = nplus + nminus
# 			ndiff = nplus - nminus
# 			if (nplus < 3 or nminus < 3):
# 				continue
# 			BSA_hist.SetBinContent(binx, 1/0.8*ndiff/ntotal)
# 			BSA_hist.SetBinError(binx, 1/0.8*np.sqrt(4*nplus*nminus/(nplus+nminus)**3))
# 		Fitf = ROOT.TF1("fitf_xBQ2_"+str(ind_xBQ2)+"_t_"+str(tbin), "[alpha]*sin(TMath::DegToRad()*x)/(1+[beta]*cos(TMath::DegToRad()*x))",0.,360.)
# 		data[ind_xBQ2, tbin] = [BSA_hist, Fitf]
# 		BSA_hist.Fit(Fitf.GetName())
# 		BSA_hist.Draw()

# for ind_xBQ2 in range(1,18):
# 	c1 = ROOT.TCanvas("c1_xBQ2_"+str(ind_xBQ2),"c1_xBQ2_"+str(ind_xBQ2),480,480)
# 	c1.Divide(3,4)
# 	t_array2 = array('f', [])
# 	e_t_array = array('f', [])
# 	alpha_array = array('f', [])
# 	e_alpha_array = array('f', [])
# 	for tbin in range(0,10):
# 		if (not (ind_xBQ2, tbin) in data):
# 			continue
# 		c1.cd(tbin+1)
# 		data[ind_xBQ2, tbin][0].Fit(data[ind_xBQ2, tbin][1].GetName())
# 		data[ind_xBQ2, tbin][0].GetYaxis().SetTitle("BSA")
# 		data[ind_xBQ2, tbin][0].Draw()

# 		if (data[ind_xBQ2, tbin][1].GetParError(0) < 0.1):
# 			t_array2.append(t_array[tbin]*0.5 + t_array[tbin+1]*0.5 + (9-ind_xBQ2)*0.005)
# 			alpha_array.append(data[ind_xBQ2, tbin][1].GetParameter(0))
# 			e_t_array.append(0)
# 			e_alpha_array.append(data[ind_xBQ2, tbin][1].GetParError(0))
# 		c1.Update()

# 	c1.cd(12)
# 	gr = ROOT.TGraphErrors( len(t_array2), t_array2, alpha_array, e_t_array, e_alpha_array)
# 	gr.SetTitle( '#alpha vs -t at xBQ2_'+str(ind_xBQ2) )
# 	gr.SetMarkerColor( 4 )
# 	gr.SetMarkerStyle( 21 )
# 	gr.SetMarkerSize( 0.25* gr.GetMarkerSize() )
# 	grtl[ind_xBQ2] = gr
# 	gr.GetYaxis().SetTitle("#alpha")
# 	gr.GetXaxis().SetTitle("-t (GeV^{2})")
# 	gr.Draw( 'ALP' )

# 	c1.Print("bsa_xBQ2_"+str(ind_xBQ2)+".pdf")

# c2 = ROOT.TCanvas("c2","c2",640,480)
# mg = ROOT.TMultiGraph("alpha vs -t", "alpha vs -t")
# mg.SetTitle("#alpha vs -t (x_{B} = 0.09); -t (GeV^{2}); #alpha");
# grtl[1].SetMarkerColor( ROOT.kBlack )
# grtl[1].SetLineColor( ROOT.kBlack )
# mg.Add(grtl[1])
# mg.SetMinimum(-0.2)
# mg.SetMaximum(0.5)
# mg.Draw("AP")
# legend = ROOT.TLegend(.65, .77, 0.95, .83)
# legend.AddEntry(grtl[1], "1, x_{B} 0.09, Q^{2} 1.17")
# legend.Draw()
# c2.Print("alpha_1.pdf")

# c2.cd()
# mg = ROOT.TMultiGraph("alpha vs -t", "alpha vs -t")
# mg.SetTitle("#alpha vs -t (x_{B} = 0.13); -t (GeV^{2}); #alpha");
# grtl[2].SetMarkerColor( ROOT.kRed )
# grtl[2].SetLineColor( ROOT.kRed )
# grtl[3].SetMarkerColor( ROOT.kBlack )
# grtl[3].SetLineColor( ROOT.kBlack )
# mg.Add(grtl[3])
# mg.Add(grtl[2])
# mg.SetMinimum(-0.2)
# mg.SetMaximum(0.5)
# mg.Draw("AP")
# legend = ROOT.TLegend(.65, .74, 0.95, .86)
# legend.AddEntry(grtl[3], "3, x_{B} 0.13, Q^{2} 1.91")
# legend.AddEntry(grtl[2], "2, x_{B} 0.12, Q^{2} 1.34")
# legend.Draw()
# c2.Print("alpha_23.pdf")

# c2.cd()
# mg = ROOT.TMultiGraph("alpha vs -t", "alpha vs -t")
# mg.SetTitle("#alpha vs -t (x_{B} = 0.17); -t (GeV^{2}); #alpha");
# grtl[4].SetMarkerColor( ROOT.kBlue )
# grtl[4].SetLineColor( ROOT.kBlue )
# grtl[5].SetMarkerColor( ROOT.kRed )
# grtl[5].SetLineColor( ROOT.kRed )
# grtl[6].SetMarkerColor( ROOT.kBlack )
# grtl[6].SetLineColor( ROOT.kBlack )
# mg.Add(grtl[6])
# mg.Add(grtl[5])
# mg.Add(grtl[4])
# mg.SetMinimum(-0.2)
# mg.SetMaximum(0.5)
# mg.Draw("AP")
# legend = ROOT.TLegend(.65, .71, 0.95, .89)
# legend.AddEntry(grtl[6], "6, x_{B} 0.18, Q^{2} 2.50")
# legend.AddEntry(grtl[5], "5, x_{B} 0.17, Q^{2} 1.93")
# legend.AddEntry(grtl[4], "4, x_{B} 0.17, Q^{2} 1.35")
# legend.Draw()
# c2.Print("alpha_456.pdf")

# c2.cd()
# mg = ROOT.TMultiGraph("alpha vs -t", "alpha vs -t")
# mg.SetTitle("#alpha vs -t (x_{B} = 0.24); -t (GeV^{2}); #alpha");
# grtl[7].SetMarkerColor( ROOT.kViolet )
# grtl[7].SetLineColor( ROOT.kViolet )
# grtl[8].SetMarkerColor( ROOT.kGreen + 4 )
# grtl[8].SetLineColor( ROOT.kGreen + 4 )
# grtl[9].SetMarkerColor( ROOT.kBlue )
# grtl[9].SetLineColor( ROOT.kBlue )
# grtl[10].SetMarkerColor( ROOT.kRed )
# grtl[10].SetLineColor( ROOT.kRed )
# grtl[11].SetMarkerColor( ROOT.kBlack )
# grtl[11].SetLineColor( ROOT.kBlack )
# mg.Add(grtl[11])
# mg.Add(grtl[10])
# mg.Add(grtl[9])
# mg.Add(grtl[8])
# mg.Add(grtl[7])
# mg.SetMinimum(-0.2)
# mg.SetMaximum(0.5)
# mg.Draw("AP")
# legend = ROOT.TLegend(.65, .65, 0.95, .95)
# legend.AddEntry(grtl[11], "11, x_{B} 0.26, Q^{2} 3.87")
# legend.AddEntry(grtl[10], "10, x_{B} 0.24, Q^{2} 3.1")
# legend.AddEntry(grtl[9], "9, x_{B} 0.24, Q^{2} 2.45")
# legend.AddEntry(grtl[8], "8, x_{B} 0.24, Q^{2} 1.93")
# legend.AddEntry(grtl[7], "7, x_{B} 0.22, Q^{2} 1.49")
# legend.Draw()
# c2.Print("alpha_7891011.pdf")

# c2.cd()
# mg = ROOT.TMultiGraph("alpha vs -t", "alpha vs -t")
# mg.SetTitle("#alpha vs -t (x_{B} = 0.034); -t (GeV^{2}); #alpha");
# grtl[12].SetMarkerColor( ROOT.kGreen + 4 )
# grtl[12].SetLineColor( ROOT.kGreen + 4 )
# grtl[13].SetMarkerColor( ROOT.kBlue )
# grtl[13].SetLineColor( ROOT.kBlue )
# grtl[14].SetMarkerColor( ROOT.kRed )
# grtl[14].SetLineColor( ROOT.kRed )
# grtl[15].SetMarkerColor( ROOT.kBlack )
# grtl[15].SetLineColor( ROOT.kBlack )
# mg.Add(grtl[15])
# mg.Add(grtl[14])
# mg.Add(grtl[13])
# mg.Add(grtl[12])
# mg.SetMinimum(-0.2)
# mg.SetMaximum(0.5)
# mg.Draw("AP")
# legend = ROOT.TLegend(.65, .68, 0.95, .92)
# legend.AddEntry(grtl[15], "15, x_{B} 0.35, Q^{2} 4.36")
# legend.AddEntry(grtl[14], "14, x_{B} 0.35, Q^{2} 3.1")
# legend.AddEntry(grtl[13], "13, x_{B} 0.34, Q^{2} 2.49")
# legend.AddEntry(grtl[12], "12, x_{B} 0.32, Q^{2} 2.01")
# legend.Draw()
# c2.Print("alpha_12131415.pdf")


# c2.cd()
# mg = ROOT.TMultiGraph("alpha vs -t", "alpha vs -t")
# mg.SetTitle("#alpha vs -t (x_{B} = 0.047); -t (GeV^{2}); #alpha");
# grtl[17].SetMarkerColor( ROOT.kBlack )
# grtl[17].SetLineColor( ROOT.kBlack )
# grtl[16].SetMarkerColor( ROOT.kRed )
# grtl[16].SetLineColor( ROOT.kRed )
# mg.Add(grtl[17])
# mg.Add(grtl[16])
# mg.SetMinimum(-0.2)
# mg.SetMaximum(0.5)
# mg.Draw("AP")
# legend = ROOT.TLegend(.65, .74, 0.95, .86)
# legend.AddEntry(grtl[17], "17, x_{B} 0.44, Q^{2} 3.08")
# legend.AddEntry(grtl[16], "16, x_{B} 0.50, Q^{2} 5.22")
# legend.Draw()
# c2.Print("alpha_1617.pdf")

# print("Integral: " + str(Integral))

"""
Misc.
"""
# c1.cd()
# h1 = ff.Get("epg_h_Q2_xB")
# h1.SetTitle("Q^{2} - x_{B}")
# h1.GetXaxis().SetTitle("x_{B}");
# h1.GetYaxis().SetTitle("Q^{2} (GeV^{2})");
# # h1.GetYaxis().SetRangeUser(0,6);
# h1.Draw("colz")
# c1.Print("dvcs_clas12.pdf(")

# c1.cd()
# h1 = ff.Get("epg_h_Q2_xB_W<2")
# h1.SetTitle("Q^{2} - x_{B}")
# h1.GetXaxis().SetTitle("x_{B}");
# h1.GetYaxis().SetTitle("Q^{2} (GeV^{2})");
# h1.GetYaxis().SetRangeUser(0.5,5.5);
# h1.GetXaxis().SetLimits(.05,.7);
# h2 = ff.Get("epg_h_Q2_xB_5_theta_10")
# h2.SetMarkerColor(2)
# h3 = ff.Get("epg_h_Q2_xB_10_theta_15")
# h3.SetMarkerColor(3)
# h4 = ff.Get("epg_h_Q2_xB_15_theta_20")
# h4.SetMarkerColor(4)
# h5 = ff.Get("epg_h_Q2_xB_20_theta_25")
# h5.SetMarkerColor(6)
# h6 = ff.Get("epg_h_Q2_xB_25_theta_30")
# h6.SetMarkerColor(7)
# h7 = ff.Get("epg_h_Q2_xB_30_theta_35")
# h7.SetMarkerColor(28)

# h1.Draw()
# h2.Draw("same")
# h3.Draw("same")
# h4.Draw("same")
# h5.Draw("same")
# h6.Draw("same")
# h7.Draw("same")
# h1.Draw("same")
# c1.Print("dvcs_clas12.pdf")

# c1.cd()
# h1 = ff.Get("epg_h_t_xB")
# h1.SetTitle("t - x_{B}")
# h1.GetXaxis().SetTitle("x_{B}");
# h1.GetYaxis().SetTitle("-t (GeV^{2})");
# # h1.GetYaxis().SetRangeUser(0,6);
# h1.Draw("colz")
# c1.Print("dvcs_clas12.pdf)")

# c1.cd()
# h1 = ff.Get("rates_h_ele_rate")
# h1.SetTitle("electron rates over 4.5 #circ")
# h1.GetXaxis().SetTitle("#theta (#circ)")
# h1.GetYaxis().SetTitle("Counts/ day")
# h1.Scale(ratio)
# h1.Draw("ehist")
# c1.Print("dvcs_clas12.pdf")

# c1.cd()
# h1 = ff.Get("rates_h_pro_rate")
# h1.SetTitle("Proton rates over 4.5 #circ")
# h1.GetXaxis().SetTitle("#theta (#circ)")
# h1.GetYaxis().SetTitle("Counts/ day")
# h1.Scale(ratio)
# h1.Draw("ehist")
# c1.Print("dvcs_clas12.pdf")

# c1.cd()
# h1 = ff.Get("rates_h_gam_rate")
# h1.SetTitle("Photon rates over 4.5 #circ")
# h1.GetXaxis().SetTitle("#theta (#circ)")
# h1.GetYaxis().SetTitle("Counds/ day")
# h1.Scale(ratio)
# h1.Draw("ehist")
# c1.Print("dvcs_clas12.pdf")

# c1.cd()
# h1 = ff.Get("angular_h_ep_azimuth")
# h1.SetTitle("e-p azimuthal angle")
# h1.GetXaxis().SetTitle("#phi_{p} (#circ)")
# h1.GetYaxis().SetTitle("#phi_{e} (#circ)")
# h1.Draw("colz")
# c1.Print("dvcs_clas12.pdf")


# c1.cd()
# h1 = ff.Get("epg_hmm2_epg")
# h1.SetTitle("Missing Mass Squared, ep#gamma")
# h1.GetXaxis().SetTitle("MM^{2}_{ep#gamma} (GeV^{2})")
# h1.Draw("colz")
# c1.Print("dvcs_clas12.pdf")

# c1.cd()
# h1 = ff.Get("angular_h_ep_azimuth_diff")
# h1.SetTitle("e-p azimuthal angle difference")
# h1.GetXaxis().SetTitle("|#phi_{e}-#phi_{p}| (#circ)")
# h1.Draw("colz")
# c1.Print("dvcs_clas12.pdf")

# c1.cd()
# h1 = ff.Get("angular_h_ep_polar")
# h1.SetTitle("e-p polar angle")
# h1.GetXaxis().SetTitle("#theta_{p} (#circ)")
# h1.GetYaxis().SetTitle("#theta_{e} (#circ)")
# h1.Draw("colz")

# f1 = ROOT.TF1('f1', '180-2*180/TMath::Pi()*TMath::ATan(5.938/0.938*TMath::Tan(x*TMath::Pi()/180))', 0,90)
# f1.Draw("same")


# c1.Print("dvcs_clas12.pdf")

# c1.cd()
# h1 = ff.Get("xsec_h_cross_section")
# h1.SetTitle("DVCS cross section (rg-a train)")
# h1.GetXaxis().SetTitle("#phi (#circ)")
# h1.GetYaxis().SetTitle("Number of Events")
# print(h1.Integral())
# c1.SetLogy()

# h1.Draw("ehist")
# c1.Print("dvcs_clas12.pdf)")

"""
Temporary place
"""

c1 = ROOT.TCanvas('c1','c1',800, 600)

h_Q2_xB_inb = ff1.Get("root_dvcs_binning_h_Q2_xB")
h_Q2_xB_outb = ff2.Get("root_dvcs_binning_h_Q2_xB")
h_Q2_xB_inb.Add(h_Q2_xB_outb)
c1.cd()
h_Q2 = h_Q2_xB_inb.ProjectionY()
h_Q2.Draw("colz")
c1.Print("test.pdf")