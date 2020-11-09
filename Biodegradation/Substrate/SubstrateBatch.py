import numpy as np

from Biodegradation.Biomass.BiomassBatch import BiomassBatch


class SubstrateBatch(object):
    def __init__(self, death_rate, initial_biomass, initial_substrate, time, biomass_growth_rate,
                 yield_mass):
        self.initial_substrate = initial_substrate
        self.yield_mass = yield_mass
        self.time = time
        self.initial_biomass = initial_biomass
        self.death_rate = death_rate
        self.biomass_growth_rate = biomass_growth_rate

    def substrate_concentration_analytical(self):
        biomass = BiomassBatch(self.death_rate, self.initial_biomass, self.time,
                                         self.biomass_growth_rate)
        bio_concentration = biomass.biomass_concentration_analytical()
        sub_concentration = self.initial_substrate - (bio_concentration/self.yield_mass)
        sub_concentration[sub_concentration < 0] = 0
        return sub_concentration
