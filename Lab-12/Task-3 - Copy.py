from scipy.optimize import linprog

# Coefficients of the profit function (maximize 6A + 5B, but linprog minimizes -6A - 5B)
c = [-6, -5]  # Negate because linprog does minimization

# Inequality constraints (A and B >= 0 by default in linprog)
# Each unit of A requires 1 Milk, 3 Choco
# Each unit of B requires 1 Milk, 2 Choco
# Constraints:
# A + B <= 5 (Milk)
# 3A + 2B <= 12 (Choco)

A = [
    [1, 1],    # Milk constraint
    [3, 2],    # Choco constraint
]

b = [5, 12]

# Bounds for A and B (can't be negative)
x0_bounds = (0, None)
x1_bounds = (0, None)

# Solve using linprog
res = linprog(
    c,
    A_ub=A,
    b_ub=b,
    bounds=[x0_bounds, x1_bounds],
    method='highs'
)

if res.success:
    A_opt, B_opt = res.x
    # Since we're producing discrete units, round down to nearest integer
    A_opt_int = int(A_opt)
    B_opt_int = int(B_opt)
    max_profit = 6 * A_opt_int + 5 * B_opt_int
    print(f"Optimal units to produce: A = {A_opt_int}, B = {B_opt_int}")
    print(f"Maximum profit: Rs {max_profit}")
else:
    print("Optimization failed:", res.message)
