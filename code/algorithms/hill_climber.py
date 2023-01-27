from code.algorithms.random import random_routes
from code.classes import district
import random

'''
Pseudo code from the lecture:

Kies een random start state
Herhaal tot na N-keer niet meer verbetert:
    Doe een kleine random aanpassing
    Als de state is verslechterd:
        Maak de aanpassing ongedaan
'''

def hill_climber(district, number_of_iterations = 100):
    # Initialize random solution
    start_state = random.random_routes(district)

    for i in range(number_of_iterations):
        # Makes a copy of the district to work with
        district_copy = district.copy() # TODO find out, Deep copy or not?

        # TODO think of mutations that help improve the routes


        # TODO Calculate new cost


        # TODO compare costs
