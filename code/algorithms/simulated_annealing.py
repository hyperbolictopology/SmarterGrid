import random

def initialize_random_state(district):
    # Initializes an empty list to store the cables
    cables = []

    # Iterate through all houses in the district
    for house in district.houses:
        # Chooses a random battery to connect the house to
        battery = random.choice(district.batteries)
        # Appends a tuple of the house and battery to the cables list
        cables.append((house, battery))

    return cables

def calculate_cost(state, district):
    # Initializes a cost variable to store the total cost
    cost = 0

    # Iterates through all cables in the state
    for cable in state.cables:
        # Gets the house and battery for the current cable
        house, battery = cable
        # Calculates the Manhattan distance between the house and battery
        distance = abs(house[0] - battery[0]) + abs(house[1] - battery[1])
        # Adds the cost of the cable (9 per grid segment) multiplied by the distance to the total cost
        cost += distance * 9
    # Adds the cost of the batteries (5000 each) to the total cost
    cost += len(district.batteries) * 5000
    return cost

def simulated_annealing(district, max_iterations=10000, initial_temperature=100, cooling_rate=0.95):
    """This function takes in a district and runs a simulated annealing algorithm to optimize the cable arrangements, 
    inputs are district (class), the maximum number of iterations (int), the initial temperature (int), and the cooling rate (float). """
    
    # Initializes the current state as a random configuration of cables
    current_state = initialize_random_state(district)
    # Initializes the current cost as the cost of the current state
    current_cost = calculate_cost(current_state)
    # Initializes the best state and best cost as the current state and current cost
    best_state = current_state
    best_cost = current_cost

    # Sets the initial temperature
    temperature = initial_temperature

    # Repeats for the maximum number of iterations
    for i in range(max_iterations):
        # Creates a new state by making a small change to the current state
        new_state = make_small_change(current_state)
        # Calculate the cost of the new state
        new_cost = calculate_cost(new_state)
        # Calculatess the cost difference between the new state and the current state
        cost_difference = new_cost - current_cost

        # If the new state is better than the current state, always accept it
        if cost_difference < 0:
            current_state = new_state
            current_cost = new_cost
            # Updates the best state and best cost if the new state is better than the best state
            if new_cost < best_cost:
                best_state = new_state
                best_cost = new_cost
        # If the new state is worse than the current state, sometimes accept it
        else:
            # Calculates the acceptance probability
            acceptance_probability = math.exp(-cost_difference / temperature)
            # Generates a random number between 0 and 1
            random_number = random.uniform(0, 1)
            # If the random number is less than the acceptance probability, accept the new state
            if random_number < acceptance_probability:
                current_state = new_state
                current_cost = new_cost

        # Cools the temperature
        temperature *= cooling_rate

    return best_state, best_cost

