# Suppose that X ∼ Bin(n, 0.5). Find the probability mass function of Y = 2X 

# P(X = k) = (n choose k) * (1/2)^n
# if probability mass function of Y = 2X; we use P(Y = j) = P(2X = j) = P(X = j/2)
# P(Y = j) = (n choose j/2) * (1/2)^n

import math

n = 10  # number of trials
p = 0.5  # probability of success
pmf_Y = {}  # dictionary to store the probability mass function of Y

for j in range(0, 2*n+1, 2):
    pmf_Y[j] = math.comb(n, j//2) * (p**j) * ((1-p)**(n-j//2))

print("Probability mass function of Y:")
for j, prob in pmf_Y.items():
    print("P(Y = {}): {:.6f}".format(j, prob))
