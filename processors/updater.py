import sys

import pygame

from ..components.keyboard_input import KeyboardInput
from ..mesper import Processor


class Updater(Processor):

    def process(self):

        keyboard_input_entity_and_components = self.world.get_component(KeyboardInput)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                for ent, keyboard_input_component in keyboard_input_entity_and_components:
                    if keyboard_input_component.is_listening(event.key):
                        keyboard_input_component.call(event.key, ent, self.world)
