import autograd as ag
import autograd.numpy as np
from scipy import linalg


# define the matrix of unknowns each comma represents a new equation, x represents the vector of unknowns
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
    err = np.sqrt(np.sum(val**2))
