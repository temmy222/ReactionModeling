import itertools
import os
import re
import string
from collections import OrderedDict

from Parameters.basis import Basis
from Parameters.mineral import Mineral
from Parameters.utils import slicing, split, diff_list


class Preparation(object):
    def __init__(self, dest, file, database):

        """
        An instance of this class takes in two parameters;

        file --> the name of the file
        dest ---> where the file is located
        """
        self.dest = dest
        self.file = file
        os.chdir(dest)
        self.database = database
        self.kinetic = False
        self.equilibrium = False
        self.dissolution = False
        self.precipitation = False

