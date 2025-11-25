
class Board:
	def __init__(self, width: int = 800, height: int = 600, cell_size: int = 20, sidebar_width: int = 200):
		self.width = width
		self.height = height
		self.cell_size = cell_size
		self.sidebar_width = sidebar_width
		self.play_width = width - sidebar_width

	def draw_grid(self, screen):
		import pygame
		grid_color = (40, 40, 40)
		for x in range(0, self.play_width, self.cell_size):
			pygame.draw.line(screen, grid_color, (x, 0), (x, self.height))
		for y in range(0, self.height, self.cell_size):
			pygame.draw.line(screen, grid_color, (0, y), (self.width, y))

	def draw_sidebar(self, screen, score: int, best_score: int):
		import pygame
		sidebar_rect = pygame.Rect(self.play_width, 0, self.sidebar_width, self.height)
		pygame.draw.rect(screen, (20, 20, 20), sidebar_rect)
		pygame.draw.line(screen, (80, 80, 80), (self.play_width, 0), (self.play_width, self.height))
		font = pygame.font.SysFont(None, 28)
		score_surf = font.render(f"Score: {score}", True, (200, 200, 200))
		best_surf = font.render(f"Best: {best_score}", True, (200, 200, 200))
		screen.blit(score_surf, (self.play_width + 16, 20))
		screen.blit(best_surf, (self.play_width + 16, 52))
