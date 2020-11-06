import numpy as np
class BiomassBatch(object):
    def __init__(self, biomass_growth_rate, death_rate, initial_biomass, time, sub_utilization_rate = None, yield_mass = None):
        self.yield_mass = yield_mass
        self.sub_utilization_rate = sub_utilization_rate
        self.time = time
        self.initial_biomass = initial_biomass
        self.death_rate = death_rate
        self.biomass_growth_rate = biomass_growth_rate

    def biomass_concentration_analytical(self):
        if self.sub_utilization_rate is not None and self.yield_mass is not None:
            self.biomass_growth_rate = self.sub_utilization_rate * self.yield_mass
        inner_value = (self.biomass_growth_rate - self.death_rate) * self.time
        biomass_X = self.initial_biomass * np.exp(inner_value)
        return biomass_X