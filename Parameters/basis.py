import os
import re

from Parameters.utils import slicing, split, searchComp


class Basis(object):
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
        os.chdir(self.dest)

    def searchBasis(self, compname, dict_of_basis_species):
        pos = searchComp(compname, dict_of_basis_species)
        return pos

    def getBasis(self):
        f = open(self.file, 'r')
        m = f.readlines()
        for i in range(len(m) - 1, -1, -1):
            if re.match(r'\s', m[i]):
                del m[i]
        pattern = r"^'temperature"  # check for line that starts with 'temperature
        listt, mache = slicing(pattern, m)
        first_index = mache[0]
        pattern2 = r"^'null"  # check for line that starts with 'null
        listt, mache = slicing(pattern2, m)
        second_index = mache[0]
        basis_species = m[first_index + 1:second_index]
        basis_species = split(basis_species)
        return basis_species

    def getMolarMass(self, comp_name):
        parameters = self.getBasis()
        pos = searchComp(comp_name, parameters)
        line_param = parameters[pos[0]]
        molarMass = line_param[3]
        molarMass = float(molarMass)
        return molarMass
    
    def getHydratedRadius(self, comp_name):
        parameters = self.getBasis()
        pos = searchComp(comp_name, parameters)
        line_param = parameters[pos[0]]
        radius = line_param[1]
        radius = float(radius)
        return radius

    def getElectricCharge(self, comp_name):
        parameters = self.getBasis()
        pos = searchComp(comp_name, parameters)
        line_param = parameters[pos[0]]
        electric_charge = line_param[2]
        electric_charge = float(electric_charge)
        return electric_charge
