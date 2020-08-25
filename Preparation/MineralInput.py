import itertools
import re
from collections import OrderedDict

from Parameters.mineral import Mineral
from Parameters.utils import diff_list
from Preparation.MineralKineticInput import MineralKineticInput
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

    def compareKineticToInput(self):
        mineral_kinetic = MineralKineticInput(self.dest, self.file, self.database)
        kinetic_minerals = mineral_kinetic.getMinerals()
        input_minerals = self.getMinerals()
        kinetic_minerals = [x.upper() for x in kinetic_minerals]
        input_minerals = [x.upper() for x in input_minerals]
        missing_minerals = diff_list(kinetic_minerals, input_minerals)
        return missing_minerals

    def checkKineticInInput(self):
        flag = False
        mineral_kinetic = MineralKineticInput(self.dest, self.file, self.database)
        kinetic_minerals = mineral_kinetic.getMinerals()
        input_minerals = self.getMinerals()
        kinetic_minerals = [x.upper() for x in kinetic_minerals]
        input_minerals = [x.upper() for x in input_minerals]
        missing_minerals = diff_list(kinetic_minerals, input_minerals)
        if len(missing_minerals) == 0:
            flag = True
        return flag
