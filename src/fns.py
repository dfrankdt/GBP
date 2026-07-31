#!/usr/bin/env python3
"""
We define the Hamiltonian functions that are used for plotting level curves.
"""

# ======================================
# Packages
# ======================================
import numpy as np
from sims import gel_buffer

# ======================================
# Hamiltonian (xi < 0)
# ======================================
def Hneg(x, y, C0):
	z = 1/2*y**2 - 2*C0*(np.cosh(x) - 1)

	return z
	
# ======================================
# Hamiltonian (xi > 0)
# ======================================
def Hpos(x, y, kappa, C0):
	phi = gel_buffer(kappa, C0)
	z = 1/2*y**2
	z = z - 2*C0*(np.cosh(x) - np.cosh(phi))
	z = z + np.log( (kappa*np.exp(phi) + 1) / (kappa*np.exp(x) + 1) )

	return z
