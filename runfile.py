import os
import time

from Parameters.aqueous import Aqueous
from Solver.preparation import Preparation

dest1 = r"C:\Users\AJ\OneDrive - Louisiana State University\Second numerical paper\carbonate 2"
os.chdir(dest1)
filename = 'thddem1214r3_hs.dat'
chem_file = 'chemical.inp'

start = time.time()


prep = Preparation(dest1, chem_file, filename)
data = prep.getAllAqueousComplexesInWater()



end = time.time()
print(end - start)