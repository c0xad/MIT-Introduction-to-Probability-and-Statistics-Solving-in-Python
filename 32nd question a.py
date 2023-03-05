#Suppose I play a gambling game where I either win or lose k dollars. Suppose further
#that the chance of winning is p = .5.
#I employ the following strategy to try to guarantee that I win some money.
#I bet $1; if I lose, I double my bet to $2, if I lose I double my bet again. I continue until
#I win. Eventually I’m sure to win a bet and net $1 (run through the first few rounds and
#you’ll see why this is the net).
#If this really worked casinos would be out of business. Our goal in this problem is to
#understand the flaw in the strategy. Let X be the amount of money bet on the last game (the one I win). X takes values
#1, 2, 4, 8, . . . . Determine the probability mass function for X. That is, find p(2k), where k
#is in {0, 1, 2, . . . } 

# Solution ; Y takes values 0, 1, 2, 3, ....
#  The probability of losing k - 1 times in a row is (1/2)^(k-1), and the probability of winning on the kth bet is 1/2. 
# betting 2^(k-1) dollars is: p(2^(k-1)) = (1/2)^k

#probability mass function for X is:
#p(2k) = p(2^(k-1)) - p(2^k)
# = (1/2)^(k-1) - (1/2)^k
# = (1/2)^k

import numpy as np

p = 0.5  # probability of winning
k_max = 10  # maximum number of rounds to consider

# initialize the pmf
pmf = np.zeros(2*k_max)

# calculate the pmf for each value of k
for k in range(1, k_max+1):
    pmf[2*k-2] = (1/2)**(k-1) - (1/2)**k

print("Probability Mass Function for X:")
for i, p in enumerate(pmf):
    print("p({}): {:.4f}".format(2*i+2, p))
