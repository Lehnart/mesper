from ...components.collision import Collision
from ...components.rectangle import Rectangle
from ...events.rectangle_collision import RectangleCollision
from ...mesper import World
from ...processors.rectangle_collider import RectangleCollider



class TestRectangleCollider:

    def test_process(self):
        world = World()

        rectangle_component = Rectangle(0, 0, 50, 100)
        entity1 = world.create_entity(rectangle_component, Collision())

        rectangle_component = Rectangle(30, 75, 50, 100)
        entity2 = world.create_entity(rectangle_component, Collision())

        rectangle_component = Rectangle(60, 150, 50, 100)
        entity3 = world.create_entity(rectangle_component, Collision())

        world.add_processor(RectangleCollider())
        world.process()

        collisions = world.receive(RectangleCollision)
        assert len(collisions) == 2
        for collision in collisions:
            assert (collision.ent1, collision.ent2) in [(entity1, entity2), (entity2, entity3)]
