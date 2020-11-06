import os

from Parameters.aqueous import Aqueous
from Preparation.WaterInputUser import WaterInputUser


class PreparationUser(object):
    """
    This class provides methods that prepares the solver for its calculations

    """

    def __init__(self, dest, database, water_species=None, gas_species=None, minerals=None):
        """
        An instance of this class takes in two parameters;

        file --> the name of the file
        dest ---> where the file is located
        """
        self.dest = dest
        os.chdir(dest)
        self.database = database
        self.water_species = water_species
        self.gas_species = gas_species
        self.minerals = minerals
        self.aqueous_species = Aqueous(self.dest, self.database)
        self.water_input = WaterInputUser(self.dest, self.database, self.water_species)

    def getAllAqueousComplexesInWater(self):
        all_aqueous = self.aqueous_species.getAllAqueousComplexes()
        all_reactants = self.aqueous_species.getAllReactants()
        water_species_inside = list(map(lambda x: x.lower(), self.water_species))
        if self.water_input.compareWaterIsABasisSpecie() is True:
            output = []
            for i in range(0, len(all_reactants)):
                temp = list(map(lambda x: x.lower()[1:-1], all_reactants[i]))
                if all(x in water_species_inside for x in temp):
                    output.append(all_aqueous[i])
        else:
            raise ValueError("Provided specie list are not all present in database. Please recheck")
        return output[:-1]

    def getUnknowns(self):
        complexes = self.getAllAqueousComplexesInWater()
        reactants = []
        for complex in complexes:
            reactants.append(self.aqueous_species.getReactants(complex))
        reactants = [item for sublist in reactants for item in sublist]
        reactants = [i[1:-1] for i in reactants]
        reactants.extend(complexes)
        reactants = list(set(reactants))
        reactants.remove('H2O')
        return reactants

    def massBalance(self, comp):
        lhs = self.aqueous_species.getLeftSide(comp)
        return lhs
