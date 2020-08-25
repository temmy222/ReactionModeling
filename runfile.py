import os

import numpy as np

from Preparation.MineralInput import MineralInput
from Preparation.ReadInput import ReadInput

dest1 = r"C:\Users\AJ\OneDrive - Louisiana State University\Second numerical paper\carbonate 2"
os.chdir(dest1)
filename = 'thddem1214r3_hs.dat'
chem_file = 'chemical.inp'

prep = MineralInput(dest1, chem_file, filename)
read = ReadInput(dest1, chem_file, filename)

block = read.readMineralBlock()

mineral_list = prep.getMinerals()
mineral_constituents = prep.getAllConstituentMineralSpecies()
mineral_line = prep.getMineralLine()
miss = prep.checkAllMineralInBasis()
kinetic = prep.determineKinetic()
precipitate = prep.determinePrecipitation()
dissolution = prep.determineDissolution()
diss_rate_constants = prep.getDissolutionRateConstants()
multi_mech = prep.getDissolutionMultipleMechanisms()
exponent = prep.getPrecipitationInitialVolumeFraction()


inputs = ['Ag+2', 'Adamite', 'Br2(g)', 'F-']

#
# print(bases.getMolarMass(inputs[3]))
# print(bases.getHydratedRadius(inputs[3]))
# print(bases.getElectricCharge(inputs[3]))
