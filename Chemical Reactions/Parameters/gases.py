import os

import numpy as np

from Parameters.utils import getComponents, searchComp


class Gases(object):
    """
    This class reads data from the supplied thermodynamic database in TOUGHREACT format from the gases
    section of the database

    """

    def __init__(self, dest, file):

        """
        An instance of this class takes in two parameters;

        file --> the name of the file (thermodynamic database)
        dest ---> where the file is located
        """
        self.dest = dest
        self.file = file
        os.chdir(dest)

    def getLine(self, comp_name, line_index):
        assert isinstance(comp_name, str)
        all_gases, all_liquid, all_minerals = getComponents(self.dest, self.file)
        pos = searchComp(comp_name, all_gases)
        output = all_gases[pos[line_index]]
        return output

    def getMolarMass(self, comp_name):
        parameters = self.getLine(comp_name, 0)
        molarMass = parameters[1]
        molarMass = float(molarMass)
        return molarMass

    def getMolarDiameter(self, comp_name):
        parameters = self.getLine(comp_name, 0)
        output = parameters[2]
        output = float(output)
        return output

    def getNumberOfReactingSpecies(self, comp_name):
        parameters = self.getLine(comp_name, 0)
        output = parameters[3]
        output = float(output)
        return output

    def getStoichiometry(self, comp_name):
        parameters = self.getLine(comp_name, 0)
        reactants = []
        for i in range(4, len(parameters), 2):
            reactants.append(parameters[i])
        return reactants

    def getReactants(self, comp_name):
        parameters = self.getLine(comp_name, 0)
        reactants = []
        for i in range(5, len(parameters), 2):
            reactants.append(parameters[i])
        return reactants

    def getReaction(self, comp_name):
        dict_to_write = {}
        x = self.getReactants(comp_name)
        value = self.getStoichiometry(comp_name)

        for i in range(0, len(x)):
            dict_to_write[x[i]] = value[i]

        return dict_to_write

    def getListOfEquilibriumConstants(self, compName):
        parameters = self.getLine(compName, 1)
        parameters = parameters[1:]
        parameters = list(map(float, parameters))
        return parameters

    def getRegressionCoefficients(self, comp_name):
        parameters = self.getLine(comp_name, 2)
        parameters = parameters[1:]
        parameters = list(map(float, parameters))
        return parameters

    def getEquilibriumConstantAtTemp(self, comp_name, temp, unit='celsius'):
        if unit.lower() == 'celsius':
            temp = temp + 273.15
        reg_coeff = self.getRegressionCoefficients(comp_name)
        regression = reg_coeff[0]*np.log(temp) + reg_coeff[1] + reg_coeff[2]*temp + reg_coeff[3]/temp + reg_coeff[4]/temp**2
        return regression