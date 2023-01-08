import pygame

from ...components.sprite import Sprite
from ...events.move_sprite import MoveSprite
from ...mesper import World
from ...processors.sprite_mover import SpriteMover


class TestSpriteMover:

    def test_process(self):
        world = World()

        surf = pygame.Surface((5, 5))
        ent = world.create_entity(Sprite(surf, (10, 10)))

        world.add_processor(SpriteMover())

        world.publish(MoveSprite(ent, (-3, 7)))
        world.process()

        sprite_comp = world.component_for_entity(ent, Sprite)
        assert sprite_comp.top_left_position == (7, 17)
