#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 23:11:32 2019

@author: matt
"""
from builtins import input
from numpy import random

C = int(eval(input("How many C atoms in the formula? ")))
H = int(eval(input("How many H atoms in the formula? ")))
O = int(eval(input("How many O atoms in the formula? ")))

mass = float(eval(input("What is the unknown mass? (0 for random) ")))

if mass == 0:
    mass = random.rand() * 5.0

M_H2O = 15.9994 + 2 * 1.00794
M_CO2 = 12.011 + 2 * 15.9994

M = 12.011 * C + 15.9994 * O + 1.00794 * H
Comp_C = 12.011 * C / M
Comp_O = 15.9994 * O / M
Comp_H = 1.00794 * H / M

mass_CO2 = mass * Comp_C * (M_CO2 / 12.011)
mass_H2O = mass * Comp_H * (M_H2O / 1.00794 / 2)

print("Unknown Formula: C{}H{}O{}".format(C, H, O))
print("Unknown mass: {}".format(mass))
print("CO2 mass: {}".format(mass_CO2))
print("H2O mass: {}".format(mass_H2O))
print("Unknown Molar Mass: {}".format(M))
