from mesper.components.rectangle import Rectangle


class TestRectangle:

    def test_constructor(self):
        rectangle = Rectangle(15, 23, 456, 879)
        assert rectangle.top_left_x == 15
        assert rectangle.top_left_y == 23
        assert rectangle.width == 456
        assert rectangle.height == 879

    def test_move(self):
        rectangle = Rectangle(15, 23, 456, 879)
        rectangle.move(7, 13)
        assert rectangle.top_left_x == 22
        assert rectangle.top_left_y == 36
        assert rectangle.width == 456
        assert rectangle.height == 879

    def test_position(self):
        rectangle = Rectangle(15, 23, 456, 879)
        rectangle.set_position(7, 13)
        assert rectangle.top_left_x == 7
        assert rectangle.top_left_y == 13
        assert rectangle.width == 456
        assert rectangle.height == 879
