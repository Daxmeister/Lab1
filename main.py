# Lab 1
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def game_play():
    '''Returns win or loss of the gamer'''
    winning = -1
    if random.randrange(0, 12) == 11:
        winning += 10
    return winning

def a_round_of_gameplay():
    netto_money = 100
    for i in range (600):
        netto_money += game_play()
    return netto_money
'''
class Dictionary_of_categories():
    def __init__(self):
        self.dictionary = {}
        for i in range(-500, 5501):
            self.dictionary[i] = 0

    #def append_to_dict(self, number):'''
'''def vector_generator():
    np.random.seed(10**7)
    mu = 0
    sigma = (50*11/12)**(0.5)/10
    return mu + sigma * np.random.randn(1000)'''

def create_vector_w_all_results():
    y = []
    for i in range(1_000_0):
        y.append(a_round_of_gameplay())
    return y

def present_distribution_from_vector_old(vector):
    unique_elements, counts_elements = np.unique(vector, return_counts=True)
    plt.stem(unique_elements, counts_elements)
    plt.show()

def present_distribution_from_vector(vector):
    #unique_elements, counts_elements = np.unique(vector, return_counts=True)
    number_of_bins = 50
    n, bins, patches = plt.hist(vector,number_of_bins, density=1)
    plt.show()

#present_distribution_from_vector(create_vector_w_all_results())

# 1.2
# Försöket som upprepas 600ggr är binomialfördelat med n=600 och p=1/12.
# Det får approximeras som normalfördelat pga np(1-p)>10
# Försöket approximeras då som normalfördelat med my=50 och sigma (50*11/12)^(1/2)
# Vi kan då skapa en ny SV Z som motsvarar vinsten av ett experiment och också är normalfördelad med
# my=0 och sigma=10*(50*11/12)^(1/2)

# Det nedan gör vi inte
# Vi skapar nu en stokastisk variabel för att upprepa experimentet 1000_000 ggr som vi kallar W
# W är normalfördelad med my=0 och sigma (50*11/12)^(1/2) / 100
# Med denna kunskap kan vi plotta ut normalfördelningen

#import numpy as np
#import matplotlib.pyplot as plt
from scipy.stats import norm
#import statistics

def present_distribution_from_vector_with_normaldistribution_curve(vector):
    mean = 0
    sd = (50 * 11 / 12) ** (1 / 2) * 10
    x = mean + sd * np.random.rand(1000)

    number_of_bins = 50
    n, bins, patches = plt.hist(vector, number_of_bins, density=1)
    y = (1 / np.sqrt(2 * np.pi) * sd ) * np.exp(-0.5 * (1 / sd * (bins - mean))**2)

    plt.plot(bins, y, '--')

    plt.show()

present_distribution_from_vector_with_normaldistribution_curve(create_vector_w_all_results())