from mesper.components.limit_position import LimitPosition
from mesper.components.rectangle import Rectangle
from mesper.events.out_of_limit import OutOfLimit, OutOfLimitType
from mesper.mesper import Processor


class LimitPositionChecker(Processor):

    def process(self):
        limit_rectangles = self.world.get_components(Rectangle, LimitPosition)
        for ent, [rectangle, limit] in limit_rectangles:
            rect_x_min = rectangle.top_left_x
            rect_x_max = rectangle.top_left_x + rectangle.width
            rect_y_min = rectangle.top_left_y
            rect_y_max = rectangle.top_left_y + rectangle.height

            if rect_x_min < limit.x_min:
                self.world.publish(OutOfLimit(ent, rect_x_min, limit.x_min, OutOfLimitType.X_LOW))
            if rect_y_min < limit.y_min:
                self.world.publish(OutOfLimit(ent, rect_y_min, limit.y_min, OutOfLimitType.Y_LOW))
            if rect_x_max > limit.x_max:
                self.world.publish(OutOfLimit(ent, rect_x_max, limit.x_max, OutOfLimitType.X_HIGH))
            if rect_y_max > limit.y_max:
                self.world.publish(OutOfLimit(ent, rect_y_max, limit.y_max, OutOfLimitType.Y_HIGH))
