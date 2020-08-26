import os

import numpy as np

from Parameters.aqueous import Aqueous
from Preparation.MineralInput import MineralInput
from Preparation.MineralKineticInput import MineralKineticInput
from Preparation.ReadInput import ReadInput
from Preparation.WaterInput import WaterInput
from Solver.preparation import Preparation

dest1 = r"C:\Users\AJ\OneDrive - Louisiana State University\Second numerical paper\carbonate 2"
os.chdir(dest1)
filename = 'thddem1214r3_hs.dat'
chem_file = 'chemical.inp'

kinetic_input = MineralKineticInput(dest1, chem_file, filename)
read = ReadInput(dest1, chem_file, filename)
water = WaterInput(dest1, chem_file, filename)
mineral_input = MineralInput(dest1, chem_file, filename)
prep = Preparation(dest1, chem_file, filename)
aqueous = Aqueous(dest1, filename)


def f1(x1, x2):
    output = x1 + 2 * x2 - 2
    return output


def f2(x1, x2):
    output = x1 ** 2 + 4 * x2 ** 2 - 2
    return output


allspecies = aqueous.getAllAqueousComplexes()

basis = prep.getAllAqueousComplexesInWater()

# block = read.readWaterData()
#
# water_species = water.getWaterSpecies()
# flag_it = water.checkAllWaterInBasis()
# water_comp = water.getWaterNRGuess()
# pH = water.determinePH()
#
# output = mineral_input.getMinerals()
# compare = mineral_input.compareKineticToInput()

# mineral_list = kinetic_input.getMinerals()
# mineral_constituents = kinetic_input.getAllConstituentMineralSpecies()
# mineral_line = kinetic_input.getMineralLine()
# miss = kinetic_input.checkAllMineralInBasis()
# kinetic = kinetic_input.determineKinetic()
# precipitate = kinetic_input.determinePrecipitation()
# dissolution = kinetic_input.determineDissolution()
# diss_rate_constants = kinetic_input.getDissolutionRateConstants()
# multi_mech = kinetic_input.getDissolutionMultipleMechanisms()
# exponent = kinetic_input.getPrecipitationInitialVolumeFraction()


inputs = ['Ag+2', 'Adamite', 'Br2(g)', 'F-']

#
# print(bases.getMolarMass(inputs[3]))
# print(bases.getHydratedRadius(inputs[3]))
# print(bases.getElectricCharge(inputs[3]))
