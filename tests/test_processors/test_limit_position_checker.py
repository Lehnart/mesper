from ...components.limit_position import LimitPosition
from ...components.rectangle import Rectangle
from ...events.out_of_limit import OutOfLimit, OutOfLimitType
from ...mesper import World
from ...processors.limit_position_checker import LimitPositionChecker


class TestLimitPositionChecker:

    def test_process(self):
        world = World()

        rectangle_component = Rectangle(20, 40, 50, 100)
        limit_position = LimitPosition(25, 60, 45, 130)
        world.create_entity(rectangle_component, limit_position)

        world.add_processor(LimitPositionChecker())

        world.process()

        out_of_limit_events = world.receive(OutOfLimit)
        assert out_of_limit_events[0].limit == 25
        assert out_of_limit_events[0].position == 20
        assert out_of_limit_events[0].out_of_limit == OutOfLimitType.X_LOW

        assert out_of_limit_events[1].limit == 45
        assert out_of_limit_events[1].position == 40
        assert out_of_limit_events[1].out_of_limit == OutOfLimitType.Y_LOW

        assert out_of_limit_events[2].limit == 60
        assert out_of_limit_events[2].position == 70
        assert out_of_limit_events[2].out_of_limit == OutOfLimitType.X_HIGH

        assert out_of_limit_events[3].limit == 130
        assert out_of_limit_events[3].position == 140
        assert out_of_limit_events[3].out_of_limit == OutOfLimitType.Y_HIGH
