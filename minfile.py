# 1.1
import random
import numpy as np
import matplotlib.pyplot as plt

# Create a function for the game
def game_play():
    '''Returns win or loss of the gamer'''
    winning = -1
    if random.randrange(0, 12) == 11:
        winning += 10
    return winning

# Playing the game 600 times
def a_round_of_gameplay():
    netto_money = 100
    for i in range (600):
        netto_money += game_play()
    return netto_money

# Create a vector that contains the values of playing the game 1_000_000 times
def vector_creator():
    y = []
    for i in range(1_000_0):
        y.append(a_round_of_gameplay())
    return y

# Alternative method for generating the game_samples that is more efficient
def alt_vector_creator():
    # We create a 1_000_000 random vectors with the amount of times that a person would win out of 600
    vector = np.random.binomial(600, 1/12, 1_000_000)
    vector = vector * 10 # We then multiply the amount of times won by the winning to get the total winnings
    vector = vector - 500 # We then subtract the fixed cost, 100 starting money and 600 spent on playing
    return vector



# Create a histogram of the WINNINGS (but actually of the density distribution of the different winnings)
#vector = vector_creator()
vector = alt_vector_creator()
number_of_bins = 50
n, bins, patches = plt.hist(vector, number_of_bins, density=1)
plt.show()
exit()
#####################################################################################################################
# 1.2 Plot a Gaussian distribution curve over the graph
#####################################################################################################################

# We calculate the mean and the standard deviation using pythons built-in formula

mean = np.mean(vector)
# Should be around 0
sd = (np.var(vector))**(0.5)
# Should be around 10*(50*11/12)^(1/2)

# We then plot the curve

x = mean + sd * np.random.rand(1000)

number_of_bins = 50 # How large our "steps" are for our plot
n, bins, patches = plt.hist(vector, number_of_bins, density=1)
y = 1 / (np.sqrt(2 * np.pi) * sd) * np.exp(-0.5 * ((bins - mean) / sd) ** 2)

plt.plot(bins, y, '--')

plt.show()

#####################################################################################################################
# 1.3 Questions
#####################################################################################################################

# The gaussian distribution fits the distribution very well.
# To explain why both why it is centered around 0 and why the distribution fits the gaussian distribution (Bell curve)
# so well we should look att the mathematics.

# We have a binomialy distributed value which determines whether or not we win 10 kr.
# Since the game is repeated 600 indentendent times, we can use a specific case of the central limit theorem to
# to approximate the binomial distribution as Gaussian distribution. The general rule is that
# np(1-p)>10 in our case 600*1/12*11/12=600*11/12^2 = 46 roughly
# At this point we can stop and consider the expected value of one game (600 times).
# X is the expected money purely from winning and has an expected value n*p=600/12=50
# expected netto earning Y = 100 - 600 + X*10  where X follows Gaussian distribution (approx)
# That means that the variable Y also follow Gaussian distribution with a mean of -500 + 50*10 = 0
# This is why it is centered around 0.
# Repeating this experiment 1000000 independant times will, of course, also follow Gaussian distribution
# Which is why the curve fits the distribution.

#####################################################################################################################
# 1.4 The likelyhood of earning more than 100 kr
#####################################################################################################################

# For an accurate computation we want to sum all "stacks" starting with 101 and divide that by all possible outcomes.
# That will, however, be 1. As such, all we need to do is either take 1 - summarizing all stacks up to 100
# or summarize all stacks, starting with 101. Stacks = probability of certain netto earning.

# We have certain information from our histogram plot. "n" gives us a number of values for every bin
# "bins" describes the values that each n corresponds to.

# Step 1 is to identify which bin that contains 100
'''def bin_index_finder(bin):
    low_value_index = 0
    high_value_index = 0
    for i in bin:
        if bin[i]<100:
            low_value_index = i
        else:   # The first time we arrive here is when we have just passed 100. 
            high_value_index = i    # This will be the first value greater than 100
            break
    if (100 - bin[low_value_index]) < (bin[high_value_index] - 100):    # Checks which value is closest to 100
        return low_value_index  # And returns the index
    else:
        return high_value_index'''

def bin_index_finder(bin):
    for i in range(len(bin)):
        if bin[i] >= 100:  # finds the lowest value greater than 100 and returns the index. n[i] starts at value bin[i]
            return i

# Step 2 is to identify the size of each bin
def bin_size_finder(bin):
    return abs(bin[0]-bin[1])   # It should be the same for all values

# Step 3 is to summarize the value of n for all bins starting with the one above 100
def likelihood_summariser(n, bin):
    total = 0
    for i in range(bin_index_finder(bin), len(n)): # Starts at 100 and summarizes the above ones
        total += n[i]
    print(bin_index_finder(bin)*total)

likelihood_summariser(n, bins)

#####################################################################################################################
# 1.5 New game
#####################################################################################################################

# I make the assumption that I can calculate without generating 1000000 cases.
# The chances of success are 1/2 * 3/6 * 4/52 = 1/52
# We can formulate the banks winnings as Y = n - X*b
# Where X is the amount of times they win during n games. X is Binomially distributed with n=n and p=1/52
# Assuming that a lot of players play the game, n is a high number. We seek the expected value of the game to be higher
# than 0.
# E(Y) = E(n - X*b) = n - b* E(X) = n - b*n/52 = n * (1-b/52)
# We can plot the expected winnings per player (must be multiplied by n for absolute numbers).
# This number needs to be greater than 0 in order to expect profits from our gambling den. One sees that b<52

prize_money = np.arange(0, 200)
expected_income_per_customer = 1 - prize_money/52
plt.plot(prize_money, expected_income_per_customer)
plt.plot(52, 0, marker='o')
plt.show()

#####################################################################################################################
# 1.6 New game
#####################################################################################################################

def play_game():
    for i in range(10): # We repeat the game for every player
        y = []
        current_state = 0
        for i in range(1000):   # Each player plays 1000 times
            if random.randrange(0, 52) == 11:   # The chances of success are 1/52
                current_state = current_state - 50  # If they win, the bank looses 51-1=50
            else:
                current_state += 1  # Else the bank wins 1
            y.append(current_state) # We append the current bank_status to follow the status
        plt.plot(y)
    plt.show()
play_game()

#####################################################################################################################
# 1.7 Question
#####################################################################################################################
# Different in different runs, but we made money from 8 people in the first run

#####################################################################################################################
# 1.8 Tweeeet
#####################################################################################################################
def one_coin():
    for i in range(10):
        if random.randrange(0, 2) == 1:
            return 0
    return 1

def playing_cointoss():
    result_vector = []
    for i in range(10000):
        number_of_perfect_coins = 0
        for i in range(0, 1024):    # This is 1024 people flipping 10 coins each. Appends 1 if at least one person succeeded, else 0
            number_of_perfect_coins += one_coin()
        if number_of_perfect_coins > 0:
            result_vector.append(1)
        else:
            result_vector.append(0)
    print(np.mean(np.array(result_vector))) # The mean will be the average amount of wins

playing_cointoss()

