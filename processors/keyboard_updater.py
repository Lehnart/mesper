import sys

import pygame

from ..components.keyboard_input import KeyboardInput
from ..mesper import Processor


class KeyboardUpdater(Processor):

    def process(self):

        keyboard_input_entity_and_components = self.world.get_component(KeyboardInput)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.check_pressed_key(event, keyboard_input_entity_and_components)

        self.check_keys_hold_down(keyboard_input_entity_and_components)

    def check_pressed_key(self, event, keyboard_input_entity_and_components):
        if event.type == pygame.KEYDOWN:
            for ent, keyboard_input_component in keyboard_input_entity_and_components:
                if keyboard_input_component.is_listening(event.key) and not keyboard_input_component.is_repeated:
                    keyboard_input_component.call(event.key, ent, self.world)

    def check_keys_hold_down(self, keyboard_input_entity_and_components):
        keys = pygame.key.get_pressed()
        for ent, keyboard_input_component in keyboard_input_entity_and_components:
            for key in keyboard_input_component.keys():
                if keys[key] and keyboard_input_component.is_repeated:
                    keyboard_input_component.call(key, ent, self.world)
                    break
