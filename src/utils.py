#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from sims import gel_buffer, bValues
from fns import Hpos, Hneg
# ======================================
# Gel Buffer Potential Plots
# ======================================
def doGBplots(kap_range, C0):
	phi_range = np.zeros(len(kap_range))
	for kphi in range(len(kap_range)):
		kappa = kap_range[kphi]
		phi_range[kphi] = gel_buffer(kappa, C0)
	
	# --- Donnan Potential
	phi_D = - np.asinh(1/(2*C0))
	
	fig, ax = plt.subplots()
	ax.plot(kap_range, phi_range*25.8, label='Gel-Buffer Potential')	
	ax.plot(kap_range, phi_D*25.8*np.ones(len(kap_range)), '--r', label='Donnan Potential')
	ax.set(xlabel = r'$\kappa$', ylabel = 'Potential (mV)')
	ax.legend()
	return fig

# ======================================
# Solution Trajectory Plots
# ======================================
def doNegTrajectory(kappa, C0):
	phi = gel_buffer(kappa, C0)
	phi0, psi0 = bValues(kappa, C0)
	
	fig, ax = plt.subplots()
	x = np.linspace(phi0, 0, 2**8+1)
	y = np.linspace(psi0, -psi0, 2**8+1)
	X, Y = np.meshgrid(x, y)
	Zneg = Hneg(X, Y, C0)
	
	# --- Get the saddle
	levels = [0]
	CSneg = ax.contour(X, Y, Zneg, levels, colors=['black'], linestyles=['solid'])

	# --- Get other trajectories
	xvals = np.linspace(phi0/4, phi0, 4)
	levels = Hneg(xvals, 0, C0)
	levels = np.sort(levels)
	CSneg = ax.contour(X, Y, Zneg, levels, colors=['black'], linestyles=['solid'])

	# --- Turn the desired part of the saddle red
	levels = [0]
	y = np.linspace(psi0, 0, 2**8+1)
	X, Y = np.meshgrid(x, y)
	Zneg = Hneg(X, Y, C0)
	CSneg = ax.contour(X, Y, Zneg, levels, colors=['red'], linestyles=['solid'])
	
	# --- Plot the eq point
	ax.plot(0, 0, 'ok')
	ax.set(xlim = (phi0, 0.0001))
	ax.set_xticks(np.array([phi0, 0]), [r'$\Phi(0)$', r'$\Phi_{-\infty}$'])
	ax.set(xlabel=r'$\Phi$', ylabel=r'$\Psi$')
	ax.set_yticks(np.array([psi0, 0]), [r'$\Psi(0)$', 0])
	ax.set(title=r'Phase Plane, $\xi < 0$')
	return fig

def doPosTrajectory(kappa, C0):
	phi = gel_buffer(kappa, C0)
	phi0, psi0 = bValues(kappa, C0)

	fig, ax = plt.subplots()
	x = np.linspace(phi, phi0, 2**8+1)
	y = np.linspace(psi0, -psi0, 2**8+1)
	X, Y = np.meshgrid(x, y)
	Zpos = Hpos(X, Y, kappa, C0)
	
	# --- Get the saddle
	levels = [0]
	CSpos = ax.contour(X, Y, Zpos, levels, colors=['black'], linestyles=['solid'])

	# --- Get other trajectories
	xvals = np.linspace(phi, 5*phi0/4, 4)
	levels = Hpos(xvals, 0, kappa, C0)
	levels = np.sort(levels)
	CSpos = ax.contour(X, Y, Zpos, levels, colors=['black'], linestyles=['solid'])

	# --- Turn the desired part of the saddle red
	levels = [0]
	y = np.linspace(psi0, 0, 2**8+1)
	X, Y = np.meshgrid(x, y)
	Zpos = Hpos(X, Y, kappa, C0)
	CSpos = ax.contour(X, Y, Zpos, levels, colors=['red'], linestyles=['solid'])
	
	# --- Plot the eq point
	ax.plot(phi, 0, 'ok')
	ax.set(xlim = (-0.0041, phi0))
	ax.set_xticks(np.array([phi, phi0]), [r'$\Phi_{\infty}$', r'$\Phi(0)$'])
	ax.set_yticks(np.array([psi0, 0]), [r'$\Psi(0)$', 0])
	ax.set(xlabel=r'$\Phi$', ylabel=r'$\Psi$')
	ax.set(title=r'Phase Plane, $\xi > 0$')
	return fig

def doSadSadTrajectory(kappa, C0):
	phi = gel_buffer(kappa, C0)
	
	phi0, psi0 = bValues(kappa, C0)

	fig, ax = plt.subplots()

	# --- Surrounding trajectories
	x = np.linspace(1.1*phi, phi, 2**8+1)
	y = np.linspace(psi0, -psi0, 2**8+1)
	X, Y = np.meshgrid(x, y)
	Zpos = Hpos(X, Y, kappa, C0)
	CSsadsad = ax.contour(X, Y, Zpos, [0], colors=['black'], linestyles=['solid'])
	
	x = np.linspace(0, -.1*phi, 2**8+1)
	X, Y = np.meshgrid(x, y)
	Zneg = Hneg(X, Y, C0)
	CSsadsad = ax.contour(X, Y, Zneg, [0], colors=['black'], linestyles=['solid'])

	# --- Unstable manifold for xi < 0
	x = np.linspace(phi0, 0, 2**8+1)
	y = np.linspace(psi0, 0, 2**8+1)
	X, Y = np.meshgrid(x, y)
	Zneg = Hneg(X, Y, C0)
	CSsadsad = ax.contour(X, Y, Zneg, [0], colors=['red'], linestyles=['solid'])

	# --- Stable manifold for xi > 0
	x = np.linspace(phi, phi0, 2**8+1)
	y = np.linspace(psi0, 0, 2**8+1)
	X, Y = np.meshgrid(x, y)
	Zpos = Hpos(X, Y, kappa, C0)
	CSsadsad = ax.contour(X, Y, Zpos, [0], colors=['red'], linestyles=['solid'])
	
	
	ax.plot([0, phi], [0, 0], 'ok')
	ax.set_xticks([0, phi0, phi], [r'$\Phi_{-\infty}$', r'$\Phi(0)$', r'$\Phi_{\infty}$'])
	ax.set_yticks([0, psi0], [0, r'$\Psi(0)$'])
	ax.set(xlabel=r'$\Phi$', ylabel=r'$\Psi$')
	ax.set(title='Saddle-Saddle Connection')
	
	
	return fig

