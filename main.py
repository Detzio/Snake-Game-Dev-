import pygame
from snake import Snake
from food import Food
from game import Board

pygame.init()
board = Board(800, 600, 20)
screen = pygame.display.set_mode((board.width, board.height))
pygame.display.set_caption("Snake Game by Dusséaux Thomas")
running = True
clock = pygame.time.Clock()

snake = Snake(board.width // 2, board.height // 2, board.cell_size)
food = Food(board.cell_size * 10, board.cell_size * 5, board.cell_size)

while running:

# Événements

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Logique

    keys = pygame.key.get_pressed()

    cell_size = snake.segment_size
    if keys[pygame.K_UP] and snake.direction != (0, cell_size):
        snake.direction = (0, -cell_size)
    if keys[pygame.K_DOWN] and snake.direction != (0, -cell_size):
        snake.direction = (0, cell_size)
    if keys[pygame.K_LEFT] and snake.direction != (cell_size, 0):
        snake.direction = (-cell_size, 0)
    if keys[pygame.K_RIGHT] and snake.direction != (-cell_size, 0):
        snake.direction = (cell_size, 0)

    if snake.direction != (0, 0):
        snake.move(snake.direction)

    if snake.direction != (0, 0) and (snake.check_border_collision(board.width, board.height) or snake.check_self_collision()):
        print("Collision detected! Game Over.")
        running = False

    if snake.get_head_rect().colliderect(food.get_rect()):
        snake.grow()
        food.respawn(board.width, board.height, board.cell_size, occupied=snake.body)

# Affichage

    screen.fill((0,0,0))
    board.draw_grid(screen)
    snake.draw(screen)
    food.draw(screen)

    pygame.display.flip()
    clock.tick(10)


pygame.quit()