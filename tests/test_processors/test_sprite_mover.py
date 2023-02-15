import pygame

from ...components.rectangle import Rectangle
from ...components.sprite import Sprite
from ...components.sprite_follow_rectangle import SpriteFollowRectangle
from ...events.move_sprite import MoveSprite
from ...mesper import World
from ...processors.rectangle_mover import RectangleMover
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

    def test_follow_rectangle(self):
        world = World()

        rectangle_component = Rectangle(13, 27, 50, 100)
        surf = pygame.Surface((5, 5))
        ent = world.create_entity(Sprite(surf, (10, 10)), rectangle_component, SpriteFollowRectangle())

        world.add_processor(RectangleMover())
        world.add_processor(SpriteMover())

        world.process()

        sprite_component = world.component_for_entity(ent, Sprite)
        assert sprite_component.top_left_position == (13, 27)
