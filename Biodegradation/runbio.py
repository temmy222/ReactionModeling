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
initial_sub_conc = 0.54
sub_values = np.linspace(0, 1000, number_of_points)
time = np.linspace(0.01, 10, number_of_points)
monod_constant = 13.8
initial_biomass_conc = 0.0007

death_rate = 0.18
yield_mass = 1.28

monod = Monod(max_biomass_growth_rate, monod_constant, sub_values)
biomass_growth = monod.growth_rate()
# plot = Plotting()
# plot.plotMonod(sub_values, biomass_growth, 'Biomass Specific Growth Rate')

biomass = BiomassBatch(death_rate, initial_biomass_conc, time, biomass_growth)
biomass_conc = biomass.biomass_concentration_analytical()
# plot = Plotting()
# plot.plotConcentration(time, biomass_conc, 'Biomass Concentration')

sub = SubstrateBatch(death_rate, initial_biomass_conc, initial_sub_conc, time, biomass_growth, yield_mass)
sub_conc = sub.substrate_concentration_analytical()
# plot = Plotting()
# plot.plotConcentration(time, sub_conc, 'Substrate Concentration')

death_rates = [0.18, 0.28, 0.38]
death_rates_label = ["Death Rate of 0.18", "Death Rate of 0.28", "Death Rate of 0.38"]
yield_masses = [1.00, 1.28, 1.58]
yield_rates_label = ["Yield Rate of 1.00", "Yield Rate of 1.28", "Yield Rate of 1.58"]

biomass_death_multi = []
sub_death_multi = []

biomass_yield_multi = []
sub_yield_multi = []
for i in range(len(death_rates)):
    biomass = BiomassBatch(death_rates[i], initial_biomass_conc, time, biomass_growth)
    sub = SubstrateBatch(death_rates[i], initial_biomass_conc, initial_sub_conc, time, biomass_growth, yield_mass)
    sub_conc = sub.substrate_concentration_analytical()
    biomass_conc = biomass.biomass_concentration_analytical()
    biomass_death_multi.append(biomass_conc)
    sub_death_multi.append(sub_conc)

for i in range(len(yield_masses)):
    sub = SubstrateBatch(death_rate, initial_biomass_conc, initial_sub_conc, time, biomass_growth, yield_masses[i])
    sub_conc = sub.substrate_concentration_analytical()
    sub_yield_multi.append(sub_conc)

plot = Plotting()
plot.plotConcentrationMultiOnSingle(time, biomass_death_multi, 'Biomass Concentration', death_rates_label,
                                    format="Biomass",
                                    title="Death Rate Sensitivity Plots")
plot.plotConcentrationMultiOnSingle(time, sub_death_multi, 'Substrate Concentration', death_rates_label,
                                    format="Substrate",
                                    title="Death Rate Sensitivity Plots")
plot.plotConcentrationMultiOnSingle(time, sub_yield_multi, 'Substrate Concentration', yield_rates_label,
                                    format="Substrate Yield",
                                    title="Yield Sensitivity Plots")
