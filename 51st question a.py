#Let X be independent random variables where X ∼ N (2, 5) and Y ∼ N (5, 9) (we use the
#notation N (μ, σ2)). Let W = 3X − 2Y + 1. Compute E(W ) and Var(W ).

#E(W) = E(3X - 2Y + 1) = 3E(X) - 2E(Y) + E(1) = 3(2) - 2(5) + 1 = -3
#Var(W) = Var(3X - 2Y + 1) = 9Var(X) + 4Var(Y) + Var(1) - 12Cov(X,Y)

#Cov(X,Y) = E(XY) - E(X)E(Y)
#Cov(X,Y) = E(XY) - E(X)E(Y) = E(X)E(Y) - E(X)E(Y) = 0
#Var(W) = 9Var(X) + 4Var(Y) + Var(1) = 9(5) + 4(9) + 0 = 81
#E(W) = -3 ; Var(W) = 9

import numpy as np

# Given parameters
mu_x = 2
sigma_x = np.sqrt(5)
mu_y = 5
sigma_y = np.sqrt(9)

# Compute E(W)
E_W = 3 * mu_x - 2 * mu_y + 1
print("E(W) =", E_W)

# Compute Var(W)
Var_W = (3 ** 2) * sigma_x ** 2 + (-2 ** 2) * sigma_y ** 2
print("Var(W) =", Var_W)

