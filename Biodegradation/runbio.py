import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style
import matplotlib as mpl
from scipy.integrate import odeint

from Biodegradation.Biomass.BiomassBatch import BiomassBatch
from Biodegradation.Plotting.plotting import Plotting
from Biodegradation.Substrate.Monod import Monod
from Biodegradation.Substrate.SubstrateBatch import SubstrateBatch

mpl.style.use('classic')
number_of_points = 1000

max_biomass_growth_rate = 0.86
initial_sub_conc = 1000
sub_values = np.linspace(0, initial_sub_conc, number_of_points)
time = np.linspace(0.01, 10, number_of_points)
monod_constant = 13.8
initial_biomass_conc = 0.7

death_rate = 0.18
yield_mass = 1.28
plot = Plotting()

monod = Monod(max_biomass_growth_rate, monod_constant, sub_values)
biomass_growth = monod.growth_rate()
# plot.plotMonod(sub_values, biomass_growth, 'Biomass Specific Growth Rate')
#
# biomass = BiomassBatch(death_rate, initial_biomass_conc, time, biomass_growth)
# biomass_conc1 = biomass.biomass_concentration_analytical()
# biomass_conc2 = biomass.biomass_concentration_numerical()
# # plot.plotConcentration(time, biomass_conc1, 'Biomass Concentration')
# # plot.plotConcentration(time, biomass_conc2, 'Biomass Concentration')
# biomass_conc = [biomass_conc1, biomass_conc2]
# plot.plotConcentrationMultiOnSingle(time, biomass_conc, 'Biomass Concentration', ['analytical', 'numerical'])
#
# sub = SubstrateBatch(death_rate, initial_biomass_conc, initial_sub_conc, time, biomass_growth, yield_mass)
# sub_conc = sub.substrate_concentration_analytical()
# plot.plotConcentration(time, sub_conc, 'Substrate Concentration')
#
death_rates = [0, 0.28, 0.38]
death_rates_label = ["Death Rate of 0", "Death Rate of 0.28", "Death Rate of 0.38"]
biomass_death_multi = []
sub_death_multi = []

yield_masses = [1.00, 1.28, 1.58]
yield_rates_label = ["Yield Rate of 1.00", "Yield Rate of 1.28", "Yield Rate of 1.58"]
biomass_yield_multi = []
sub_yield_multi = []

monod_constants = [1.8, 13.8, 38.8]
monod_label = ["Monod Constant of 1.0", "Monod Constant of 13.8", "Monod Constant of 38.8"]
biomass_monod_multi = []
sub_monod_multi = []
biomass_growth_multi = []

max_biomass_growth_rates = [0.75, 0.86, 1.26]
max_biomass_label = ["max_biomass_growth_rate of 0.75", "max_biomass_growth_rate of 0.86",
                     "max_biomass_growth_rate of 1.26"]
max_biomass_multi = []
max_biomass_sub_multi = []
max_biomass_monod_multi = []

initial_biomass_concs = [0.07, 0.7, 7]
initial_biomass_conc_label = ["initial_biomass_conc of 0.07", "initial_biomass_conc of 0.7",
                              "initial_biomass_conc of 7"]
initial_biomass_conc_multi = []
initial_biomass_conc_sub_multi = []
initial_biomass_conc_monod_multi = []

initial_sub_concs = [100, 1000, 10000]
initial_substrate_conc_label = ["initial_substrate_conc of 0.07", "initial_substrate_conc of 0.7",
                                "initial_substrate_conc of 7"]

for i in range(len(initial_sub_concs)):
    sub_values = np.linspace(0, initial_sub_concs[i], number_of_points)
    initial_sub_conc = initial_sub_concs[i]
    monod = Monod(max_biomass_growth_rate, monod_constant, sub_values)
    biomass_growth = monod.growth_rate()
    max_biomass_monod_multi.append(biomass_growth)
    biomass = BiomassBatch(death_rate, initial_biomass_conc, time, biomass_growth)
    sub = SubstrateBatch(death_rate, initial_biomass_conc, initial_sub_conc, time, biomass_growth, yield_mass)
    sub_conc = sub.substrate_concentration_analytical()
    biomass_conc = biomass.biomass_concentration_analytical()
    max_biomass_multi.append(biomass_conc)
    max_biomass_sub_multi.append(sub_conc)

# for i in range(len(initial_biomass_concs)):
#     monod = Monod(max_biomass_growth_rate, monod_constant, sub_values)
#     biomass_growth = monod.growth_rate()
#     biomass = BiomassBatch(death_rate, initial_biomass_concs[i], time, biomass_growth)
#     sub = SubstrateBatch(death_rate, initial_biomass_concs[i], initial_sub_conc, time, biomass_growth, yield_mass)
#     sub_conc = sub.substrate_concentration_analytical()
#     biomass_conc = biomass.biomass_concentration_analytical()
#     initial_biomass_conc_multi.append(biomass_conc)
#     initial_biomass_conc_sub_multi.append(sub_conc)

# for i in range(len(death_rates)):
#     biomass = BiomassBatch(death_rates[i], initial_biomass_conc, time, biomass_growth)
#     sub = SubstrateBatch(death_rates[i], initial_biomass_conc, initial_sub_conc, time, biomass_growth, yield_mass)
#     sub_conc = sub.substrate_concentration_analytical()
#     biomass_conc = biomass.biomass_concentration_analytical()
#     biomass_death_multi.append(biomass_conc)
#     sub_death_multi.append(sub_conc)
#
# for i in range(len(yield_masses)):
#     sub = SubstrateBatch(death_rate, initial_biomass_conc, initial_sub_conc, time, biomass_growth, yield_masses[i])
#     sub_conc = sub.substrate_concentration_analytical()
#     sub_yield_multi.append(sub_conc)

# for i in range(len(max_biomass_growth_rates)):
#     monod = Monod(max_biomass_growth_rates[i], monod_constant, sub_values)
#     biomass_growth = monod.growth_rate()
#     max_biomass_monod_multi.append(biomass_growth)
#     biomass = BiomassBatch(death_rate, initial_biomass_conc, time, biomass_growth)
#     sub = SubstrateBatch(death_rate, initial_biomass_conc, initial_sub_conc, time, biomass_growth, yield_mass)
#     sub_conc = sub.substrate_concentration_analytical()
#     biomass_conc = biomass.biomass_concentration_analytical()
#     max_biomass_multi.append(biomass_conc)
#     max_biomass_sub_multi.append(sub_conc)

plot = Plotting()
plot.plotConcentrationMultiOnSingle(time, max_biomass_multi, 'Biomass Concentration',
                                    initial_substrate_conc_label,
                                    format="Biomass",
                                    title="Initial Substrate Concentration Sensitivity Plots")
plot.plotConcentrationMultiOnSingle(time, max_biomass_sub_multi, 'Substrate Concentration',
                                    initial_substrate_conc_label,
                                    format="Substrate",
                                    title="Initial Substrate Concentration Sensitivity Plots")
plot.plotConcentrationMultiOnSingle(sub_values, max_biomass_monod_multi, 'Biomass specific growth rate',
                                    initial_substrate_conc_label,
                                    format="Substrate",
                                    title="Initial Substrate Concentration Sensitivity Plots", filename='Monod')
