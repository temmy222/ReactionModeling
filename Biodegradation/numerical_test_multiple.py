import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from Biodegradation.Substrate.Monod import Monod


def miucalc(umax, S, Ks):
    miuvalue = (umax * S) / (Ks + S)
    return miuvalue


def f(y, t, params):
    S, X = y
    umax, yieldmass, Ks = params
    miu = (umax * S) / (Ks + S)
    miuval = miucalc(umax, S, Ks)
    derivs = [-miuval / yieldmass * X,  # list of dy/dt=f functions
              miuval * X]
    return derivs


def mult(y, t, params):
    S_PCE, S_TCE, S_DCE, S_VC, X = y
    umax_PCE, umax_TCE, umax_DCE, umax_VC, Ks_PCE, Ks_TCE, Ks_DCE, Ks_VC, Kci_PCE, Kci_TCE, Kci_DCE, Khi_TCE, Khi_DCE, Khi_VC = params
    monod_PCE = Monod(umax_PCE, Ks_PCE, S_PCE)
    miu_PCE = monod_PCE.growth_rate()
    monod_TCE = Monod(umax_TCE, Ks_TCE, S_TCE)
    miu_TCE = monod_TCE.growth_rate(Kc=Kci_PCE)
    monod_DCE = Monod(umax_DCE, Ks_DCE, S_DCE)
    miu_DCE = monod_DCE.growth_rate(Kc=Kci_TCE)
    monod_VC_DCE = Monod(umax_VC, Ks_VC, S_VC)
    miu_VC_DCE = monod_DCE.growth_rate(Kc=Kci_DCE)

    derivs = [-miuval / yieldmass * X,  # list of dy/dt=f functions
              miuval * X]
    return derivs


# Parameters
umax = 0.86
Ks = 13.6
yieldmass = 4

# Initial values
S0 = 4400000.0  # initial substrate concentration
X0 = 100.0  # initial biomass concentration

# Bundle parameters for ODE solver
params = [umax, yieldmass, Ks]

# Bundle initial conditions for ODE solver
y0 = [S0, X0]

# Make time array for solution
tStop = 200.
tInc = 0.05
t = np.arange(0., tStop, tInc)

# Call the ODE solver
psoln = odeint(f, y0, t, args=(params,))

# Plot results
fig = plt.figure(1, figsize=(8, 8))

# Plot theta as a function of time
ax1 = fig.add_subplot(211)
ax1.plot(t, psoln[:, 0])
ax1.set_xlabel('time')
ax1.set_ylabel('substrate')

# Plot omega as a function of time
ax2 = fig.add_subplot(212)
ax2.plot(t, psoln[:, 1])
ax2.set_xlabel('time')
ax2.set_ylabel('biomass')

plt.tight_layout()
plt.show()
