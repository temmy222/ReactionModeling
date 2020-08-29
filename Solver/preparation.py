import itertools
import os
import re
import string
from collections import OrderedDict

from Parameters.aqueous import Aqueous
from Parameters.basis import Basis
from Parameters.mineral import Mineral
from Parameters.utils import slicing, split, diff_list
from Preparation.WaterInput import WaterInput


class Preparation(object):
    """
    This class provides methods that prepares the solver for its calculations

    """

    def __init__(self, dest, file, database):

        """
        An instance of this class takes in two parameters;

        file --> the name of the file
        dest ---> where the file is located
        """
        self.dest = dest
        self.file = file
        os.chdir(dest)
        self.database = database
        self.aqueous_species = Aqueous(self.dest, self.database)
        self.water_input = WaterInput(self.dest, self.file, self.database)

    def getAllAqueousComplexesInWater(self):
        all_aqueous = self.aqueous_species.getAllAqueousComplexes()
        all_reactants = self.aqueous_species.getAllReactants()
        water_species = self.water_input.getWaterSpecies()
        water_species = list(map(lambda x: x.lower(), water_species))
        if self.water_input.checkAllWaterInBasis() is True:
            output = []
            for i in range(0, len(all_reactants)):
                temp = list(map(lambda x: x.lower()[1:-1], all_reactants[i]))
                if all(x in water_species for x in temp):
                    output.append(all_aqueous[i])
        else:
            print('There are missing species')
        return output
