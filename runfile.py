import os

import autograd as ag
import autograd.numpy as np
import scipy.sparse as sps
from scipy import linalg, sparse
from scipy.sparse.linalg import gmres
from scipy.sparse.linalg import spsolve
from autograd import jacobian

from Parameters.aqueous import Aqueous
from Preparation.MineralInput import MineralInput
from Preparation.MineralKineticInput import MineralKineticInput
from Preparation.ReadInput import ReadInput
from Preparation.WaterInput import WaterInput
from Solver.preparation import Preparation
from ad.forward_mode import Ad_array

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
    output = x1 ** 2 + 4 * x2 ** 2 - 2
    return output


def f2(x1, x2):
    output = x1 ** 2 + 4 * x2 ** 2 - 2
    return output


def f3(x, y):
    output = np.array([x[0] ** 2, x[1] + y[1]])
    return output


def f4(x, rhs, coeff1, coeff2, power1, power2):
    output = np.array([coeff1[0] * x[0] ** power1[0] + (coeff2[0] * x[1] ** power2[0]) - rhs[0], coeff1[1] * x[0] ** power1[1] + coeff2[1] * x[1] ** power2[1] - rhs[1]])
    return output


# f = lambda x, y: np.array([x[0] ** 2, x[0] + y[0]])
# jacobian_f = jacobian(f3)(x1, y1)
# print(jacobian_f(np.array([1., 1.])))

def f(x, A):
    return np.array([A * x[0] ** 2, x[1] ** 3, x[2] ** 2])


guess = np.array([1, 2], dtype=float)
rhs = np.array([-2, 0], dtype=float)
coeff1 = np.array([3, 2], dtype=float)
coeff2 = np.array([-1, -1], dtype=float)
power1 = np.array([1, 2], dtype=float)
power2 = np.array([1, 1], dtype=float)

# x = np.array([3, 11, 5], dtype=float)
# A = float(5)
# jac = ag.jacobian(f)(x, A)
# print(f(x, A))
# print(jac)
# timeline = np.linspace(1, 100, 4)
# ag.jacobian(f)(np.array([1.0, 1.0]))

# jac2 = ag.jacobian(f4)(guess, rhs)
# left_side = jac2
# print(left_side)
# try_sparse = sparse.csr_matrix(left_side)
# right_side = -f4(guess)
# print(f4(guess))
# print(jac2)
# x = linalg.solve(left_side, right_side)

newton_tol = 1e-6
err = np.inf
iteration_count = 0
while err > newton_tol:
    val = -f4(guess, rhs, coeff1, coeff2, power1, power2)
    iteration_count = iteration_count + 1
    jac = ag.jacobian(f4)(guess, rhs, coeff1, coeff2, power1, power2)
    jac = sparse.csr_matrix(jac)
    dx = spsolve(jac, val)
    guess = guess + dx
    print(err)
    err = np.sqrt(np.sum(val ** 2))

# allspecies = aqueous.getAllAqueousComplexes()
#
# basis = prep.getAllAqueousComplexesInWater()

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
