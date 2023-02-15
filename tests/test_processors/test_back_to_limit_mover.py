from ...components.limit_position import LimitPosition
from ...components.rectangle import Rectangle
from ...mesper import World
from ...processors.back_to_limit_mover import BackToLimitMover
from ...processors.limit_position_checker import LimitPositionChecker
from ...processors.rectangle_mover import RectangleMover


class TestOutOfCollisionMover:

    def test_process(self):
        world = World()

        rectangle_component = Rectangle(20, 40, 50, 100)
        limit_position = LimitPosition(25, 500, 0, 500)
        entity1 = world.create_entity(rectangle_component, limit_position)

        rectangle_component = Rectangle(25, -15, 50, 100)
        limit_position = LimitPosition(25, 500, 0, 500)
        entity2 = world.create_entity(rectangle_component, limit_position)

        rectangle_component = Rectangle(50, 0, 100, 100)
        limit_position = LimitPosition(0, 100, 0, 100)
        entity3 = world.create_entity(rectangle_component, limit_position)

        rectangle_component = Rectangle(0, 50, 100, 100)
        limit_position = LimitPosition(0, 100, 0, 100)
        entity4 = world.create_entity(rectangle_component, limit_position)

        world.add_processor(LimitPositionChecker())
        world.add_processor(BackToLimitMover())
        world.add_processor(RectangleMover())
        world.process()

        rectangle1 = world.component_for_entity(entity1, Rectangle)
        assert rectangle1.top_left_x == 25

        rectangle2 = world.component_for_entity(entity2, Rectangle)
        assert rectangle2.top_left_y == 0

        rectangle3 = world.component_for_entity(entity3, Rectangle)
        assert rectangle3.top_left_x == 0

        rectangle4 = world.component_for_entity(entity4, Rectangle)
        assert rectangle4.top_left_y == 0
