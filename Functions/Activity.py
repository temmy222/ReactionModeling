import numpy as np

from constants import Constants


class Activity(object):
    """
    This class helps calculating the activity and fugacity coefficients

    """

    def __init__(self, ion_conc, ion_charges):
        """
        An instance of this class takes in two parameters;

        file --> the name of the file
        dest ---> where the file is located
        """
        self.ion_conc = ion_conc
        self.ion_charges = ion_charges

    def ionicStrength(self):
        I = (self.ion_conc * self.ion_charges ** 2)
        I = np.sum(I) * 0.5
        return I

    def acDebyeHuckel(self, index, ionic_strength=None):
        constant = Constants()
        coefficient = -1824000 / (constant.dielectric_constant * (constant.room_temperature + 273)) ** 1.5
        print(coefficient)
        if ionic_strength is None:
            ionic_strength = self.ionicStrength()
        print(ionic_strength)
        print(self.ion_charges[index])
        output = coefficient * self.ion_charges[index] ** 2 * np.sqrt(ionic_strength)
        output = 10 ** output
        return output
