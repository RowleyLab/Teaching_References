# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 16:39:44 2016

@author: matt
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constants
h = constants.h
k = constants.k
c = constants.c
pi = constants.pi
r = constants.gas_constant

xvals = np.linspace(0,10,200)

def curve(xvals, x0):
    e = xvals - x0
    for i, val in enumerate(e):
        if val < 0:
            e[i]=0
    return e
Rb = curve(xvals, 2)
K = curve(xvals, 4)
Na = curve(xvals, 6)

plt.figure()
plt.plot(xvals, Na, label='Na', linewidth=2)
plt.plot(xvals, K, label='K', linewidth=2)
plt.plot(xvals, Rb, label='Rb', linewidth=2)
plt.ylabel(r'$e^-$ Kinetic Energy')
plt.xlabel(r'Incident Light Frequency $\nu$')
plt.annotate(r'$\nu_o^{Na}$', fontsize=16, xy=(2, 0), xytext=(5.8, -.5))
plt.annotate(r'$\nu_o^{K}$', fontsize=16, xy=(2, 0), xytext=(3.8, -.5))
plt.annotate(r'$\nu_o^{Rb}$', fontsize=16, xy=(2, 0), xytext=(1.8, -.5))
plt.legend(loc=2)
frame=plt.gca()
plt.ylim(-1,8)
frame.axes.get_xaxis().set_ticks([])
frame.axes.get_yaxis().set_ticks([0])
