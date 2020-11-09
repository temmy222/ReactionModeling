import os
import matplotlib.pyplot as plt
import numpy as np


class Plotting(object):
    """
    This class helps in making plots of data from biodegradation calculations

    """

    def __init__(self):
        pass

    def plotConcentration(self, time, yValue, yLabel, format='Substrate'):
        fig, axs = plt.subplots(1, 1)
        axs.plot(time, yValue)
        axs.set_xlabel('Time (hours)', fontsize=14)
        axs.set_ylabel(yLabel, fontsize=14)
        axs.ticklabel_format(useOffset=False)
        plt.setp(axs.get_xticklabels(), fontsize=14)
        plt.setp(axs.get_yticklabels(), fontsize=14)
        plt.tight_layout()
        plt.show()
        fig.savefig(format + ' Concentration' + '.png', bbox_inches='tight', dpi=600)

    def plotMonod(self, sub_conc, growth, yLabel):
        fig, axs = plt.subplots(1, 1)
        axs.plot(sub_conc, growth)
        axs.set_xlabel('Substrate Concentration', fontsize=14)
        axs.set_ylabel(yLabel, fontsize=14)
        axs.ticklabel_format(useOffset=False)
        plt.setp(axs.get_xticklabels(), fontsize=14)
        plt.setp(axs.get_yticklabels(), fontsize=14)
        plt.tight_layout()
        plt.show()
        fig.savefig('Monod' + '.png', bbox_inches='tight', dpi=600)

    def plotConcentrationMultiOnSingle(self, time, yValue, yLabel, label, format='Substrate', title='Sensitivity',
                                       filename=' default'):
        fig, axs = plt.subplots(1, 1)
        for i in range(len(yValue)):
            axs.plot(time, yValue[i], label=label[i])
        axs.legend()
        if filename == 'Monod':
            axs.set_xlabel('Substrate Concentration', fontsize=14)
        else:
            axs.set_xlabel('Time (hours)', fontsize=14)
        axs.set_ylabel(yLabel, fontsize=14)
        axs.set_title(title, fontsize=24)
        axs.ticklabel_format(useOffset=False)
        plt.setp(axs.get_xticklabels(), fontsize=14)
        plt.setp(axs.get_yticklabels(), fontsize=14)
        plt.tight_layout()
        plt.show()
        fig.savefig(format + filename + '.png', bbox_inches='tight', dpi=600)
