# import random
import pygame
from src.logic.point.point import Point


def get_keyboard_movement(events):
    pygame.init()
    next_movement_direction = []
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                next_movement_direction.append(Point(-10, 0))
            elif event.key == pygame.K_RIGHT:
                next_movement_direction.append(Point(10, 0))
            elif event.key == pygame.K_UP:
                next_movement_direction.append(Point(0, -10))
            elif event.key == pygame.K_DOWN:
                next_movement_direction.append(Point(0, 10))
    # print(next_movement_direction)
    return next_movement_direction


def main_loop(screen, seed, bot_mode):
    pygame.init()
    clock = pygame.time.Clock()
    screen_width, screen_height = screen.get_size()

    # Clear menu display
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # Colors
    green = (65, 255, 0)
    red = (144, 242, 21)

    # Game State Variables
    is_game_over = False
    is_paused = False

    # Snake Position and Direction
    snake_head_position = Point(300, 300)
    snake_head_direction = Point(0, 0)
    movement_queue = []

    while is_game_over is False:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                is_game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_paused = not is_paused

        # Get next movement
        if bot_mode is True:
            if len(movement_queue) <= 0:
                pass
            # TODO: bot movement
        else:
            movement_queue = get_keyboard_movement(events)

        # Paused Game Check
        if is_paused is True:
            continue

        # Snake out of Screen Check
        if not (0 <= snake_head_position.get_x() < screen_width) or not (
                0 <= snake_head_position.get_y() < screen_height):
            is_game_over = True

        # Move Snake
        if len(movement_queue) > 0:
            snake_head_direction = movement_queue.pop(0)
        snake_head_position += snake_head_direction

        # Draw Snake
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, green, [snake_head_position.get_x(), snake_head_position.get_y(), 10, 10])
        pygame.display.update()
        clock.tick(24)
