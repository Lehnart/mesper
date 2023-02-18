from mesper.mesper import Component


class Speed(Component):

    def __init__(self, vel_x : float, vel_y : float):
        self.vel_x = vel_x
        self.vel_y = vel_y
