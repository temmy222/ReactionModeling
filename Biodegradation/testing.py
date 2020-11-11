import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from Biodegradation.Substrate.Monod import Monod
from Biodegradation.Substrate.inhibition import Inhibition
from Biodegradation.Substrate.solution import Solution
from Biodegradation.Substrate.substrate import Component

c_pce = Component(0.2, 'PCE', 0.86, 13.6, 4.5, 5.7)
c_tce = Component(0.29, 'TCE', 0.86, 33.6, 4.5, 5.7)
c_dce = Component(0.2, 'DCE', 0.86, 23.6, 6.5, 5.7)
c_vc = Component(0.2, 'VC', 1.86, 13.6, 6.5, 5.7)
c_eth = Component(0.2, 'VC', 1.86, 13.6, 6.5, 5.7)

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
    c_pce = Component(S_PCE, 'PCE', umax_PCE, Ks_PCE, Kci_PCE)
    c_tce = Component(S_TCE, 'TCE', umax_TCE, Ks_TCE, Kci_TCE, Khi_TCE)
    c_dce = Component(S_DCE, 'DCE', umax_DCE, Ks_DCE, Kci_DCE, Khi_DCE)
    c_vc = Component(S_VC, 'VC', umax_VC, Ks_VC, None, Khi_VC)
    c_eth = Component(S_ETH, 'VC', umax_ETH, Ks_ETH)
    all_comp = [c_pce, c_tce, c_tce, c_vc, c_eth]
    iscompetiting = [{c_pce: []}, {c_tce: [c_pce]}, {c_dce: [c_tce]}, {c_vc: [c_tce, c_dce]}]
    ishaldane = [{c_pce: []}, {c_tce: [c_tce]}, {c_dce: [c_dce]}, {c_vc: [c_vc]}]
    soln = Solution(all_comp, iscompetiting, ishaldane)
    inhibit = Inhibition(soln)
    monod_PCE = Monod().growth_rate_new(c_pce, inhibit)
    monod_DCE = Monod().growth_rate_new(c_dce, inhibit)
    monod_TCE = Monod().growth_rate_new(c_tce, inhibit)
    monod_VC = Monod().growth_rate_new(c_vc, inhibit)
    derivs = [-monod_PCE * X,
              -monod_TCE * X + monod_PCE * X,
              -monod_DCE * X + monod_TCE * X,
              -monod_VC * X + monod_DCE * X,
              monod_VC * X,
              yieldmass * S_all - death_rate * X
              ]
    return derivs


S_PCE_init = 92
S_TCE_init = 0
S_DCE_init = 0
S_VC_init = 0
S_ETH_init = 0
X_init = 13
y0 = [S_PCE_init, S_TCE_init, S_DCE_init, S_VC_init, S_ETH_init, X_init]
umax_PCE = 13.3
umax_TCE = 124
umax_DCE = 22
umax_VC = 2.44
umax_ETH = 1
Ks_PCE = 3.86
Ks_TCE = 2.76
Ks_DCE = 1.9
Ks_VC = 602
Ks_ETH = 1
Kci_PCE = 3.86
Kci_TCE = 2.76
Kci_DCE = 1.90
Khi_TCE = 900
Khi_DCE = 6000
Khi_VC = 7000
yieldmass = 0.006
death_rate = 0.024

params = [umax_PCE, umax_TCE, umax_DCE, umax_VC, umax_ETH, Ks_PCE, Ks_TCE, Ks_DCE, Ks_VC, Ks_ETH, Kci_PCE, Kci_TCE,
          Kci_DCE, Khi_TCE, Khi_DCE, Khi_VC, yieldmass, death_rate]

tStop = 1.2
tInc = 0.01
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
