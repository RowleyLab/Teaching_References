# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 17:25:47 2016

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

def BBCurve(nu, T):

    return 2*h*nu**3 / (c**2 * (np.exp(h*nu/(k*T))-1))

def Classical(l, T):
    l = l/1e9
    return 2*c*k*T/l**4

def BBCurve(l, T):
    l = l/1e9
    return 2*pi*c**2*h / l**5 / (np.exp(h*c/(l*k*T)) - 1)

frequencies = np.linspace(10, 3000, 400)

K3000 = BBCurve(frequencies, 3000)
K3500 = BBCurve(frequencies, 3500)
K4000 = BBCurve(frequencies, 4000)
K4500 = BBCurve(frequencies, 4500)
classical = Classical(frequencies, 3000)

plt.figure()
plt.plot(frequencies, K3000, linewidth=2, label='Experiment - 3000 K')
plt.plot(frequencies, K3500, linewidth=2, label='Experiment - 3500 K')
plt.plot(frequencies, K4000, linewidth=2, label='Experiment - 4000 K')
plt.plot(frequencies, K4500, linewidth=2, label='Experiment - 4500 K')
plt.plot(frequencies, classical, linewidth=2, linestyle='--', label='Classical Curve - 3000 K')
plt.legend()
plt.ylim(0,2.5e13)
plt.xlabel('$\lambda (nm)$')
plt.ylabel('$Radiance (Jm^{-2}sr^{-1})$')
plt.title('Blackbody Emission')