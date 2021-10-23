"""
Name: Lisa Mekonnen
Learning Objectives: To generate visual art with markov chains!
Language: Python
Dependencies: numpy
"""

import numpy as np
from PIL import Image
import glob

class MarkovMenu:
    def __init__(self, transition_matrix):
       """ Simulate a injera (dinner) plate that relies on simple Markov chain
           Args: transition_matrix(dict): transition probablities 
       """
       self.transition_matrix = transition_matrix
       self.dishes = list(transition_matrix.keys())

    def get_next_dish(self, current_dish):
        """ Decides which dish will be served with the current dish
            Args: current_dish(str): the current dish being served
        """
        return np.random.choice(self.dishes, p = [self.transition_matrix[current_dish][next_dish] \
            for next_dish in self.dishes])

    def create_dinner(self, current_dish, amount_of_dishes):
        """ Generate several dishes on one plate
            Arguments: current_dish (str): the dish at dinner we currently have & amount_of_dishes(int): how many dishes on one plate
        """
        dinner = []

        while len(dinner) < amount_of_dishes:
            next_dish = self.get_next_dish(current_dish)
            dinner.append(next_dish)
            current_dish = next_dish
        return dinner

    def get_pics_of_dishes(self):
        """
        Make a method that will display all 10 options for 3 dish option or 2 dish option
         (you can either 
        have 3 dishes in 1 meal, 1 dish in 1 meal, or 2 of the meals 
        in one meal)
        """
        # use glob for someone who does not have access to your computer
        totomo = Image.open(r"C:\Users\lisamekonnen\Desktop\cc-github\mission-3\"totomo.jpg")
        hamli = Image.open(r"C:\Users\lisamekonnen\Desktop\cc-github\mission-3\"hamli.jpg")
        dorho = Image.open(r"C:\Users\lisamekonnen\Desktop\cc-github\mission-3\"dorho.jpg")
        totomo.show()


def main():
    dish_options = MarkovMenu({
        # Totomo is a lentil dish and it is usual serve with hamli or sometimes with dorho
        # Dorho is a heavy dish and it is usually deserved with hamli or somtimes totomo
        # Hamli is a side dish to most common dishes (totomo and dorho)
        "Totomo": {"Totomo": 0.2, "Hamli": 0.7, "Dorho": 0.1},
        "Dorho": {"Totomo": 0.3, "Hamli": 0.6, "Dorho": 0.1},
        "Hamli": {"Totomo": 0.4, "Hamli": 0.2, "Dorho": 0.4}
    })

    totomo = Image.open(r"C:\Users\lisamekonnen\Desktop\cc-github\mission-3\"totomo.jpg")
    totomo.show()

    # print(dish_options.transition_matrix)
    # print(dish_options.dishes)
    # print(dish_options.get_next_dish("Totomo"))
    # print(dish_options.create_dinner("Totomo", 5))





if __name__ == "__main__":
    main()

