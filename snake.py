import pygame

class Snake:
    def __init__(self, x, y, body_segment_size):
        self.body = [(x, y), (x - body_segment_size, y), (x - 2 * body_segment_size, y)]
        self.segment_size = body_segment_size
        self.direction = (0, 0)
    
    def move(self, direction):
        head_x, head_y = self.body[0]
        direction_x, direction_y = direction
        new_head_x = head_x + direction_x
        new_head_y = head_y + direction_y
        segment_size = self.segment_size
        new_head = (
            (new_head_x // segment_size) * segment_size,
            (new_head_y // segment_size) * segment_size,
        )
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (x, y, self.segment_size, self.segment_size))

    def check_border_collision(self, screen_width, screen_height):
        head_x, head_y = self.body[0]
        return (
            head_x < 0 or head_y < 0 or
            head_x + self.segment_size > screen_width or
            head_y + self.segment_size > screen_height
        )

    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def get_head_position(self):
        return self.body[0]

    def get_head_rect(self):
        x, y = self.body[0]
        return pygame.Rect(x, y, self.segment_size, self.segment_size)
    
