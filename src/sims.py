#!/usr/bin/env python3
"""
We create two routines:
 - gel_buffer: Newton's method to identify the gel-buffer potential
 - bValues: identify the values of the state variable at the gel boundary
"""

# ======================================
# Packages
# ======================================
import numpy as np

# ======================================
# Gel Buffer Potential
# ======================================
def gel_buffer(kappa, C0):
	"""
	Solve the transcendental equation defining the gel buffer potential.
	"""

	def f(x):
		y = kappa/(kappa + np.exp(-x)) + 2*C0*np.sinh(x)
		return y
	
	def fp(x):
		y = kappa * (kappa + np.exp(-x))**(-2) * np.exp(-x) + 2*C0*np.cosh(x)
		return y
	
	tol, check = 1e-10, 1
	x0 = 0
	while check > tol:
		x = x0 - f(x0)/fp(x0)
		check = np.abs(f(x))
		x0 = x

	return x

# ======================================
# Boundary Values
# ======================================
def bValues(kappa, C0):
	"""
	Get the values of the state variables in the phase plane at the xi = 0 boundary
	"""
	
	phi = gel_buffer(kappa, C0)
	x0 = 2*C0*(np.cosh(phi) - 1)
	x0 = ( (np.exp(phi) + 1/kappa) * np.exp(x0) - 1/kappa)
	x0 = np.log(x0)
	y0 = -2*np.sqrt(C0*(np.cosh(x0) - 1))

	return x0, y0
