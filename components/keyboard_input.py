from typing import Dict, Callable, List

from ..mesper import Component, World


class KeyboardInput(Component):

    def __init__(self, input_callbacks: Dict[int, Callable[[int, World], None]], is_repeated: bool = False):
        self.input_callbacks = input_callbacks
        self.is_repeated = is_repeated

    def is_listening(self, key: int):
        return key in self.input_callbacks

    def keys(self) -> List[int]:
        return list(self.input_callbacks)

    def call(self, key: int, ent: int, world: World):
        self.input_callbacks[key](ent, world)
