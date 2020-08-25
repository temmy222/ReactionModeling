import os

from Parameters.utils import slicing


class Preparation(object):
    def __init__(self, dest, file):

        """
        An instance of this class takes in two parameters;

        file --> the name of the file
        dest ---> where the file is located
        """
        self.dest = dest
        self.file = file
        os.chdir(dest)

    def readFile(self):
        f = open(self.file, 'r')
        read_file = f.readlines()
        return read_file

    def readPrimarySpecies(self):
        read_file = self.readFile()
        pattern = r"^#PRIMARY"
        pattern2 = r"^# AQUEOUS KINETICS"
        listt, first_point = slicing(pattern, read_file)
        listt, second_point = slicing(pattern2, read_file)
        param = read_file[first_point[0]+1:second_point[0]-2]
        return param

    def readAqueousKinetics(self):
        read_file = self.readFile()
        pattern = r"^# AQUEOUS KINETICS"
        pattern2 = r"^# AQUEOUS COMPLEXES"
        listt, first_point = slicing(pattern, read_file)
        listt, second_point = slicing(pattern2, read_file)
        param = read_file[first_point[0]+1:second_point[0]-2]
        return param

    def readAqueousComplexes(self):
        read_file = self.readFile()
        pattern = r"^# AQUEOUS COMPLEXES"
        pattern2 = r"^# MINERALS"
        listt, first_point = slicing(pattern, read_file)
        listt, second_point = slicing(pattern2, read_file)
        param = read_file[first_point[0]+1:second_point[0]-2]
        return param

    def readMineralBlock(self):
        read_file = self.readFile()
        pattern = r"^# MINERALS"
        pattern2 = r"^# GASES"
        listt, first_point = slicing(pattern, read_file)
        listt, second_point = slicing(pattern2, read_file)
        param = read_file[first_point[0]+1:second_point[0]-3]
        return param