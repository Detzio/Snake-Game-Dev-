import pygame
from snake import Snake

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game by Dusséaux Thomas")
running = True
clock = pygame.time.Clock()

snake = Snake(400, 300, 30)

while running:

# Événements

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Logique

    keys = pygame.key.get_pressed()

    step = snake.segment_size
    if keys[pygame.K_UP] and snake.direction != (0, step):
        snake.direction = (0, -step)
    if keys[pygame.K_DOWN] and snake.direction != (0, -step):
        snake.direction = (0, step)
    if keys[pygame.K_LEFT] and snake.direction != (step, 0):
        snake.direction = (-step, 0)
    if keys[pygame.K_RIGHT] and snake.direction != (-step, 0):
        snake.direction = (step, 0)

    snake.move(snake.direction)

# Affichage

    screen.fill((0,0,0))
    snake.draw(screen)

    pygame.display.flip()
    clock.tick(10)


pygame.quit()