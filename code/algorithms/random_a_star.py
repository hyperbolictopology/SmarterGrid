from code.classes import district
import random
import heapq

'''
This is exactly the same as the random except for the way a route is made from
a house to a battery. Here, the A* is used. I thought it might come in handy
with some reconstruction (e.g. lowering the cost if it chooses to take the
route with overlap). But maybe not.
'''


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

def a_star_route(house, battery):
    start = (house.pos_x, house.pos_y)
    goal = (battery.pos_x, battery.pos_y)

    # Create a priority queue list and evaluated coordinates set
    queue = []
    evaluated = set()

    # Add the starting coordinate to the queue
    heapq.heappush(queue, (0, (start)))

    # Create a dictionary to store the previous location
    came_from = {start: None}

    # Create a dictionary to store the cost of the route
    costs_so_far = {start: 0}

    while queue:
        # Current location (coordinate)
        current = heapq.heappop(queue)[1]

        # Make sure to only check this coordinate once
        evaluated.add(current)

        # Generate the neighbours of the current coordinate
        neighbours = []

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current
            neighbour = (x + dx, y + dy)

            # The road goes forward
            if neighbour not in evaluated:
                neighbours.append(neighbour)

        # Update the costs and parents of the neighbours
        for neighbour in neighbours:

            # Check whether the neighbour has not been visited before
            if neighbour not in costs_so_far:

                # Each adjencent step (i.e. towards a neighbour) costs 1
                costs_so_far[neighbour] = costs_so_far[current] + 1

                # Adding priority (cost + distance to goal)
                priority = costs_so_far[current] + 1 + manhattan_distance(goal[0], neighbour[0], goal[1], neighbour[1])
                heapq.heappush(queue, (priority, neighbour))

                # Keeping track of the route
                came_from[neighbour] = current

        # If we have reached the goal, update the complete route
        if current == goal:
            route = []

            while current != start:
                route.append((current, came_from[current]))
                current = came_from[current]

            route.append((start, current))
            route.reverse()

            for segment in route:
                house.cables.add_cable_segment(segment[0], segment[1])

            return

def create_all_routes(district):
    '''
    Creates routes with A* from a house to an available battery.
    '''

    # Keep track of houses that are connected with a battery
    all_connected = False
    connected_houses_count = 0

    # Keeps trying until it creates routes for all houses
    while not all_connected:

        # Start the for-loop again
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
            a_star_route(house, district.batteries[chosen_battery_index])

            # Check if all houses are connected to break the while-loop
            if connected_houses_count == len(district.houses):
                all_connected = True


    # Calculate the cost
    district.calculate_own_cost()
    district.calculate_shared_cost()
