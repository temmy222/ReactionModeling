from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

from Parameters.utils import slicing, split, getComponents, searchComp, getCompNames
from pytough.t2listing import t2listing
import os
import re


def getListOfTemperatures():
    temp = [0, 25, 60, 100, 150, 200, 250, 300]
    return temp


class Aqueous(object):
    """
    This class reads data from the supplied thermodynamic database in TOUGHREACT format from the aqueous section of the
    database

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
        pos = searchComp(comp_name, all_liquid)
        output = all_liquid[pos[line_index]]
        return output

    def getMolarMass(self, comp_name):
        parameters = self.getLine(comp_name, 0)
        molarMass = parameters[1]
        molarMass = float(molarMass)
        return molarMass

    def getListOfEquilibriumConstants(self, compName):
        parameters = self.getLine(compName, 1)
        parameters = parameters[1:]
        parameters = list(map(float, parameters))
        return parameters

    # def getEquilibriumConstantAtTemp(self, compName, Temp):
    #     parameters = self.getListOfEquilibriumConstants(compName)
    #     temperatures = getListOfTemperatures()
    #     if Temp not in temperatures:
    #         raise RuntimeError("the specified temperature is not in the list of temperatures. It can only be 0, 25, "
    #                            "60, 100, 150, 200, 250, 300")
    #     index_temp = temperatures.index(Temp)
    #     return parameters[index_temp]

    def getHydratedRadius(self, comp_name):
        parameters = self.getLine(comp_name, 0)
        radius = parameters[2]
        radius = float(radius)
        return radius

    def getElectricCharge(self, comp_name):
        parameters = self.getLine(comp_name, 0)
        electric_charge = parameters[3]
        electric_charge = float(electric_charge)
        return electric_charge

    def getNumberOfReactingSpecies(self, comp_name):
        parameters = self.getLine(comp_name, 0)
        output = parameters[4]
        output = float(output)
        return output

    def getReactants(self, comp_name):
        parameters = self.getLine(comp_name, 0)
        reactants = []
        for i in range(6, len(parameters), 2):
            reactants.append(parameters[i])
        return reactants

    def getStoichiometry(self, comp_name):
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

    def getAllAqueousComplexes(self):
        all_gases, all_liquid, all_minerals = getComponents(self.dest, self.file)
        list_of_components = getCompNames(all_liquid)
        temp = []
        for specie in list_of_components:
            temp.append(specie.strip("'"))
        return temp

    def getRegressionCoefficients(self, comp_name):
        parameters = self.getLine(comp_name, 2)
        parameters = parameters[1:]
        parameters = list(map(float, parameters))
        return parameters

    def getEquilibriumConstantAtTemp(self, comp_name, temp, unit='celsius'):
        if unit.lower() == 'celsius':
            temp = temp + 273.15
        reg_coeff = self.getRegressionCoefficients(comp_name)
        regression = reg_coeff[0] * np.log(temp) + reg_coeff[1] + reg_coeff[2] * temp + reg_coeff[3] / temp + reg_coeff[
            4] / temp ** 2
        return regression
