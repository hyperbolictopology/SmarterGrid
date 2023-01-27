from code.classes import cable

class House():
    '''
    This class defines the house properties
    '''
    def __init__(self, pos_x, pos_y, output):
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.location = f'{pos_x}, {pos_y}'
        self.output = float(output)
        self.colour = 'k'
        # low priority TODO: instead of markers, find a way to use pictures in the plot
        self.cables = cable.Cable()
