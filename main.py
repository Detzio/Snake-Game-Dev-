import pygame
from snake import Snake

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game by Dusséaux Thomas")
running = True
clock = pygame.time.Clock()

snake = Snake(400, 300, 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    snake.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()