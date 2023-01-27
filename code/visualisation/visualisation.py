import matplotlib.pyplot as plt
from code.classes import district


def visualise(district):
    # Lists for the plot
    list_x = []
    list_y = []
    list_colour = []

    # Add the location and color of each input to the lists
    for input in district.grid_inputs:
        list_x.append(input.pos_x)
        list_y.append(input.pos_y)
        list_colour.append(input.colour)

    # Change the figure size
    plt.figure(figsize=(9,9))

    # low priority TODO: find a way to plot only the decimals ticks while having
    # a grid for every unit

    # Make scatter plot with grid
    plt.grid(which = 'both')
    plt.title(f'District {district.district_number} (with shared cost of {district.shared_cost})')
    plt.scatter(list_x, list_y, c = list_colour, zorder = 3)
    plt.xticks(range(min(list_x), max(list_x) + 1), fontsize = 7)
    plt.yticks(range(min(list_y), max(list_y) + 1), fontsize = 7)

    # Add the plot of the cables

    for house in district.houses:

        x, y = zip(*house.cables.get_route_list())
        plt.plot(x, y, c = 'blue')

    plt.show()
