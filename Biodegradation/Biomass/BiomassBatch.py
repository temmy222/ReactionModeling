import numpy as np


class BiomassBatch(object):
    def __init__(self, death_rate, initial_biomass, time, biomass_growth_rate):
        self.time = time
        self.initial_biomass = initial_biomass
        self.death_rate = death_rate
        self.biomass_growth_rate = biomass_growth_rate

    def biomass_concentration_analytical(self):
        inner_value = (self.biomass_growth_rate - self.death_rate) * self.time[len(self.time)-1]
        # inner_value = (0.86 - self.death_rate) * self.time
        biomass_X = self.initial_biomass * np.exp(inner_value)
        return biomass_X

    def biomass_concentration_numerical(self):
        biomass_X = np.repeat(self.initial_biomass, len(self.time))
        for i in range(0, len(self.time) - 1):
            deltaT = self.time[i + 1] - self.time[i]
            inner_value = (self.biomass_growth_rate - self.death_rate)
            biomass_new = (inner_value * deltaT * biomass_X) + biomass_X
            biomass_X = biomass_new
        return biomass_X
