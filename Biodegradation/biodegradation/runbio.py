# from win32com.client import Dispatch
#
# w = Dispatch('IPhreeqcCOM.Object')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style
import matplotlib as mpl
from scipy.integrate import odeint

mpl.style.use('classic')
number_of_points = 1000

max_biomass_growth_rate = 0.86
initial_sub_conc = 0.54
sub_values = np.linspace(0, 1000, number_of_points)
time = np.linspace(0.01, 10, number_of_points)
monod_constant = 13.8
initial_biomass_conc = 0.0007

death_rate = 0.18
yield_mass = 1.28


def all_data(number_of_points, max_biomass_growth_rate, monod_constant, initial_sub_conc, initial_biomass_conc,
             death_rate, yield_mass):
    sub_values = np.linspace(0, 1000, number_of_points)
    time = np.linspace(0.01, 10, number_of_points)
    utilization_rate = np.zeros(len(sub_values))
    inner_value = np.zeros(len(sub_values))
    biomass_conc = np.zeros(len(sub_values))
    sub_conc = np.zeros(len(sub_values))
    utilization_rate = max_biomass_growth_rate * (sub_values / (monod_constant + sub_values))
    inner_value = (utilization_rate - death_rate) * time
    biomass_conc = initial_biomass_conc * np.exp(inner_value)
    sub_conc = initial_sub_conc - (biomass_conc / yield_mass)
    return utilization_rate, biomass_conc, sub_conc


# utilization_rate = np.zeros(len(sub_conc))
# inner_value = np.zeros(len(sub_conc))
# biomass_conc = np.zeros(len(sub_conc))
# for i in range(0, len(sub_conc)):
#     utilization_rate[i] = (max_biomass_growth_rate * sub_conc[i]) / (michaelis_constant + sub_conc[i])
#     inner_value[i] = (utilization_rate[i] - death_rate) * time[i]
#     biomass_conc[i] = initial_biomass_conc * np.exp(inner_value[i])


# def dX_dt(inputt , t):
#     output = inputt[1] * inputt[0]
#     return output
#
#
# def dS_dt(S, X):
#     output = -1 / yield_mass * (max_biomass_growth_rate * S / monod_constant + S) * X
#     return output
#
# test=[0,0]
# x_sol = odeint(dX_dt, test, time)
# # sol = odeint(dS_dt, initial_sub_conc, biomass_conc)

util = []
biomass = []
substrate = []
death_rate = [0.18, 0.28, 0.38]
yield_mass = [1.00, 1.28, 1.58]
for i in range(len(death_rate)):
    utilization_rate, biomass_conc, sub_conc = all_data(number_of_points, max_biomass_growth_rate, monod_constant,
                                                        initial_sub_conc, initial_biomass_conc, death_rate[0],
                                                        yield_mass[i])
    util.append(utilization_rate)
    biomass.append(biomass_conc)
    substrate.append(sub_conc)

fig, axs = plt.subplots(1, 1)
axs.plot(sub_values, util[0], label=yield_mass[0])
axs.plot(sub_values, util[1], label=yield_mass[1])
axs.plot(sub_values, util[2], label=yield_mass[2])
axs.legend()
axs.set_title('Sensitivity to Yield', fontsize=24)
axs.set_xlabel("Substrate Concentration", fontsize=14)
axs.set_ylabel("Biomass Specific Growth Rate", fontsize=14)
plt.setp(axs.get_xticklabels(), fontsize=14)
plt.setp(axs.get_yticklabels(), fontsize=14)
plt.show()
fig.savefig('Monod' '.png', bbox_inches='tight', dpi=600)

fig, axs = plt.subplots(1, 1)
axs.plot(sub_values, biomass[0], label=yield_mass[0])
axs.plot(sub_values, biomass[1], label=yield_mass[1])
axs.plot(sub_values, biomass[2], label=yield_mass[2])
axs.legend()
axs.set_title('Sensitivity to Yield', fontsize=24)
axs.set_xlabel("Time (hours)", fontsize=14)
axs.set_ylabel("Biomass Concentration (mg)", fontsize=14)
plt.setp(axs.get_xticklabels(), fontsize=14)
plt.setp(axs.get_yticklabels(), fontsize=14)
plt.show()
fig.savefig('Biomass Conc' '.png', bbox_inches='tight', dpi=600)
#
fig, axs = plt.subplots(1, 1)
axs.plot(sub_values, substrate[0], label=yield_mass[0])
axs.plot(sub_values, substrate[1], label=yield_mass[1])
axs.plot(sub_values, substrate[2], label=yield_mass[2])
axs.legend()
axs.set_title('Sensitivity to Yield', fontsize=24)
axs.set_xlabel("Time (hours)", fontsize=14)
axs.set_ylabel("Substrate Concentration (mg)", fontsize=14)
plt.setp(axs.get_xticklabels(), fontsize=14)
plt.setp(axs.get_yticklabels(), fontsize=14)
plt.show()
fig.savefig('Substrate Conc' '.png', bbox_inches='tight', dpi=600)

# plt.figure()
# plt.plot(time, sol)
# plt.xlabel("Time")
# plt.ylabel("Substrate Concentration")
# plt.show()
