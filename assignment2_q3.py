import cvxpy as cp
import numpy as np


def egalitarian_division(value_matrix):
    """
    Solves the Egalitarian Division problem using convex optimization.

    Each row in value_matrix represents an agent, and each column represents a resource.
    The value at (i, j) represents how much agent i values resource j.

    This function prints how much of each resource is allocated to each agent in a way
    that maximizes the minimum value any agent receives.

    >>> egalitarian_division([[81, 19, 1], [70, 1, 29]])
    Agent #1 gets 0.53 of resource #1, 1.00 of resource #2, 0.00 of resource #3.
    Agent #2 gets 0.47 of resource #1, 0.00 of resource #2, 1.00 of resource #3.
    """
    n, m = len(value_matrix), len(value_matrix[0])
    values = np.array(value_matrix)

    # Define variables: fraction of each resource allocated to each agent
    X = cp.Variable((n, m), nonneg=True)

    # Egalitarian division maximizes the minimum value any agent receives
    min_value = cp.Variable()

    # Constraints:
    constraints = [cp.sum(X, axis=0) <= 1]  # Resource usage limits

    for i in range(n):
        constraints += [cp.sum(cp.multiply(X[i], values[i])) >= min_value]

    # Solve the optimization problem
    problem = cp.Problem(cp.Maximize(min_value), constraints)
    problem.solve()

    # Display results
    for i in range(n):
        allocation = X.value[i]
        allocation_str = ", ".join([f"{allocation[j]:.2f} of resource #{j + 1}" for j in range(m)])
        print(f"Agent #{i + 1} gets {allocation_str}.")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    print("\nExample 1: Mixed preferences")
    value_matrix = [[81, 19, 1], [70, 1, 29]]
    egalitarian_division(value_matrix)
    print()

    print("Example 2: Agent 1 dominates most resources")
    value_matrix = [[90, 90, 90], [1, 1, 1]]
    egalitarian_division(value_matrix)
    print()

    print("Example 3: Agent 2 dominates one important resource")
    value_matrix = [[10, 5, 2], [2, 3, 100]]
    egalitarian_division(value_matrix)
    print()

    print("Example 4: Inverse valuations (one likes what the other hates)")
    value_matrix = [[100, 0, 50], [0, 100, 50]]
    egalitarian_division(value_matrix)
    print()

    print("Example 5: Sparse interests")
    value_matrix = [[1, 0, 0], [0, 1, 1]]
    egalitarian_division(value_matrix)
    print()
