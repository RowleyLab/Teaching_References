# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 08:40:09 2016

@author: matthewrowley1
"""

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

num_points = 1000

xvals = np.linspace(-1, 1, num_points)
stepsize = 2/num_points

sinx = np.sin(xvals) + 1/2
phi0 = np.ones_like(xvals)/np.sqrt(2)
phi1 = np.sqrt(3/2)*xvals
phi2 = np.sqrt(15/16)*(xvals**2 - 1/3)
phi3 = np.sqrt(175/8)*(xvals**3 - 3/5*xvals)

p0 = np.sum(sinx*phi0) * stepsize
p1 = np.sum(sinx*phi1) * stepsize
p2 = np.sum(sinx*phi2) * stepsize
p3 = np.sum(sinx*phi3) * stepsize

projection = p0*phi0 + p1*phi1 + p2*phi2 + p3*phi3

plt.figure()
plt.plot(xvals, sinx, label='sin(x) + 1/2', linewidth=2)
plt.plot(xvals, phi0, label = r'$\phi_0$ - p0 = {:3.2f}'.format(p0), linestyle='--', linewidth=4)
plt.plot(xvals, phi1, label = r'$\phi_1$ - p1 = {:3.2f}'.format(p1), linestyle='--', linewidth=4)
plt.plot(xvals, phi2, label = r'$\phi_2$ - p2 = {:3.2f}'.format(p2), linestyle='--', linewidth=4)
plt.plot(xvals, phi3, label = r'$\phi_3$ - p3 = {:3.2f}'.format(p3), linestyle='--', linewidth=4)
plt.plot(xvals, projection, label = 'Projection', linestyle='-.', linewidth=4, color='k')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc=4)
plt.show()

# Projecting onto a fourier series
xvals = np.linspace(-np.pi, np.pi, num_points)

f = xvals**2

num_cosines = 10
bases = []
bases.append(np.ones_like(xvals)*(1/3*np.pi**2))  # Our offset basis function
for i in range(1,num_cosines+1):  # Our cosine basis functions
    basis = (-1)**i*4/i**2 * np.cos(i*xvals)
    bases.append(basis)

series = []
for i in range(num_cosines+1):
    approximation = bases[0]
    for j in range(i):
        approximation = approximation + bases[j+1]
    series.append(approximation)

plt.figure()
plt.plot(xvals, series[1], label='1 cosine', linestyle='--', linewidth=4)
plt.plot(xvals, series[2], label='2 cosine', linestyle='--', linewidth=4)
plt.plot(xvals, series[3], label='3 cosines', linestyle='--', linewidth=4)
plt.plot(xvals, series[10], label='10 cosines', linestyle='--', linewidth=4)
plt.plot(xvals, f, label='f(y)',linewidth=2, color='k')
plt.xlabel('y')
plt.ylabel('f(y)')
plt.legend(loc=4)
plt.show()

# PIB linear variation solution
xvals = np.linspace(0, 1, num_points)
stepsize = 1/num_points

f = np.sqrt(2)*np.sin(np.pi*xvals)

phi0 = np.ones_like(xvals)
phi1 = np.sqrt(3/2)*xvals
phi2 = np.sqrt(15/16)*(xvals**2 - 1/3)
phi3 = np.sqrt(175/8)*(xvals**3 - 3/5*xvals)

p0 = np.sum(f*phi0) * stepsize
p1 = np.sum(f*phi1) * stepsize
p2 = np.sum(f*phi2) * stepsize
p3 = np.sum(f*phi3) * stepsize

projection = p0*phi0 + p1*phi1 + p2*phi2 + p3*phi3
