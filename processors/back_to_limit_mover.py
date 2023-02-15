from mesper.events.move_rectangle import MoveRectangle
from mesper.events.out_of_limit import OutOfLimit, OutOfLimitType
from mesper.mesper import Processor


class BackToLimitMover(Processor):

    def process(self):

        out_of_limit_events = self.world.receive(OutOfLimit)
        for out_of_limit_event in out_of_limit_events:
            entity = out_of_limit_event.entity
            event_type = out_of_limit_event.out_of_limit
            if event_type == OutOfLimitType.X_LOW:
                self.world.publish(MoveRectangle(entity, out_of_limit_event.limit - out_of_limit_event.position, 0))

            elif event_type == OutOfLimitType.X_HIGH:
                self.world.publish(MoveRectangle(entity, out_of_limit_event.limit - out_of_limit_event.position, 0))

            elif event_type == OutOfLimitType.Y_LOW:
                self.world.publish(MoveRectangle(entity, 0, out_of_limit_event.limit - out_of_limit_event.position))

            else:
                self.world.publish(MoveRectangle(entity, 0, out_of_limit_event.limit - out_of_limit_event.position))
