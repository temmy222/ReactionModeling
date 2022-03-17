import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from Biodegradation.Biomass.biomass import Biomass
from Biodegradation.Solver.Solver import Solver
from Biodegradation.Substrate.Monod import Monod
from Biodegradation.Substrate.inhibition import Inhibition
from Biodegradation.Substrate.solution import Solution
from Biodegradation.Substrate.substrate import Component

c_pce = Component(1, 0.2, 'PCE', 0.86, 13.6, 4.5, 5.7)
c_tce = Component(2, 0.29, 'TCE', 0.86, 33.6, 4.5, 5.7)
c_dce = Component(3, 0.2, 'DCE', 0.86, 23.6, 6.5, 5.7)
c_vc = Component(4, 0.2, 'VC', 1.86, 13.6, 6.5, 5.7)
c_eth = Component(5, 0.2, 'VC', 1.86, 13.6, 6.5, 5.7)

biomass = Biomass(40, 0.024, 1.2)

all_comp = [c_pce, c_tce, c_tce, c_vc]

iscompetiting = [{c_pce: []}, {c_tce: [c_pce]}, {c_dce: [c_tce]}, {c_vc: [c_tce, c_dce]}]
ishaldane = [{c_pce: []}, {c_tce: [c_tce]}, {c_dce: [c_dce]}, {c_vc: [c_vc]}]

react_to_react = [{c_pce: [c_pce]}, {c_tce: [c_tce]}, {c_dce: [c_dce]}, {c_vc: [c_vc]}, {c_eth: []}]
react_to_product = [{c_pce: []}, {c_tce: [c_pce]}, {c_dce: [c_tce]}, {c_vc: [c_dce]}, {c_eth: [c_vc]}]

soln = Solution(all_comp, iscompetiting, ishaldane)
# temp = list(iscompetiting[0].keys())
# print(temp[0])
inhibit = Inhibition(soln)
inhibit_TCE = inhibit.computeCompetitiveInhibition(c_tce) + inhibit.computeHaldaneInhibition(c_tce)
monod_TCE = Monod().growth_rate_new(c_tce, inhibit)


def mult_five(y, t, params):
    S_PCE, S_TCE, S_DCE, S_VC, S_ETH, X = y
    umax_PCE, umax_TCE, umax_DCE, umax_VC, umax_ETH, Ks_PCE, Ks_TCE, Ks_DCE, Ks_VC, Ks_ETH, Kci_PCE, Kci_TCE, Kci_DCE, Khi_TCE, Khi_DCE, Khi_VC, yieldmass, death_rate = params
    S_all = S_PCE + S_TCE + S_DCE + S_VC + S_ETH
    c_pce = Component(1, S_PCE, 'PCE', umax_PCE, Ks_PCE, Kci_PCE)
    c_tce = Component(2, S_TCE, 'TCE', umax_TCE, Ks_TCE, Kci_TCE, Khi_TCE)
    c_dce = Component(3, S_DCE, 'DCE', umax_DCE, Ks_DCE, Kci_DCE, Khi_DCE)
    c_vc = Component(4, S_VC, 'VC', umax_VC, Ks_VC, None, Khi_VC)
    c_eth = Component(5, S_ETH, 'VC', umax_ETH, Ks_ETH)
    all_comp = [c_pce, c_tce, c_dce, c_vc, c_eth]
    iscompetiting = [{c_pce: []}, {c_tce: [c_pce]}, {c_dce: [c_tce]}, {c_vc: [c_tce, c_dce]}]
    ishaldane = [{c_pce: []}, {c_tce: [c_tce]}, {c_dce: [c_dce]}, {c_vc: []}]
    soln = Solution(all_comp, iscompetiting, ishaldane)
    inhibit = Inhibition(soln)
    monod_PCE = Monod().growth_rate_new(c_pce, inhibit)
    monod_TCE = Monod().growth_rate_new(c_tce, inhibit)
    monod_DCE = Monod().growth_rate_new(c_dce, inhibit)
    monod_VC = Monod().growth_rate_new(c_vc, inhibit)
    derivs = [-monod_PCE * X,
              -monod_TCE * X + monod_PCE * X,
              -monod_DCE * X + monod_TCE * X,
              -monod_VC * X + monod_DCE * X,
              monod_VC * X,
              yieldmass * S_all - death_rate * X
              ]
    # derivs = [-monod_PCE * X,
    #               -monod_TCE * X,
    #               -monod_DCE * X,
    #               -monod_VC * X,
    #               monod_VC * X + monod_PCE * X + monod_TCE * X + monod_DCE * X,
    #               yieldmass * S_all - death_rate * X
    #               ]

    # print(monod_PCE, monod_TCE, monod_DCE, monod_VC)
    return derivs


S_PCE_init = 282
S_TCE_init = 0
S_DCE_init = 0
S_VC_init = 0
S_ETH_init = 0
X_init = 40
y0 = [S_PCE_init, S_TCE_init, S_DCE_init, S_VC_init, S_ETH_init, X_init]
umax_PCE = 12.4
umax_TCE = 125
umax_DCE = 13.8
umax_VC = 8.08
umax_ETH = 1
Ks_PCE = 1.63
Ks_TCE = 1.80
Ks_DCE = 1.76
Ks_VC = 62.6
Ks_ETH = 1
Kci_PCE = 1.63
Kci_TCE = 1.80
Kci_DCE = 1.76
Khi_TCE = 900
Khi_DCE = 750
Khi_VC = 0.750
yieldmass = 0.006
death_rate = 0.024

params = [umax_PCE, umax_TCE, umax_DCE, umax_VC, umax_ETH, Ks_PCE, Ks_TCE, Ks_DCE, Ks_VC, Ks_ETH, Kci_PCE, Kci_TCE,
          Kci_DCE, Khi_TCE, Khi_DCE, Khi_VC, yieldmass, death_rate]

tStop = 6
tInc = 0.001
t = np.arange(0., tStop, tInc)

psoln = odeint(mult_five, y0, t, args=(params,))

fig = plt.figure(1, figsize=(8, 8))

# Plot theta as a function of time
fig, ax1 = plt.subplots()
soln_PCE = psoln[:, 0]
soln_TCE = psoln[:, 1]
soln_DCE = psoln[:, 2]
soln_VC = psoln[:, 3]
soln_ETH = psoln[:, 4]
soln_X = psoln[:, 5]
big_T = t.reshape((len(t),1))
# ax1.plot(t, soln_PCE,'r--', label='PCE', marker = 'D',markevery=500, markersize=5)
ax1.plot(t, soln_PCE, label='PCE')
ax1.plot(t, soln_TCE,  label='TCE')
ax1.plot(t, soln_DCE, label='DCE')
ax1.plot(t, soln_VC, label='VC')
ax1.plot(t, soln_ETH, label='ETH')
ax1.plot(t, soln_X, label='X')
ax1.set_xlabel('Time (days)')
ax1.set_ylabel('Concentration ($\mu M$)')
plt.legend(loc="upper right")
fig.savefig('PCE_validation.png', bbox_inches='tight', dpi=600)

plt.show()

# fig, ax2 = plt.subplots()
# ax2.plot(t, soln_X, label='X')
# ax2.set_xlabel('time')
# ax2.set_ylabel('concentration')
# plt.legend(loc="upper right")
#
# plt.show()

# import itertools
#
# a = [['a', 'b'], ['c']]
# print(list(itertools.chain.from_iterable(a)))
# solve = Solver(all_comp, biomass, iscompetiting, ishaldane, None, react_to_react, react_to_product)
# solve.getProducts(c_eth)
