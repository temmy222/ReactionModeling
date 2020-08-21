import os

from Parameters.utils import getComponents, searchComp


class Gases(object):
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
        pos = searchComp(comp_name, all_gases)
        output = all_gases[pos[line_index]]
        return output

    def getMolarMass(self, comp_name):
        parameters = self.getLine(comp_name, 0)
        molarMass = parameters[1]
        molarMass = float(molarMass)
        return molarMass