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
