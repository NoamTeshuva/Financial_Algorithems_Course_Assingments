import cvxpy as cp
import numpy as np

def egalitarian_division(value_matrix):
    n, m = len(value_matrix), len(value_matrix[0])
    values = np.array(value_matrix)

    # Define variables: fraction of each resource allocated to each agent
    X = cp.Variable((n, m), nonneg=True)

    # Egalitarian division maximizes the minimum value any agent receives
    min_value = cp.Variable()

    # Constraints:
    constraints = []

    # Each resource can be fully allocated at most once
    constraints += [cp.sum(X, axis=0) <= 1]

    # Each agent must get at least min_value
    for i in range(n):
        constraints += [X[i, :] @ values[i, :].T >= min_value]

    # Optimization problem
    problem = cp.Problem(cp.Maximize(min_value), constraints)

    # Solve the problem
    problem.solve()

    # Display results
    for i in range(n):
        allocations = X.value[i]
        alloc_str = ", ".join([f"{allocations[j]:.2f} of resource #{j+1}" for j in range(m)])
        print(f"Agent #{i+1} gets {alloc_str}.")


# Example usage:
value_matrix = [[81,19,1],[70,1,29]]
egalitarian_division(value_matrix)
