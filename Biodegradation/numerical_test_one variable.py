import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def f(y, t, params):
    derivs = params * y
    return derivs


def miu(umax, S, Ks):
    miuvalue = (umax * S) / (Ks + S)
    return miuvalue


S = 1000
umax = 0.86
Ks = 13.6

# Parameters
miuvalue = miu(umax, S, Ks)

# Initial values
X0 = 100.0  # initial biomass population

# Bundle parameters for ODE solver
params = [miuvalue]

# Bundle initial conditions for ODE solver
y0 = [X0]

# Make time array for solution
tStop = 2.
tInc = 0.1
t = np.arange(0., tStop, tInc)

# Call the ODE solver
psoln = odeint(f, y0, t, args=(params,))

# Plot results
fig = plt.figure(1, figsize=(8, 8))

# Plot theta as a function of time
ax1 = fig.add_subplot(111)
temp = psoln[:, 0]
ax1.plot(t, temp, 'bo', t, X0 * np.exp(miuvalue * t), 'r-')
ax1.set_xlabel('time')
ax1.set_ylabel('theta')
plt.show()
