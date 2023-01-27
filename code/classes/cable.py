class Cable():
    '''
    This class defines cables properties.
    '''
    def __init__(self):
        self.cable_segments = [] # Example: [ ((1,1), (1,2)), ((1,2), (1,3)) ]
        self.price = 9
        # TODO net zoals bij huis en batterij hier ook een kleur toe te wijzen.
        # Tip van wouter was om batterijen verschillende kleuren te geven en de
        # kabels daarbij te matchen voor beter overzicht (begreep ik dat goed?)

    # A segment consists out of two adjacent points in the grid (start and end)
    def add_cable_segment(self, start, end):
        self.cable_segments.append((start, end))

    # Start clean
    def clear_segments(self):
        self.cable_segments = []

    # Get a list from the segment list of the coordinates of the cable routes for the plot
    def get_route_list(self):

        # Adding the first coordinate from the segment for every segment in the list
        cable_plot_list = [self.cable_segments[i][0] for i in range(len(self.cable_segments))]

        # Add last segment (the battery location)
        cable_plot_list.append(self.cable_segments[-1][-1])
        return cable_plot_list

    # Get a list of the coordinates of the cable routes for the json output
    def get_route_list_string(self):
        new_list = []

        for segment in self.cable_segments:
            new_list.append(",".join(map(str, segment[0])))

        new_list.append(",".join(map(str, self.cable_segments[-1][-1])))
        return new_list
