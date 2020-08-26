import itertools
import os
import re
import string
from collections import OrderedDict

from Parameters.aqueous import Aqueous
from Parameters.basis import Basis
from Parameters.mineral import Mineral
from Parameters.utils import slicing, split, diff_list


class Preparation(object):
    """
    This class provides methods that prepares the solver for its calculations

    """
    def __init__(self, dest, database, file):

        """
        An instance of this class takes in two parameters;

        file --> the name of the file
        dest ---> where the file is located
        """
        self.dest = dest
        self.file = file
        os.chdir(dest)
        self.database = database
        self.aqueous_species = Aqueous(self.dest, self.file)

    def getAllAqueousComplexesInWater(self):
        all_aqueous = self.aqueous_species.getAllAqueousComplexes()
        output = []
        for specie in all_aqueous:
            output.append(self.aqueous_species.getReaction(specie))
        return output

