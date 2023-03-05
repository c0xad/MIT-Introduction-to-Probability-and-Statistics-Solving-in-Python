#Suppose 100 people all toss a hat into a box and then proceed to randomly pick out
#a hat. What is the expected number of people to get their own hat back.

#E(X) = ∑i=0 to n P(X=i) * i
#  For i = 0
# P(X=0) = !n / n!

#For i > 0
#P(X=i) = (-1)^i * C(n,i) * !n-i / n!

from math import factorial as fact

def derangement(n):
    """
    Compute the number of derangements of n items.
    """
    return round(fact(n) / (2.71828 ** n))

def expected_num_match(n):
    """
    Compute the expected number of people who get their own hat back,
    given n people and n hats.
    """
    exp = 0
    for i in range(n+1):
        if i == 0:
            p = derangement(n) / fact(n)
        else:
            p = (-1)**i * fact(n) / (fact(i) * fact(n-i)) * derangement(n-i) / fact(n)
        exp += p * i
    return exp

n = 100  # example value
print("Expected number of people who get their own hat back: {:.2f}".format(expected_num_match(n)))
