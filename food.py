import pygame
import random


class Food:
    def __init__(self, x, y, size):
        self.position = (x, y)
        self.size = size

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0], self.position[1], self.size, self.size))

    def get_rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.size, self.size)

    def respawn(self, screen_width, screen_height, cell_size, occupied=None):
        column_count = screen_width // cell_size
        row_count = screen_height // cell_size
        choices = [
            (column_index * cell_size, row_index * cell_size)
            for column_index in range(column_count)
            for row_index in range(row_count)
        ]
        if occupied:
            occupied_positions = set(occupied)
            choices = [position for position in choices if position not in occupied_positions]
        if choices:
            self.position = random.choice(choices)