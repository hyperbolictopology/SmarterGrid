class Battery():
    '''
    This class defines battery properties.
    '''
    def __init__(self, pos_x, pos_y, max_capacity):
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.location = f'{pos_x}, {pos_y}'
        self.max_capacity = float(max_capacity)
        self.current_capacity = 0.0
        self.colour = 'r'
        # low priority TODO: instead of markers, find a way to use pictures in the plot
        self.price = 5000
