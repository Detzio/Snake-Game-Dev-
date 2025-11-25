import pygame
from snake import Snake
from food import Food
from game import Board

pygame.init()
board = Board(1000, 600, 20, sidebar_width=200)
screen = pygame.display.set_mode((board.width, board.height))
pygame.display.set_caption("Snake Game by Dusséaux Thomas")
clock = pygame.time.Clock()

# Load best score once for the session
best_score = 0
try:
    with open("best_score.txt", "r", encoding="utf-8") as f:
        best_score = int((f.read() or "0").strip())
except Exception:
    best_score = 0

quit_game = False
while True:
    snake = Snake(board.play_width // 2, board.height // 2, board.cell_size)
    food = Food(board.cell_size * 10, board.cell_size * 5, board.cell_size)
    score = len(snake.body)
    running = True

    # Gameplay loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
                running = False
        keys = pygame.key.get_pressed()
        cell_size = snake.segment_size
        if keys[pygame.K_UP] and snake.direction != (0, cell_size):
            if not snake.will_bite_itself((0, -cell_size)):
                snake.direction = (0, -cell_size)
        if keys[pygame.K_DOWN] and snake.direction != (0, -cell_size):
            if not snake.will_bite_itself((0, cell_size)):
                snake.direction = (0, cell_size)
        if keys[pygame.K_LEFT] and snake.direction != (cell_size, 0):
            if not snake.will_bite_itself((-cell_size, 0)):
                snake.direction = (-cell_size, 0)
        if keys[pygame.K_RIGHT] and snake.direction != (-cell_size, 0):
            if not snake.will_bite_itself((cell_size, 0)):
                snake.direction = (cell_size, 0)

        if snake.direction != (0, 0):
            snake.move(snake.direction)

        if snake.direction != (0, 0) and (snake.check_border_collision(board.play_width, board.height) or snake.check_self_collision()):
            best_score = max(best_score, score)
            try:
                with open("best_score.txt", "w", encoding="utf-8") as f:
                    f.write(str(best_score))
            except Exception:
                pass
            running = False

        if snake.get_head_rect().colliderect(food.get_rect()):
            snake.grow()
            score = len(snake.body)
            food.respawn(board.play_width, board.height, board.cell_size, occupied=snake.body)

        # Render
        screen.fill((0, 0, 0))
        board.draw_grid(screen)
        snake.draw(screen)
        food.draw(screen)
        board.draw_sidebar(screen, score=score, best_score=best_score)
        pygame.display.flip()
        clock.tick(10)

    if quit_game:
        break

    # Game over screen; wait for R to restart
    font = pygame.font.SysFont(None, 36)
    msg = font.render("Game Over - Press R to Restart", True, (220, 220, 220))
    screen.blit(msg, (board.play_width // 2 - msg.get_width() // 2, board.height // 2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                quit_game = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                waiting = False
        clock.tick(30)

    if quit_game:
        break

pygame.quit()