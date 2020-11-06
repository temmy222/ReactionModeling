import os


class ReadInput(object):
    """
    This class reads blocks of data from each section of the supplied TOUGHREACT chemical.inp file for subsequent
    processing by the various child classes.

    """

    def __init__(self, dest, database):
        """
        An instance of this class takes in two parameters;

        dest ---> where the file is located
        database ---> name of the thermodynamic database
        """
        self.dest = dest
        os.chdir(dest)
        self.database = database
        self.read_file = self.readFile()
