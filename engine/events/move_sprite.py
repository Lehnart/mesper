from typing import Tuple

from engine.mesper import Event


class MoveSprite(Event):

    def __init__(self, ent: int, movement: Tuple[int, int]):
        self.ent = ent
        self.movement = movement