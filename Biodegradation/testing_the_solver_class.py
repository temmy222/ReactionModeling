import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from Biodegradation.Biomass.biomass import Biomass
from Biodegradation.Solver.Solver import Solver
from Biodegradation.Substrate.Monod import Monod
from Biodegradation.Substrate.inhibition import Inhibition
from Biodegradation.Substrate.solution import Solution
from Biodegradation.Substrate.substrate import Component

c_pce = Component(1, 92, 'PCE', 13.3, 3.86, 3.86, None, None)
c_tce = Component(2, 0, 'TCE', 124, 2.76, 2.76, 900, None)
c_dce = Component(3, 0, 'DCE', 22, 1.9, 1.9, 6000, None)
c_vc = Component(4, 0, 'VC', 2.44, 602, None, 7000, None)
c_eth = Component(5, 0, 'ETH', 1, 1, None, 6.5, None, None)

all_components = [c_pce, c_tce, c_dce, c_vc, c_eth]

iscompetiting = [{c_pce: []}, {c_tce: [c_pce]}, {c_dce: [c_tce]}, {c_vc: [c_tce, c_dce]}]
ishaldane = [{c_pce: []}, {c_tce: [c_tce]}, {c_dce: [c_dce]}, {c_vc: [c_vc]}]

react_to_react = [{c_pce: [c_pce]}, {c_tce: [c_tce]}, {c_dce: [c_dce]}, {c_vc: [c_vc]}, {c_eth: []}]
react_to_product = [{c_pce: []}, {c_tce: [c_pce]}, {c_dce: [c_tce]}, {c_vc: [c_dce]}, {c_eth: [c_vc]}]

biomass = Biomass(40, 0.024, 0.006)
biomasses = [biomass]
solver_class = Solver(all_components, biomasses, iscompetiting, ishaldane, None, react_to_react, react_to_product)

tStop = 6
tInc = 0.01

soln = solver_class.solve(6, 0.01)
