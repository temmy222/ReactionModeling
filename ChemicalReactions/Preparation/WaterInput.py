import re

import numpy as np

from Parameters.utils import diff_list
from Preparation.ReadInput import ReadInput


class WaterInput(object):
    """
    This class reads data from the supplied TOUGHREACT chemical.inp file. It reads only the water input section

    """

    def __init__(self, dest, file, database, water_species=None):
        """
        An instance of this class takes in two parameters;

        file --> the name of the file (chemical.inp)
        dest ---> where the file is located
        database ---> name of the thermodynamic database
        """
        self.dest = dest
        self.file = file
        self.database = database
        self.read_file = ReadInput(self.dest, self.file, self.database)
        self.water_block = self.read_file.readWaterData()
        self.water_species = water_species

    def getWaterInput(self):
        if self.water_species is None:
            temp_value = []
            final_value = []
            output = list(self.water_block.values())
            for i in range(0, len(output)):
                middle = output[i][0]
                temp = middle.split()
                if middle.startswith("'") or re.match('^[a-zA-Z]+', middle):
                    temp_value.append(middle)
            for value in temp_value:
                if value.startswith("'"):
                    final_value.append(value[1:-1])
                else:
                    final_value.append(value)
        else:
            final_value = self.water_species

        return final_value

    def compareWaterToBasis(self):
        aqueous = self.read_file.getBasisSpecies()
        temp = []
        for specie in aqueous:
            temp.append(specie.strip("'"))
        aqueous = temp.copy()
        aqueous = [x.upper() for x in aqueous]
        mineral_species = self.getWaterInput()
        mineral_species = [x.upper() for x in mineral_species]
        missing_species = diff_list(aqueous, mineral_species)
        return missing_species

    def checkAllWaterInBasis(self, water_species=None):
        flag = False
        if water_species is None:
            temp = []
            aqueous = self.read_file.getBasisSpecies()
            for specie in aqueous:
                temp.append(specie.strip("'"))
            aqueous = temp.copy()
            aqueous = [x.upper() for x in aqueous]
            mineral_species = self.getWaterInput()
            mineral_species = [x.upper() for x in mineral_species]
            if all(x in aqueous for x in mineral_species):
                flag = True
        else:
            temp = []
            aqueous = self.read_file.getBasisSpecies()
            for specie in aqueous:
                temp.append(specie.strip("'"))
            aqueous = temp.copy()
            aqueous = [x.upper() for x in aqueous]
            water_species = [x.upper() for x in water_species]
            if all(x in aqueous for x in water_species):
                flag = True
        return flag

    def getWaterComposition(self):
        temp_value = []
        output = list(self.water_block.values())
        for i in range(0, len(output)):
            middle = output[i][3]
            temp_value.append(middle)
        return temp_value

    def getWaterNRGuess(self):
        temp_value = []
        output = list(self.water_block.values())
        for i in range(0, len(output)):
            middle = output[i][2]
            temp_value.append(middle)
        return temp_value

    def determinePH(self):
        output = list(self.water_block.values())
        temp_value = 0
        for i in range(0, len(output)):
            if int(output[i][1]) == 3:
                temp_value = np.log10(float(output[i][3]))
        return temp_value
