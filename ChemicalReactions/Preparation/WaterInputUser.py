from Parameters.basis import Basis
from Parameters.utils import diff_list, getCompNames
from Preparation.ReadInput import ReadInput


class WaterInputUser(object):
    """
    This class reads data from the supplied TOUGHREACT chemical.inp file. It reads only the water input section

    """

    def __init__(self, dest, database, water_species):
        """
        An instance of this class takes in two parameters;

        file --> the name of the file (chemical.inp)
        dest ---> where the file is located
        database ---> name of the thermodynamic database
        """
        self.dest = dest
        self.database = database
        self.water_species = water_species

    def compareWaterIsABasisSpecie(self):
        basis = Basis(self.dest, self.database)
        all_basis_species = basis.getBasis()
        list_of_basis = getCompNames(all_basis_species)
        aqueous = [x.upper() for x in self.water_species]
        list_of_basis = [x.upper() for x in list_of_basis]
        list_of_basis = [i[1:-1] for i in list_of_basis]
        check = all(item in list_of_basis for item in aqueous)
        if check is not True:
            raise ValueError("Provided specie list are not all present in database. Please recheck")
        return check
