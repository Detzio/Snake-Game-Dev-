import pygame

class Snake:
    def __init__(self, x, y, body_segment_size):
        self.body = [(x, y), (x - body_segment_size, y), (x - 2 * body_segment_size, y)]
        self.segment_size = body_segment_size
        self.direction = (1, 0)
    
    def move(self, direction):
        head_x, head_y = self.body[0]
        dir_x, dir_y = direction
        new_head = ( head_x + dir_x, head_y + dir_y )
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0,255,0), (segment[0], segment[1], self.segment_size, self.segment_size))

    def check_collision(self, screen_width, screen_height):
        pass

    def get_head_position(self):
        return self.body[0]
    
