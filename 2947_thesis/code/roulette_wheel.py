#roulette wheel algorithm 
import random
def roulette_wheel_select(prob_array):
    total_prob = sum(prob_array)
    random_prob =random.uniform(0,total_prob) 
    current=0
    for i, prob in enumerate(prob_array): 
        current+=prob
        if current>random_prob:
            return i

