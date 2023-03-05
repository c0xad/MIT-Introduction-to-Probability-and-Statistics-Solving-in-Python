#Suppose that you have already waiting for 10 minutes. Compute the probability that
#you have to wait an additional five minutes or more.

#we have waited 10 minute and we have to wait 5 minutes or more;
# P(X ≥ 15 | X > 10)
#use bayes rule; P(X ≥ 15 | X > 10) = P(X > 15) / P(X > 10)
# compute the probability P(X > x) as: P(X > x) = ∫x∞ fX(t) dt ; where fX(t) is the probability density function of X

#When we substitute the given probability density function, we get: P(X > x) = ∫x∞ λe^(-λt) dt = e^(-λx)
# P(X ≥ 15 | X > 10) = P(X > 15) / P(X > 10) = e^(-15λ) / e^(-10λ) = e^(-5λ)

import math

# Define lambda
lam = 1/10

# Compute probability using exponential distribution cdf
prob = math.exp(-5*lam)

print("Probability of waiting for an additional 5 minutes or more:", prob)
