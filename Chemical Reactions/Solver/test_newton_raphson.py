import autograd as ag
import autograd.numpy as np
from scipy import linalg, sparse

# define the matrix of unknowns each comma represents a new equation, x represents the vector of unknowns
from scipy.sparse.linalg import spsolve


def f(x, rhs):
    output = np.array([x[0] + (2 * x[1]) - rhs[0], x[0] ** 2 + 4 * x[1] ** 2 - rhs[1]])
    return output


guess = np.array([1, 2], dtype=float)  # provide an initial guess
rhs = np.array([2, 4], dtype=float)  # provide a vector of right hand sides

newton_tol = 1e-6
err = np.inf
while err > newton_tol:
    val = -f(guess, rhs)
    jac = ag.jacobian(f)(guess, rhs)
    dx = linalg.solve(jac, val)
    guess = guess + dx
    err = np.sqrt(np.sum(val ** 2))

# using a sparse matrix for the Jacobian. Other linear problem solution methods can be found here
# https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html
newton_tol = 1e-6
err = np.inf
iteration_count = 0
while err > newton_tol:
    val = -f(guess, rhs)
    iteration_count = iteration_count + 1
    jac = ag.jacobian(f)(guess, rhs)
    jac = sparse.csr_matrix(jac)
    dx = spsolve(jac, val)
    guess = guess + dx
    err = np.sqrt(np.sum(val ** 2))


# provides a more generalized function
def general_function(x, rhs, coeff1, coeff2, power1, power2):
    output = np.array([coeff1[0] * x[0] ** power1[0] + (coeff2[0] * x[1] ** power2[0]) - rhs[0],
                       coeff1[1] * x[0] ** power1[1] + coeff2[1] * x[1] ** power2[1] - rhs[1]])
    return output


guess = np.array([1, 2], dtype=float)
rhs = np.array([-2, 0], dtype=float)
coeff1 = np.array([3, 2], dtype=float)
coeff2 = np.array([-1, -1], dtype=float)
power1 = np.array([1, 2], dtype=float)
power2 = np.array([1, 1], dtype=float)

newton_tol = 1e-6
err = np.inf
iteration_count = 0
while err > newton_tol:
    val = -general_function(guess, rhs, coeff1, coeff2, power1, power2)
    iteration_count = iteration_count + 1
    jac = ag.jacobian(general_function)(guess, rhs, coeff1, coeff2, power1, power2)
    jac = sparse.csr_matrix(jac)
    dx = spsolve(jac, val)
    guess = guess + dx
    print(err)
    err = np.sqrt(np.sum(val ** 2))



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


answers = solve([[2, 9, -3, 7, 8], [7, -2, 6, -1, -10], [-8, -3, 2, 5, 4], [0, 2, 1, 1, 0]])