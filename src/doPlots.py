#!/usr/bin/env python3
"""
This routine creates the following figures:
 - xiNegPPlane.pdf: trajectories in the phase plane for xi < 0
 - xiPosPPlane.pdf: trajectories in the phase plane for xi > 0
 - SadSadPplane.pdf: the unique saddle-saddle connection
 - DeltaPhi-v-kappa.pdf gel-buffer potential as a function of the value kappa

For the first three, we use C0 = 130 and kappa = 10. The last figures uses a
range of values in kappa
"""
# ======================================
# Packages
# ======================================
import numpy as np
import matplotlib.pyplot as plt
from utils import doNegTrajectory, doPosTrajectory, doSadSadTrajectory, doGBplots

# ======================================
# Main Simluation
# ======================================
def doPlots():

	# --- Parameters
	C0 = 130
	kappa = 10

	# --- Trajectories for xi < 0	
	fig = doNegTrajectory(kappa, C0)
	plt.show()
	fig.savefig('../figures/xiNegPPlane.pdf', format = 'pdf')

	# --- Trajectories for xi > 0	
	fig = doPosTrajectory(kappa, C0)
	plt.show()
	fig.savefig('../figures/xiPosPPlane.pdf', format = 'pdf')

	# --- Unique saddle-saddle connection	
	fig = doSadSadTrajectory(kappa, C0)
	plt.show()
	fig.savefig('../figures/SadSadPPlane.pdf', format = 'pdf')

	# --- Gel-buffer potential as a function of C0, saturating to Donnan potential
	kap_range = np.logspace(-2, 2, 2**8+1)
	fig = doGBplots(kap_range, C0)
	plt.show()
	fig.savefig("../figures/DeltaPhi-v-kappa.pdf", format="pdf")
	
# ======================================
# Execute if the script is run directly
# ======================================
if __name__ == "__main__":
	doPlots()

