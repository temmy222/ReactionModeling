import itertools
import re
from collections import OrderedDict

from Parameters.mineral import Mineral
from Parameters.utils import diff_list
from Preparation.ReadInput import ReadInput


class MineralKineticInput(object):
    """
    This class reads data from the supplied TOUGHREACT chemical.inp file. It reads only the mineral kinetic input section

    """
    def __init__(self, dest, file, database):
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
        self.mineral_block = self.read_file.readMineralKineticBlock()

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
                temp_value.append(i)
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
        output = list(self.mineral_block.values())
        dissolution = self.determineDissolution()
        mineral_line_index = self.getMineralLineIndex()
        mineral_number = len(self.getMinerals())
        dissolution_rate_constants = [None] * mineral_number
        for i in range(0, len(mineral_line_index)):
            if dissolution[i] is True:
                index = mineral_line_index[i] + 1
                dissolution_rate_constants[i] = float(output[index][0])
        return dissolution_rate_constants

    def getDissolutionFirstExponent(self):
        output = list(self.mineral_block.values())
        dissolution = self.determineDissolution()
        mineral_line_index = self.getMineralLineIndex()
        mineral_number = len(self.getMinerals())
        exponent = [None] * mineral_number
        for i in range(0, len(mineral_line_index)):
            if dissolution[i] is True:
                index = mineral_line_index[i] + 1
                exponent[i] = float(output[index][2])
        return exponent

    def getDissolutionSecondExponent(self):
        output = list(self.mineral_block.values())
        dissolution = self.determineDissolution()
        mineral_line_index = self.getMineralLineIndex()
        mineral_number = len(self.getMinerals())
        exponent = [None] * mineral_number
        for i in range(0, len(mineral_line_index)):
            if dissolution[i] is True:
                index = mineral_line_index[i] + 1
                exponent[i] = float(output[index][3])
        return exponent

    def getDissolutionActivationEnergy(self):
        output = list(self.mineral_block.values())
        dissolution = self.determineDissolution()
        mineral_line_index = self.getMineralLineIndex()
        mineral_number = len(self.getMinerals())
        activation_energy = [None] * mineral_number
        for i in range(0, len(mineral_line_index)):
            if dissolution[i] is True:
                index = mineral_line_index[i] + 1
                activation_energy[i] = float(output[index][4])
        return activation_energy

    def getDissolutionMultipleMechanisms(self):
        output = list(self.mineral_block.values())
        dissolution = self.determineDissolution()
        mineral_line_index = self.getMineralLineIndex()
        mineral_number = len(self.getMinerals())
        multi_mech = [None] * mineral_number
        for i in range(0, len(mineral_line_index)):
            if dissolution[i] is True:
                index = mineral_line_index[i] + 1
                multi_mech[i] = float(output[index][1])
        return multi_mech

    def getPrecipitationRateConstants(self):
        output = list(self.mineral_block.values())
        kinetic = self.determinePrecipitation()
        mineral_line_index = self.getMineralLineIndex()
        mineral_number = len(self.getMinerals())
        precipitation_rate_constants = [None] * mineral_number
        multi_mech = self.getDissolutionMultipleMechanisms()
        for i in range(0, len(mineral_line_index)):
            if kinetic[i] is True and multi_mech[i] == 0:
                index = mineral_line_index[i] + 2
                precipitation_rate_constants[i] = float(output[index][0])
            elif kinetic[i] is True and multi_mech[i] != 0:
                index = mineral_line_index[i] + 4
                precipitation_rate_constants[i] = float(output[index][0])
        return precipitation_rate_constants

    def getPrecipitationFirstExponent(self):
        output = list(self.mineral_block.values())
        kinetic = self.determinePrecipitation()
        mineral_line_index = self.getMineralLineIndex()
        mineral_number = len(self.getMinerals())
        dissolution_rate_constants = [None] * mineral_number
        multi_mech = self.getDissolutionMultipleMechanisms()
        for i in range(0, len(mineral_line_index)):
            if kinetic[i] is True and multi_mech[i] == 0:
                index = mineral_line_index[i] + 2
                dissolution_rate_constants[i] = float(output[index][2])
            elif kinetic[i] is True and multi_mech[i] != 0:
                index = mineral_line_index[i] + 4
                dissolution_rate_constants[i] = float(output[index][2])
        return dissolution_rate_constants

    def getPrecipitationSecondExponent(self):
        output = list(self.mineral_block.values())
        kinetic = self.determinePrecipitation()
        mineral_line_index = self.getMineralLineIndex()
        mineral_number = len(self.getMinerals())
        dissolution_rate_constants = [None] * mineral_number
        multi_mech = self.getDissolutionMultipleMechanisms()
        for i in range(0, len(mineral_line_index)):
            if kinetic[i] is True and multi_mech[i] == 0:
                index = mineral_line_index[i] + 2
                dissolution_rate_constants[i] = float(output[index][3])
            elif kinetic[i] is True and multi_mech[i] != 0:
                index = mineral_line_index[i] + 4
                dissolution_rate_constants[i] = float(output[index][3])
        return dissolution_rate_constants

    def getPrecipitationActivationEnergy(self):
        output = list(self.mineral_block.values())
        kinetic = self.determinePrecipitation()
        mineral_line_index = self.getMineralLineIndex()
        mineral_number = len(self.getMinerals())
        dissolution_rate_constants = [None] * mineral_number
        multi_mech = self.getDissolutionMultipleMechanisms()
        for i in range(0, len(mineral_line_index)):
            if kinetic[i] is True and multi_mech[i] == 0:
                index = mineral_line_index[i] + 2
                dissolution_rate_constants[i] = float(output[index][4])
            elif kinetic[i] is True and multi_mech[i] != 0:
                index = mineral_line_index[i] + 4
                dissolution_rate_constants[i] = float(output[index][4])
        return dissolution_rate_constants

    def getPrecipitationInitialVolumeFraction(self):
        output = list(self.mineral_block.values())
        kinetic = self.determinePrecipitation()
        mineral_line_index = self.getMineralLineIndex()
        mineral_number = len(self.getMinerals())
        dissolution_rate_constants = [None] * mineral_number
        multi_mech = self.getDissolutionMultipleMechanisms()
        for i in range(0, len(mineral_line_index)):
            if kinetic[i] is True and multi_mech[i] == 0:
                index = mineral_line_index[i] + 2
                dissolution_rate_constants[i] = float(output[index][8])
            elif kinetic[i] is True and multi_mech[i] != 0:
                index = mineral_line_index[i] + 4
                dissolution_rate_constants[i] = float(output[index][8])
        return dissolution_rate_constants

