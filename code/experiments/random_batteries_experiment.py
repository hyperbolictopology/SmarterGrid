
from code.algorithms import random_batteries
from code.classes import district

def experiment(district_number, number_of_runs):
    all_costs = []

    for i in range(number_of_runs):
        new_district = district.District(district_number)
        random_batteries.hill_climber_algorithm(new_district)
        all_costs.append(new_district.shared_cost)

    print(f'The average shared shared over {number_of_runs} runs is {sum(all_costs) / number_of_runs}')

    return
Give feedback
