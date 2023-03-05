#Suppose that buses arrive are scheduled to arrive at a bus stop at noon but are
#always X minutes late, where X is an exponential random variable with probability density
#function fX (x) = λe−λx . Suppose that you arrive at the bus stop precisely at noon.
#Compute the probability that you have to wait for more than five minutes for the bus to arrive.

#the arrival time of the bus is given by T = 12:00 PM + X.
#P(T > 12:05 PM) = P(X > 5)
#use exponential probability density function fX(x) = λe^(-λx) ; P(X > 5) = ∫5∞ λe^(-λx) dx
# P(X > 5) = -e^(-λx) |5∞ + ∫5∞ λe^(-λx) dx = e^(-5λ)

import math

# Parameters
arrival_time = 12 * 60 # Arrival time in minutes
waiting_time = 5 # Waiting time in minutes
lmbda = 1/10 # Rate parameter for exponential distribution

# Compute probability
prob_wait = math.exp(-lmbda*waiting_time)

print(f"The probability of waiting for more than {waiting_time} minutes is: {prob_wait:.4f}")
