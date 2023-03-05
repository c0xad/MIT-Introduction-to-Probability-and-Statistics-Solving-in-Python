#Compute E(X)

#E(X) = Σ x*p(x)
#the probability mass function of X is: p(2k) = (1/2)^(k+1)
#where k is a non-negative integer.

p = 1/2  # probability of winning
k = 0    # initial value of k
sum = 0  # initialize the sum

while True:
    x = 2**k  # value of X for this round
    px = p**(k+1)  # probability of winning in this round
    sum += x*px  # add to the sum
    if px < 1e-10:  # if the probability is very small, stop
        break
    k += 1

print("Expected value of X is:", sum)
