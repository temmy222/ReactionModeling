import os

import numpy as np

from Functions.Activity import Activity
from Parameters.aqueous import Aqueous
from Parameters.basis import Basis
from Parameters.gases import Gases
from Parameters.mineral import Mineral
from Solver.preparation import Preparation

dest1 = r"C:\Users\AJ\OneDrive - Louisiana State University\Second numerical paper\carbonate"
os.chdir(dest1)
filename = 'thddem1214r3_hs.dat'
chem_file = 'chemical.inp'

aqu = Aqueous(dest1, filename)
mine = Mineral(dest1, filename)
gaseous = Gases(dest1, filename)
bases = Basis(dest1, filename)


input_file = Preparation(dest1, chem_file)
listt = input_file.readMineralBlock()

inputs = ['Ag+2', 'Adamite', 'Br2(g)', 'F-']



species = mine.getReactants(inputs[1])

#
# print(bases.getMolarMass(inputs[3]))
# print(bases.getHydratedRadius(inputs[3]))
# print(bases.getElectricCharge(inputs[3]))
