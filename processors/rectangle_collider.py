import pygame

from mesper.components.collision import Collision
from mesper.components.rectangle import Rectangle
from mesper.events.rectangle_collision import RectangleCollision
from mesper.mesper import Processor


class RectangleCollider(Processor):

    def process(self):

        collision_rectangles = self.world.get_components(Collision, Rectangle)
        rectangles = [rectangle for _, [_, rectangle] in collision_rectangles]
        pygame_rectangles = [self.to_pygame_rect(rectangle) for rectangle in rectangles]
        for current_index, pygame_rectangle in enumerate(pygame_rectangles):
            entity1 = collision_rectangles[current_index][0]
            collisions = pygame_rectangle.collidelistall(pygame_rectangles[current_index + 1:])
            for i in collisions:
                entity2 = collision_rectangles[current_index + 1 + i][0]
                self.world.publish(
                    RectangleCollision(
                        entity1,
                        pygame_rectangle,
                        entity2,
                        pygame_rectangles[current_index + 1 + i]
                    )
                )

    @staticmethod
    def to_pygame_rect(rectangle: Rectangle) -> pygame.Rect:
        return pygame.Rect(rectangle.top_left_x, rectangle.top_left_y, rectangle.width, rectangle.height)
