import itertools
import os
import re
import string
from collections import OrderedDict

from Parameters.basis import Basis
from Parameters.mineral import Mineral
from Parameters.utils import slicing, split, diff_list


class Preparation(object):
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

    def readFile(self):
        f = open(self.file, 'r')
        read_file = f.readlines()
        return read_file

    def readPrimarySpeciesBlock(self):
        read_file = self.readFile()
        pattern = r"^#PRIMARY"
        pattern2 = r"^# AQUEOUS KINETICS"
        listt, first_point = slicing(pattern, read_file)
        listt, second_point = slicing(pattern2, read_file)
        param = read_file[first_point[0] + 1:second_point[0] - 2]
        param = split(param)
        return param

    def getBasisSpecies(self):
        output = self.readPrimarySpeciesBlock()
        temp_value = []
        final_value = []
        output = list(output.values())
        for i in range(0, len(output)):
            middle = output[i][0]
            temp_value.append(middle)
        return temp_value

    def readAqueousKinetics(self):
        read_file = self.readFile()
        pattern = r"^# AQUEOUS KINETICS"
        pattern2 = r"^# AQUEOUS COMPLEXES"
        listt, first_point = slicing(pattern, read_file)
        listt, second_point = slicing(pattern2, read_file)
        param = read_file[first_point[0] + 1:second_point[0] - 2]
        return param

    def readAqueousComplexes(self):
        read_file = self.readFile()
        pattern = r"^# AQUEOUS COMPLEXES"
        pattern2 = r"^# MINERALS"
        listt, first_point = slicing(pattern, read_file)
        listt, second_point = slicing(pattern2, read_file)
        param = read_file[first_point[0] + 1:second_point[0] - 2]
        return param

    def readMineralBlock(self):
        read_file = self.readFile()
        pattern = r"^# MINERALS"
        pattern2 = r"^# GASES"
        listt, first_point = slicing(pattern, read_file)
        listt, second_point = slicing(pattern2, read_file)
        param = read_file[first_point[0] + 1:second_point[0] - 3]
        param = split(param)
        return param

    def getMinerals(self):
        output = self.readMineralBlock()
        temp_value = []
        final_value = []
        output = list(output.values())
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
        aqueous = self.getBasisSpecies()
        aqueous = [x.upper() for x in aqueous]
        mineral_species = self.getAllConstituentMineralSpecies()
        mineral_species = [x.upper() for x in mineral_species]
        missing_species = diff_list(aqueous, mineral_species)
        return missing_species

    def checkAllMineralInBasis(self):
        flag = False
        aqueous = self.getBasisSpecies()
        aqueous = [x.upper() for x in aqueous]
        mineral_species = self.getAllConstituentMineralSpecies()
        mineral_species = [x.upper() for x in mineral_species]
        if all(x in aqueous for x in mineral_species):
            flag = True
        return flag

