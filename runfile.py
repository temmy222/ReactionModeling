import os

import numpy as np

from Functions.Activity import Activity
from Parameters.aqueous import Aqueous
from Parameters.basis import Basis
from Parameters.gases import Gases
from Parameters.mineral import Mineral

dest1 = r"C:\Users\AJ\OneDrive - Louisiana State University\Validation\Cement-Anhydrite"
os.chdir(dest1)
filename = 'thddem1214r3_hs.dat'

aqu = Aqueous(dest1, filename)
mine = Mineral(dest1, filename)
gaseous = Gases(dest1, filename)
bases = Basis(dest1, filename)

inputs = ['Ag+2', 'Adamite', 'Br2(g)', 'F-']

arr1 = np.array([0.008, 0.005, 0.029])
arr2 = np.array([3, 1, 1])
first = arr1[0]

calc = Activity(arr1, arr2)
ionic_strength = calc.ionicStrength()
acti = calc.acDebyeHuckel(0, 0.001)

man1 = -1824000 / ((79 * 298) ** 1.5)

#
# print(bases.getMolarMass(inputs[3]))
# print(bases.getHydratedRadius(inputs[3]))
# print(bases.getElectricCharge(inputs[3]))
