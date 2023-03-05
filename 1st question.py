#A full house in poker is a hand where three cards share one rank and two cards share
#another rank. How many ways are there to get a full-house? What is the probability of
#getting a full-house?

import math

# Calculate the number of ways to get a full house
full_house = (13 * math.comb(4, 3) * 12 * math.comb(4, 2))

# Calculate the probability of getting a full house
total_hands = math.comb(52, 5)
prob_full_house = full_house / total_hands

# Print the results
print("Number of ways to get a full house:", full_house)
print("Probability of getting a full house:", prob_full_house)