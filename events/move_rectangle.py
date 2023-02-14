from mesper.mesper import Event


class MoveRectangle(Event):

    def __init__(self, entity: int, move_x: float, move_y: float):
        super().__init__()
        self.entity = entity
        self.move_x = move_x
        self.move_y = move_y
