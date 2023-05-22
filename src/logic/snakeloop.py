# import random
import pygame
from src.logic.point.point import Point


def main_loop(screen, seed, bot_mode):
    pygame.init()

    # Clear menu display
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # Colors
    green = (65, 255, 0)

    # Game Variables
    is_game_over = False
    is_paused = False
    snake_head_position = Point(300, 300)
    snake_head_direction = Point(0, 0)

    clock = pygame.time.Clock()

    while is_game_over is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_head_direction = Point(-10, 0)
                elif event.key == pygame.K_RIGHT:
                    snake_head_direction = Point(10, 0)
                elif event.key == pygame.K_UP:
                    snake_head_direction = Point(0, -10)
                elif event.key == pygame.K_DOWN:
                    snake_head_direction = Point(0, 10)
                elif event.key == pygame.K_SPACE:
                    is_paused = not is_paused
        if is_paused is True:
            continue

        # Draw Snake
        snake_head_position += snake_head_direction
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, green, [snake_head_position.get_x(), snake_head_position.get_y(), 10, 10])
        pygame.display.update()
        clock.tick(24)
