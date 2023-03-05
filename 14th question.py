#Suppose you are taking a multiple-choice test with c choices for each question. In
#answering a question on this test, the probability that you know the answer is p. If you
#don’t know the answer, you choose one at random. What is the probability that you knew
#the answer to a question, given that you answered it correctly?

#P(B) = P(B|A) * P(A) + P(B|not A) * P(not A)
# = 1 * p + (1/c) * (1-p)
# = (cp + 1 - p) / c

c = 4  # number of choices
p = 0.7  # probability of knowing the answer
p_not_A = 1 - p  # probability of not knowing the answer
p_B_given_A = 1  # probability of answering correctly given that the test taker knows the answer
p_B_given_not_A = 1/c  # probability of answering correctly given that the test taker doesn't know the answer

p_B = p_B_given_A * p + p_B_given_not_A * p_not_A
p_A_given_B = p / ((c * p) + (1 - p))

print("Probability that the test taker knew the answer given that they answered correctly:", p_A_given_B)
