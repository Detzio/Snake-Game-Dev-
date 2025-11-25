
class Board:
	def __init__(self, width: int = 800, height: int = 600, cell_size: int = 20):
		self.width = width
		self.height = height
		self.cell_size = cell_size

	def draw_grid(self, screen):
		import pygame
		grid_color = (40, 40, 40)
		for x in range(0, self.width, self.cell_size):
			pygame.draw.line(screen, grid_color, (x, 0), (x, self.height))
		for y in range(0, self.height, self.cell_size):
			pygame.draw.line(screen, grid_color, (0, y), (self.width, y))
