import os

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

inputs = ['Ag+2', 'Adamite', 'Ar(g)', 'F-']

print(aqu.getMolarMass(inputs[0]))
print(aqu.getListOfEquilibriumConstants(inputs[0]))
print(aqu.getEquilibriumConstantAtTemp(inputs[0], 25))
print(aqu.getNumberOfReactingSpecies(inputs[0]))
print(aqu.getReactants(inputs[0]))

# print(mine.getInitialMolarVolume(inputs[1]))
# print(mine.getMolarMass(inputs[1]))
#
# print(gaseous.getMolarMass(inputs[2]))
#
# print(bases.getMolarMass(inputs[3]))
# print(bases.getHydratedRadius(inputs[3]))
# print(bases.getElectricCharge(inputs[3]))
