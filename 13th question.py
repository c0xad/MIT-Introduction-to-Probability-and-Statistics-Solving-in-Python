#More cards! Suppose you want to divide a 52 card deck into four hands with 13 cards
#each. What is the probability that each hand has a king?

#P(A and B and C and D) = (4/52) * (3/51) * (2/50) * (1/49) = 0.000000432
#This means that the probability of each hand having a king is very low, at approximately 1 in 2.3 million.

p_A = 4/52
p_B_given_A = 3/51
p_C_given_AB = 2/50
p_D_given_ABC = 1/49

p_ABCD = p_A * p_B_given_A * p_C_given_AB * p_D_given_ABC

print("Probability of each hand having a king:", p_ABCD)
