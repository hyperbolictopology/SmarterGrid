"""
Advanced #5

Randomly intializes new battery locations for a given district, updating battery locations optimally using a hillclimber algorithm.

"""

from code.algorithms.valid_shortest_route import random_shortest_route
from code.classes import district
import random

def initialize_random_batteries(district):
    # Loops over every battery in the district and changes its location randomly
    for battery in district.batteries:
        # changes location but not letting the batteries be too close to the grids borders
        battery.pos_x = random.randint(5, 45)
        battery.pos_y = random.randint(5, 45)

def battery_hill_climber_algorithm(district, number_of_iterations = 100):
    # initializes best cost
    best_cost = district.shared_cost()

    for i in range(number_of_iterations):
        # Makes a copy of the district to work with
        district_copy = district.copy()

        # Calls init_random_batteries function
        initialize_random_batteries(district_copy)

        # Creates new random routes, using the new battery allocation
        random_shortest_route(district_copy)

        # Calculates new cost
        new_cost = district_copy.shared_cost()

        # Compares costs and updates district if the new battery arrangement produces lower costs
        if new_cost < best_cost:
            district = district_copy
            best_cost = updated_cost

        return district
