#Suppose that X has probability density function fX (x) = λe−λx for x ≥ 0.
#Compute the cdf, FX (x).

#(CDF) of X is defined as FX(x) = P(X ≤ x)
# probability density function; FX(x) = ∫[0, x] fX(t) dt = ∫[0, x] λe^(−λt) dt
#FX(x) = [-e^(-λt)]_[0, x]
#FX(x) = 1 - e^(-λx) therefore; CDF of X is FX(x) = 1 - e^(-λx).

import scipy.integrate as spi
import numpy as np

def f(x, lambd):
    return lambd * np.exp(-lambd * x)

def cdf(x, lambd):
    res, _ = spi.quad(f, 0, x, args=(lambd,))
    return res

lambd = 1.5  # example value
x = 2.0  # example value
print("FX({}) = {:.4f}".format(x, cdf(x, lambd)))

# this is for the given value of the lambda. another for didnt given value of the lambda 
#import math
#def cdf_X(x, lambd):
#   return 1 - math.exp(-lambd*x)
