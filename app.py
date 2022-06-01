from poker import Range
from poker.hand import Combo

import holdem_calc
from holdem_calc import calculate_odds_villan

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from IPython.core.display import display, HTML

hero_odds = []
hero_range_odds = []

hero_hand = Combo('KsJc')
print(hero_hand)

flop = ["Qc", "Th", "9s"] 
board = flop
villan_hand = None 
exact_calculation = True 
verbose = True 
num_sims = 1 
read_from_file = None 

odds = holdem_calc.calculate_odds_villan(board, exact_calculation, 
                            num_sims, read_from_file , 
                            hero_hand, villan_hand, 
                            verbose, print_elapsed_time = True)

print(odds[0])