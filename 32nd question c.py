#Use your answer in part (b) to explain why the stategy is a bad one.

#E(X) = Σ x * p(x), where the sum is over all possible values of X and p(x) is the probability mass function of X.
#p(X = 1) = 1/2
#p(X = 2) = (1/2)^2
#p(X = 4) = (1/2)^3
#p(X = 8) = (1/2)^4

#compute E(X) as: E(X) = 11/2 + 2(1/2)^2 + 4*(1/2)^3 + 8*(1/2)^4 + ...
#formula for the sum of an infinite geometric series to get: E(X) = 1/(1 - 1/2) = 2

#So the expected value of X is 2, which means that the player will bet twice before winning.
#The strategy's flaw is that the player's bets can grow very quickly, and the player may run out of money before winning a bet.
#For example, after losing six consecutive bets, the player will need to bet $64 to win $1, and if they lose that bet, they will need to bet $128, and so on.
#The player may run out of money or reach the table's maximum bet before winning a bet, resulting in a large loss.
#As a result, this strategy is not a good way to ensure long-term success. 


import numpy as np

k = 1  # the amount of money won or lost in each round
p = 0.5  # the probability of winning
E = np.sum([(2**i)*k*p*(1-p)**i for i in range(1000)])  # compute the expected value of X up to 2^1000
print("Expected value of X: ", E)
