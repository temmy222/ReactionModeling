import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from Biodegradation.Biomass.biomass import Biomass
from Biodegradation.Solver.Solver import Solver
from Biodegradation.Substrate.Monod import Monod
from Biodegradation.Substrate.inhibition import Inhibition
from Biodegradation.Substrate.solution import Solution
from Biodegradation.Substrate.substrate import Component

c_pce = Component(1, 282, 'PCE', 12.4, 1.63, 1.63, None, None)
c_tce = Component(2, 0, 'TCE', 125, 1.80, 1.80, 900, None)
c_dce = Component(3, 0, 'DCE', 13.8, 1.76, 1.76, 750, None)
c_vc = Component(4, 0, 'VC', 8.08, 62.6, None, 750, None)
c_eth = Component(5, 0, 'ETH', 1, 1, None, None, None, None)

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
t = np.arange(0., tStop, tInc)


soln = Solution(all_components, iscompetiting, ishaldane)
inhibit = Inhibition(soln)



monod_PCE = Monod().growth_rate_new(c_pce, inhibit)
monod_DCE = Monod().growth_rate_new(c_dce, inhibit)
monod_TCE = Monod().growth_rate_new(c_tce, inhibit)
monod_VC = Monod().growth_rate_new(c_vc, inhibit)
monod_ETH = Monod().growth_rate_new(c_eth, inhibit)

# print(-monod_VC * biomass.init_conc + monod_DCE * biomass.init_conc)
# print(solver_class.computeDerivative(solver_class.getReactants(c_vc), solver_class.getProducts(c_vc), all_components, biomass.init_conc))






psoln = solver_class.solve(6, 0.01)

fig, ax1 = plt.subplots()
soln_PCE = psoln[:, 0]
soln_TCE = psoln[:, 1]
soln_DCE = psoln[:, 2]
soln_VC = psoln[:, 3]
soln_ETH = psoln[:, 4]
soln_X = psoln[:, 5]
ax1.plot(t, soln_PCE, label='PCE')
ax1.plot(t, soln_TCE, label='TCE')
ax1.plot(t, soln_DCE, label='DCE')
ax1.plot(t, soln_VC, label='VC')
ax1.plot(t, soln_ETH, label='ETH')
ax1.plot(t, soln_X, label='X')
ax1.set_xlabel('time')
ax1.set_ylabel('concentration')
plt.legend(loc="upper right")

plt.show()
