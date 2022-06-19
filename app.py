from poker import Range
from poker.hand import Combo

import holdem_calc
from holdem_calc import calculate_odds_villan

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# hero_odds = []
# hero_range_odds = []
while(True) :

    hand = input('your hand')
    hero_hand = Combo(hand)

    print(hero_hand)

    def cal(store = []):
        
        board = input("Enter board separated by space").split() + store

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

        contioune = input('contioune?')
        if contioune == 'x': 
            return
        if contioune == 'c':
            cal(board)
    cal()