import matplotlib.pyplot as plt

from Parameters.utils import slicing, split, getComponents, searchComp
from pytough.t2listing import t2listing
import os
import re


def getListOfTemperatures():
    temp = [0, 25, 60, 100, 150, 200, 250, 300]
    return temp


class Aqueous(object):
    """
    This class helps in making plots for batch reactions carried out with TOUGHREACT

    """

    def __init__(self, dest, file):

        """
        An instance of this class takes in two parameters;

        file --> the name of the file
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

    def getEquilibriumConstantAtTemp(self, compName, Temp):
        parameters = self.getListOfEquilibriumConstants(compName)
        temperatures = getListOfTemperatures()
        if Temp not in temperatures:
            raise RuntimeError("the specified temperature is not in the list of temperatures. It can only be 0, 25, "
                               "60, 100, 150, 200, 250, 300")
        index_temp = temperatures.index(Temp)
        return parameters[index_temp]

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
        parameters = self.getLine(comp_name, 0)
        dict_to_write = {}

        return len(parameters)

    def plotGasK(self, compname):
        gases, aqueouss, minerals = self.getComponents()
        print(gases)
        pos = self.searchComp(compname, gases)
        temp = [0, 25, 60, 100, 150, 200, 250, 300]
        fig = plt.figure(figsize=(10, 5))
        values = gases[pos[1]][1:9]
        print(values)
        for i in range(0, len(values)):
            values[i] = float(values[i])
        plt.plot(temp, values)
        plt.grid()
        compname2 = list(compname.split(" "))
        plt.legend(compname2, prop={'size': 16})
        plt.xlabel('Temperature (Celsius) ', fontsize=14)
        plt.ylabel('Log of Equilibirum Constant', fontsize=14)
        fig.savefig('Equilibrium constant' + '.jpg', bbox_inches='tight', dpi=(600))

    def plotSpecieK(self, compname):
        gases, aqueouss, minerals = self.getComponents()
        pos = self.searchComp(compname, aqueouss)
        temp = [0, 25, 60, 100, 150, 200, 250, 300]
        fig = plt.figure(figsize=(10, 5))
        values = aqueouss[pos[1]][1:9]
        for i in range(0, len(values)):
            values[i] = float(values[i])
        plt.plot(temp, values)
        plt.grid()
        compname2 = list(compname.split(" "))
        plt.legend(compname2, prop={'size': 16})
        plt.xlabel('Temperature (Celsius) ', fontsize=14, fontweight='bold')
        plt.ylabel('Log of Equilibirum Constant', fontsize=14, fontweight='bold')
        plt.grid(True, which='both')
        plt.minorticks_on()
        plt.grid(b=True, which='major', linestyle='-', linewidth=0.5, color='k')
        plt.grid(b=True, which='minor', linestyle='-', linewidth=0.1)
        plt.spines['bottom'].set_linewidth(1.5)
        plt.spines['left'].set_linewidth(1.5)
        plt.spines['top'].set_linewidth(0.2)
        plt.spines['right'].set_linewidth(0.2)
        fig.savefig('Equilibrium constant' + '.jpg', bbox_inches='tight', dpi=(600))

    def plotMineralK(self, compname):
        gases, aqueouss, minerals = self.getComponents()
        pos = self.searchComp(compname, minerals)
        temp = [0, 25, 60, 100, 150, 200, 250, 300]
        fig = plt.figure(figsize=(10, 5))
        fig, axs = plt.subplots(1)
        values = minerals[pos[1]][1:9]
        for i in range(0, len(values)):
            values[i] = float(values[i])
        plt.plot(temp, values)
        compname2 = list(compname.split(" "))
        plt.legend(compname2, prop={'size': 16})
        plt.grid()
        plt.xlabel('Temperature (Celsius) ', fontsize=14, fontweight='bold')
        plt.ylabel('Log of Equilibirum Constant', fontsize=14, fontweight='bold')
        plt.grid(True, which='both')
        plt.minorticks_on()
        plt.grid(b=True, which='major', linestyle='-', linewidth=0.5, color='k')
        plt.grid(b=True, which='minor', linestyle='-', linewidth=0.1)
        axs.spines['bottom'].set_linewidth(1.5)
        axs.spines['left'].set_linewidth(1.5)
        axs.spines['top'].set_linewidth(0.2)
        axs.spines['right'].set_linewidth(0.2)
        fig.savefig('Equilibrium constant' + '.jpg', bbox_inches='tight', dpi=(600))

    def plotmultipleMineralK(self, compname):
        temp = [0, 25, 60, 100, 150, 200, 250, 300]
        fig = plt.figure(figsize=(10, 10))
        fig, axs = plt.subplots(1, 1)
        markers = ["o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "D",
                   "d", "|", "_"]
        if isinstance(compname, list):
            k = 0
            for i in range(0, len(compname)):
                gases, aqueouss, minerals = self.getComponents()
                pos = self.searchComp(compname[i], minerals)
                values = minerals[pos[1]][1:9]
                value = self.converttofloat(values)
                plt.plot(temp, value, marker=markers[k], linewidth=2)
                plt.legend(compname, prop={'size': 9})
                k = k + 1
            plt.grid()
            plt.xlabel('Temperature (Celsius) ', fontsize=14)
            plt.ylabel('Log of Equilibirum Constant', fontsize=14)
            plt.grid(True, which='both')
            plt.minorticks_on()
            plt.grid(b=True, which='major', linestyle='-', linewidth=0.5, color='k')
            plt.grid(b=True, which='minor', linestyle='-', linewidth=0.1)
            axs.spines['bottom'].set_linewidth(1.5)
            axs.spines['left'].set_linewidth(1.5)
            axs.spines['top'].set_linewidth(0.2)
            axs.spines['right'].set_linewidth(0.2)
            fig.savefig('Equilibrium constant' + '.jpg', bbox_inches='tight', dpi=(600))
