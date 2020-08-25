
import os
from Parameters.utils import slicing, split


class ReadInput(object):
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
        self.read_file = self.readFile()

    def readFile(self):
        f = open(self.file, 'r')
        read_file = f.readlines()
        return read_file

    def readPrimarySpeciesBlock(self):
        pattern = r"^#PRIMARY"
        pattern2 = r"^# AQUEOUS KINETICS"
        listt, first_point = slicing(pattern, self.read_file)
        listt, second_point = slicing(pattern2, self.read_file)
        param = self.read_file[first_point[0] + 1:second_point[0] - 2]
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
        pattern = r"^# AQUEOUS KINETICS"
        pattern2 = r"^# AQUEOUS COMPLEXES"
        listt, first_point = slicing(pattern, self.read_file)
        listt, second_point = slicing(pattern2, self.read_file)
        param = self.read_file[first_point[0] + 1:second_point[0] - 2]
        return param

    def readAqueousComplexes(self):
        pattern = r"^# AQUEOUS COMPLEXES"
        pattern2 = r"^# MINERALS"
        listt, first_point = slicing(pattern, self.read_file)
        listt, second_point = slicing(pattern2, self.read_file)
        param = self.read_file[first_point[0] + 1:second_point[0] - 2]
        return param

    def readMineralBlock(self):
        pattern = r"^# MINERALS"
        pattern2 = r"^# GASES"
        listt, first_point = slicing(pattern, self.read_file)
        listt, second_point = slicing(pattern2, self.read_file)
        param = self.read_file[first_point[0] + 1:second_point[0] - 3]
        param = split(param)
        return param

    def readWaterData(self):
        pattern = r"^# INITIAL AND BOUDARY WATER TYPES"
        pattern2 = r"^#--------------"
        listt, first_point = slicing(pattern, self.read_file)
        listt, second_point = slicing(pattern2, self.read_file, first_point[0])
        param = self.read_file[first_point[0] + 6:second_point[0] - 2]
        param = split(param)
        return param


