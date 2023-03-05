#Some games, like tennis or ping pong, reach a state called deuce. This means that
#the score is tied and a player wins the game when they get two points ahead of the other
#player. Suppose the probability that you win a point is p and this is true independently for
#all points. If the game is at deuce what is the probability you win the game?

# P(A|B) = (p^2 / (p^2 + (1-p)^2)) * 2 / (2 * p * (1-p))
# P(A|B) = p^2 / (2 * p * (1-p))

p = 0.6  # probability of winning a point
p_B_given_A = 1/2  # probability of winning the game from a deuce
p_A = p**2 / (p**2 + (1-p)**2)  # probability of winning the game from a deuce
p_B = 2 * p * (1-p)  # probability of the game being at deuce

p_A_given_B = (p_A * p_B_given_A) / p_B

print("Probability of winning the game from a deuce:", p_A_given_B)
