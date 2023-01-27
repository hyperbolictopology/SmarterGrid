from code.classes import district
import numpy as np
import random


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def update_battery_capacity(house, battery):
    battery.current_capacity += house.output

# this one unfortunately does not work as fast random (if it works at all)
def nearest_available_battery(house, battery_list):
    """
    This function takes a house and a list of batteries as input, and returns
    the index of the nearest battery that has enough capacity to connect to the
    house. If there is no such battery, it returns index of -1.
    """
    distances = {}

    # Loop over every battery in the list
    for i in range(len(battery_list)):

        # Check if the current battery has enough capacity to connect to the house
        if battery_list[i].current_capacity + house.output < battery_list[i].max_capacity:
            distances[i] = manhattan_distance(house.pos_x, house.pos_y, battery_list[i].pos_x, battery_list[i].pos_y)

    # If there are no available batteries, return index -1
    if len(distances) < 1:
        return -1

    # Find the nearest one, update its capacity, and return it
    nearest_battery_index = min(distances, key=distances.get)
    update_battery_capacity(house, battery_list[nearest_battery_index])
    return nearest_battery_index

def random_available_battery(house, battery_list):
    # Randomize order of battery list
    random.shuffle(battery_list)

    # Loop over every battery in the list
    for i in range(len(battery_list)):

        # Check if battery has capacity left for the house output
        if battery_list[i].current_capacity + house.output < battery_list[i].max_capacity:

            # Update battery max_capacity
            update_battery_capacity(house, battery_list[i])

            # Returns the battery index that has enough capacity
            return i

    # Only returns -1 when there are no batteries available
    return -1

def create_route(house, battery):
    '''
    First goes right or left in the direction of the battery. Then goes up or down.
    '''
    x = house.pos_x
    y = house.pos_y

    # If the cable is left from the battery, the route goes right
    while x < battery.pos_x:
        x += 1
        house.cables.add_cable_segment((x - 1, y), (x, y))
        if x == battery.pos_x:
            break
    # If the cable is right from the battery, the route goes left
    while x > battery.pos_x:
        x -= 1
        house.cables.add_cable_segment((x + 1, y), (x, y))
        if x == battery.pos_x:
            break

    # If the cable is under from the battery, the route goes up
    while y < battery.pos_y:
        y += 1
        house.cables.add_cable_segment((x, y - 1), (x, y))
        if y == battery.pos_y:
            break

    # If the cable is above from the battery, the route goes down
    while y > battery.pos_y:
        y -= 1
        house.cables.add_cable_segment((x, y + 1), (x, y))
        if y == battery.pos_y:
            break

def create_all_routes(district):
    '''
    Creates routes for all houses to available batteries and calculates the
    cost for the overall district.
    '''

    # Keep track of houses that are connected with a battery
    all_connected = False
    connected_houses_count = 0

    # Keeps trying until it creates routes for all houses
    while not all_connected:

        # Reset if there was a dead end
        district.reset_grid()
        connected_houses_count = 0

        # For each house, find a random available battery
        for house in district.houses:
            chosen_battery_index = random_available_battery(house, district.batteries)

            # If battery index is -1, start the loop again!
            if chosen_battery_index == -1:
                #print('trying again')
                break

            # If loop is not broken, there is a house-battery connection!
            connected_houses_count += 1

            # It will create a route between house and battery
            create_route(house, district.batteries[chosen_battery_index])

            # Check if all houses are connected to break the while-loop
            if connected_houses_count == len(district.houses):
                all_connected = True


    # Calculate the cost
    district.calculate_own_cost()
    district.calculate_shared_cost()
