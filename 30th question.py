#Compute the expectation and variance of a Bernoulli(p) random variable.
# Expectation: E[X] = p ; Variance: Var[X] = p(1-p)

import numpy as np

p = 0.6  # probability of success

# create a Bernoulli random variable with parameter p
X = np.random.binomial(n=1, p=p)

# calculate the expectation and variance
E_X = np.mean(X)
Var_X = np.var(X)

print("Expectation:", E_X)
print("Variance:", Var_X)
