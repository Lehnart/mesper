import pygame

from mesper.components.keyboard_input import KeyboardInput
from mesper.mesper import World


class TestKeyboardInput:
    my_int = 0

    def set_to_12(self, ent: int, world: World):
        assert ent is not None
        assert world is not None

        TestKeyboardInput.my_int = 12

    def test_constructor(self):
        keyboard_input = KeyboardInput({pygame.K_UP: self.set_to_12})
        assert pygame.K_UP in keyboard_input.input_callbacks
        assert not keyboard_input.is_repeated

        keyboard_input = KeyboardInput({pygame.K_UP: self.set_to_12}, True)
        assert pygame.K_UP in keyboard_input.input_callbacks
        assert keyboard_input.is_repeated

    def test_is_listening(self):
        keyboard_input = KeyboardInput({pygame.K_UP: self.set_to_12})
        assert keyboard_input.is_listening(pygame.K_UP)
        assert not keyboard_input.is_listening(pygame.K_DOWN)

    def test_keys(self):
        keyboard_input = KeyboardInput({pygame.K_UP: self.set_to_12})
        assert keyboard_input.keys() == [pygame.K_UP]

    def test_call(self):
        TestKeyboardInput.my_int = 0
        assert TestKeyboardInput.my_int == 0

        keyboard_input = KeyboardInput({pygame.K_UP: self.set_to_12})
        keyboard_input.call(pygame.K_UP, 0, World())
        assert TestKeyboardInput.my_int == 12
