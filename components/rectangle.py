from mesper.mesper import Component


class Rectangle(Component):

    def __init__(self, top_left_x: float, top_left_y: float, width: float, height: float):
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height

    def move(self, move_x: float, move_y: float):
        self.top_left_x += move_x
        self.top_left_y += move_y

    def set_position(self, top_left_x: float, top_left_y: float):
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
