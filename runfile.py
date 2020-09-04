import os
import time
import numpy as np

from Preparation.WaterInputUser import WaterInputUser
from Solver.PreparationUser import PreparationUser
from Solver.preparation import Preparation

dest1 = r"C:\Users\AJ\OneDrive - Louisiana State University\Second numerical paper\carbonate 2"
os.chdir(dest1)
filename = 'thddem1214r3_hs.dat'
chem_file = 'chemical.inp'

start = time.time()
input_primary_species = ['Ca+2', 'H2O', 'H+']

# prep = Preparation(dest1, chem_file, filename)
# data = prep.getAllAqueousComplexesInWater()


prep_user = PreparationUser(dest1, filename, input_primary_species)
aqu = prep_user.getAllAqueousComplexesInWater()

data_user = prep_user.massBalance('CaOH+')

print(np.zeros(2))

end = time.time()
print(end - start)


def solve(equations):
    """
    the constants of a system of linear equations are stored in a list for each equation in the system
    for example the system below:
         2x+9y-3z+7w+8=0
         7x-2y+6z-1w-10=0
         -8x-3y+2z+5w+4=0
         0x+2y+z+w+0=0
    is expressed as the list:
         [[2,9,-3,7,8],[7,-2,6,-1,-10],[-8,-3,2,5,4],[0,2,1,1,0]]
    """
    for i in equations:
        if len(i) != (len(equations) + 1):
            raise ValueError("your equation system has not a valid format")
    lists = []  # I failed to name it meaningfully
    for eq in range(len(equations)):
        # print "equations 1", equations
        # find an equation whose first element is not zero and call it index
        index = -1
        for i in range(len(equations)):
            if equations[i][0] != 0:
                index = i
                break
        if index == -1:
            raise ValueError("your equation system can not be solved")
        # print "index "+str(eq)+": ",index
        # for the equation[index] calc the lists next item  as follows
        lists.append([-1.0 * i / equations[index][0] for i in equations[index][1:]])
        # print "list"+str(eq)+": ", lists[-1]
        # remove equation[index] and modify the others
        equations.pop(index)
        for i in equations:
            for j in range(len(lists[-1])):
                i[j + 1] += i[0] * lists[-1][j]
            i.pop(0)
    lists.reverse()
    answers = [lists[0][0]]
    for i in range(1, len(lists)):
        tmpans = lists[i][-1]
        for j in range(len(lists[i]) - 1):
            tmpans += lists[i][j] * answers[-1 - j]
        answers.append(tmpans)
    answers.reverse()
    return answers


# answers = solve([[2, 9, -3, 7, 8], [7, -2, 6, -1, -10], [-8, -3, 2, 5, 4], [0, 2, 1, 1, 0]])
