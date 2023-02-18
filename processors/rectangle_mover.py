from ..components.rectangle import Rectangle
from ..components.speed import Speed
from ..events.move_rectangle import MoveRectangle
from ..mesper import Processor


class RectangleMover(Processor):

    def process(self):
        move_events = self.world.receive(MoveRectangle)

        for move_event in move_events:
            rectangle_component = self.world.component_for_entity(move_event.entity, Rectangle)
            rectangle_component.move(move_event.move_x, move_event.move_y)

        for _, [speed_component, rectangle_component] in self.world.get_components(Speed, Rectangle):
            rectangle_component.move(
                speed_component.vel_x*self.world.process_dt,
                speed_component.vel_y*self.world.process_dt
            )
