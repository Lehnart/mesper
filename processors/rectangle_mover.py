from ..components.rectangle import Rectangle
from ..events.move_rectangle import MoveRectangle
from ..mesper import Processor


class RectangleMover(Processor):

    def process(self):
        move_events = self.world.receive(MoveRectangle)

        for move_event in move_events:
            rectangle_component = self.world.component_for_entity(move_event.entity, Rectangle)
            rectangle_component.move(move_event.move_x, move_event.move_y)
