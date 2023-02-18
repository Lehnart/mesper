import time

from ...components.rectangle import Rectangle
from ...components.speed import Speed
from ...events.move_rectangle import MoveRectangle
from ...mesper import World
from ...processors.rectangle_mover import RectangleMover


class TestRectangleMover:

    def test_process(self):
        world = World()

        rectangle_component = Rectangle(13, 27, 50, 100)
        entity = world.create_entity(rectangle_component)

        world.add_processor(RectangleMover())

        world.publish(MoveRectangle(entity, -3, 7))
        world.process()

        rectangle_component = world.component_for_entity(entity, Rectangle)
        assert rectangle_component.top_left_x == 10
        assert rectangle_component.top_left_y == 34
        assert rectangle_component.width == 50
        assert rectangle_component.height == 100

    def test_rect_and_speed(self):
        world = World()

        rectangle_component = Rectangle(13, 27, 50, 100)
        speed_component = Speed(vel_x=10., vel_y=-25.)
        entity = world.create_entity(rectangle_component, speed_component)

        world.add_processor(RectangleMover())

        world.process()
        time.sleep(0.010)
        world.process()

        rectangle_component = world.component_for_entity(entity, Rectangle)
        assert rectangle_component.top_left_x > 13
        assert rectangle_component.top_left_y < 27
