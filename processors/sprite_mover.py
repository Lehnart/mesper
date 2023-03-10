from ..components.rectangle import Rectangle
from ..components.sprite import Sprite
from ..events.move_sprite import MoveSprite
from ..events.set_sprite_position import SetSpritePosition
from ..mesper import Processor


class SpriteMover(Processor):

    def process(self):
        move_sprite_events = self.world.receive(MoveSprite)

        for move_sprite_event in move_sprite_events:
            sprite_component = self.world.component_for_entity(move_sprite_event.ent, Sprite)
            sprite_component.move(*move_sprite_event.movement)

        set_sprite_position_events = self.world.receive(SetSpritePosition)

        for set_sprite_pos_event in set_sprite_position_events:
            sprite_component = self.world.component_for_entity(set_sprite_pos_event.ent, Sprite)
            sprite_component.top_left_position = set_sprite_pos_event.pos

        following_sprites = self.world.get_components(Rectangle, Sprite)
        for _, [rect, sprite] in following_sprites:
            sprite.top_left_position = (rect.top_left_x, rect.top_left_y)
