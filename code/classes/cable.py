class Cable():
    '''
    This class defines cables properties.
    '''
    def __init__(self):
        self.cable_segments = {} # Example: { 1: ((1,1), (1,2)), 2: ((1,2), (1,3)) }
        self.price = 9


    # A segment consists out of two adjacent points in the grid (start and end) and has a unique id
    def add_cable_segment(self, start, end, id):
        self.cable_segments[id] = (start, end)

    # Starts clean
    def clear_segments(self):
        self.cable_segments = {}

    # Gets a list from the segment list of the coordinates of the cable routes for the plot
    def get_route_list(self):

        # Adds the first coordinate from the segment for every segment in the list
        cable_plot_list = [self.cable_segments[i][0] for i in range(len(self.cable_segments))]

        # Adds last segment (the battery location)
        cable_plot_list.append(self.cable_segments[-1][-1])
        return cable_plot_list

    # Gets a list of the coordinates of the cable routes for the json output
    def get_route_list_string(self):
        new_list = []

        for segment in self.cable_segments:
            new_list.append(",".join(map(str, segment[0])))

        new_list.append(",".join(map(str, self.cable_segments[-1][-1])))
        return new_list
