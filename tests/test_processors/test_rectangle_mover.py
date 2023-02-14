from ...components.rectangle import Rectangle
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
