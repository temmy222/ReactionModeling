import os
import matplotlib.pyplot as plt
import numpy as np

from Parameters.utils import getComponents, searchComp, convertToFloat


class Plotting(object):
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

    def plotGasK(self, compname):
        gases, aqueouss, minerals = getComponents()
        pos = searchComp(compname, gases)
        temp = [0, 25, 60, 100, 150, 200, 250, 300]
        fig = plt.figure(figsize=(10, 5))
        values = gases[pos[1]][1:9]
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
        gases, aqueouss, minerals = getComponents()
        pos = searchComp(compname, aqueouss)
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
        plt.ylabel('Log of Equilibrium Constant', fontsize=14, fontweight='bold')
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
        gases, aqueouss, minerals = getComponents()
        pos = searchComp(compname, minerals)
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
        plt.ylabel('Log of Equilibrium Constant', fontsize=14, fontweight='bold')
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
                gases, aqueouss, minerals = getComponents()
                pos = searchComp(compname[i], minerals)
                values = minerals[pos[1]][1:9]
                value = convertToFloat(values)
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
