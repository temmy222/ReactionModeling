import itertools
import re
from collections import OrderedDict

from Parameters.mineral import Mineral
from Parameters.utils import diff_list
from Preparation.ReadInput import ReadInput


class MineralInput(object):
    def __init__(self, dest, file, database):
        """
        An instance of this class takes in two parameters;

        file --> the name of the file
        dest ---> where the file is located
        """
        self.dest = dest
        self.file = file
        self.database = database
        self.read_file = ReadInput(self.dest, self.file, self.database)
        self.mineral_block = self.read_file.readMineralBlock()

    def getMinerals(self):
        temp_value = []
        final_value = []
        output = list(self.mineral_block.values())
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

        return final_value

    def getMineralLine(self):
        temp_value = []
        output = list(self.mineral_block.values())
        for i in range(0, len(output)):
            middle = output[i][0]
            if middle.startswith("'") or re.match('^[a-zA-Z]+', middle):
                temp_value.append(output[i])
        return temp_value

    def getMineralLineIndex(self):
        temp_value = []
        output = list(self.mineral_block.values())
        for i in range(0, len(output)):
            middle = output[i][0]
            if middle.startswith("'") or re.match('^[a-zA-Z]+', middle):
                temp_value.append(output[i])
        return temp_value

    def getAllConstituentMineralSpecies(self):
        minerallist = self.getMinerals()
        minerals = Mineral(self.dest, self.database)
        output = []
        for i in range(0, len(minerallist)):
            mineral = minerallist[i]
            mineral = "%s%s" % (mineral[0].upper(), mineral[1:])
            temp = minerals.getReactants(mineral)
            output.append(temp)
        output = list(itertools.chain.from_iterable(output))
        output = list(OrderedDict.fromkeys(output))
        return output

    def compareMineralToBasis(self):
        aqueous = self.read_file.getBasisSpecies()
        aqueous = [x.upper() for x in aqueous]
        mineral_species = self.getAllConstituentMineralSpecies()
        mineral_species = [x.upper() for x in mineral_species]
        missing_species = diff_list(aqueous, mineral_species)
        return missing_species

    def checkAllMineralInBasis(self):
        flag = False
        aqueous = self.read_file.getBasisSpecies()
        aqueous = [x.upper() for x in aqueous]
        mineral_species = self.getAllConstituentMineralSpecies()
        mineral_species = [x.upper() for x in mineral_species]
        if all(x in aqueous for x in mineral_species):
            flag = True
        return flag

    def determineKinetic(self):
        mineral_line = self.getMineralLine()
        mineral_number = len(self.getMinerals())
        kinetic = [False] * mineral_number
        for i in range(0, len(mineral_line)):
            if int(mineral_line[i][1]) == 1:
                kinetic[i] = True
        return kinetic

    def determinePrecipitation(self):
        mineral_line = self.getMineralLine()
        mineral_number = len(self.getMinerals())
        kinetic = self.determineKinetic()
        precipitate = [False] * mineral_number
        for i in range(0, len(mineral_line)):
            if kinetic[i] is True:
                if int(mineral_line[i][2]) == 2 or int(mineral_line[i][2]) == 3:
                    precipitate[i] = True
        return precipitate

    def determineDissolution(self):
        mineral_line = self.getMineralLine()
        mineral_number = len(self.getMinerals())
        kinetic = self.determineKinetic()
        dissolution = [False] * mineral_number
        for i in range(0, len(mineral_line)):
            if kinetic[i] is True:
                if int(mineral_line[i][2]) == 1 or int(mineral_line[i][2]) == 3:
                    dissolution[i] = True
        return dissolution

    def getDissolutionRateConstants(self):
        temp_value = []
        output = list(self.mineral_block.values())
        dissolution = self.determineDissolution()


        return output

