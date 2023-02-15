import enum

from mesper.mesper import Event


class OutOfLimitType(enum.Enum):
    X_LOW = 0
    X_HIGH = 1
    Y_LOW = 2
    Y_HIGH = 3


class OutOfLimit(Event):

    def __init__(self, entity: int, position: float, limit: float, out_of_limit: OutOfLimitType):
        self.entity = entity
        self.position = position
        self.limit = limit
        self.out_of_limit = out_of_limit
