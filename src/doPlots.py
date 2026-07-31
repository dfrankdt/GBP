#!/usr/bin/env python3
"""
Figures:

"""
import numpy as np
import matplotlib.pyplot as plt
from utils import doGBplots, doPosTrajectory, doNegTrajectory, doSadSadTrajectory
	


# ======================================
# Main Simluation
# ======================================
def doPlots():

	# --- Parameters
	C0 = 130

	kap_range = np.logspace(-2, 2, 2**8+1)
	
	fig = doGBplots(kap_range, C0)
	plt.show()
	fig.savefig("../figures/DeltaPhi-v-kappa.pdf", format="pdf")
	
	kappa = 10
	
	fig = doPosTrajectory(kappa, C0)
	plt.show()
	fig.savefig('../figures/xiPosPPlane.pdf', format = 'pdf')
	
	fig = doNegTrajectory(kappa, C0)
	plt.show()
	fig.savefig('../figures/xiNegPPlane.pdf', format = 'pdf')

	fig = doSadSadTrajectory(kappa, C0)
	plt.show()
	fig.savefig('../figures/SadSadPPlane.pdf', format = 'pdf')
	
# ======================================
# Execute if the script is run directly
# ======================================
if __name__ == "__main__":
	doPlots()

