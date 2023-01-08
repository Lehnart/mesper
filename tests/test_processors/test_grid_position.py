from components.grid_position import GridPosition
from events.move_on_grid import MoveOnGrid
from mesper import World
from processors.grid_mover import GridMover


class TestGridPosition:

    def test_process(self):
        world = World()

        ent = world.create_entity(GridPosition(10, 10))

        world.add_processor(GridMover())

        world.publish(MoveOnGrid(ent, (-3, 7)))
        world.process()

        comp = world.component_for_entity(ent, GridPosition)
        assert comp.pos == (7, 17)
