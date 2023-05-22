import pygame
import time
import random
from src.logic.point.point import Point
from src.logic.snakebot.snakebot import SnakeBot

pixel_size = 25


def get_keyboard_movement(events):
    pygame.init()
    next_movement_direction = []
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                next_movement_direction.append(Point(-pixel_size, 0))
            elif event.key == pygame.K_RIGHT:
                next_movement_direction.append(Point(pixel_size, 0))
            elif event.key == pygame.K_UP:
                next_movement_direction.append(Point(0, -pixel_size))
            elif event.key == pygame.K_DOWN:
                next_movement_direction.append(Point(0, pixel_size))
    # print(next_movement_direction)
    return next_movement_direction


def game_over_screen(screen):
    game_over_font = pygame.font.Font(None, 40)
    white = (255, 255, 255)
    width, height = screen.get_size()
    game_over_prompt = game_over_font.render("GAME OVER", True, white)
    screen.blit(game_over_prompt, [width // 2 - 80, height // 2])


def show_food_score(screen, score):
    score_font = pygame.font.Font(None, 35)
    white = (255, 255, 255)
    score_value = score_font.render("SCORE: " + str(score), True, white)
    screen.blit(score_value, [0, 0])


def main_loop(screen, seed, bot_mode, snake_speed=30):
    # Setup pygame and seed
    pygame.init()
    clock = pygame.time.Clock()
    screen_width, screen_height = screen.get_size()
    if seed == "":
        random.seed(int(time.time()))
    else:
        random.seed(seed)

    # Clear menu display
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # Colors
    green = (65, 255, 0)
    red = (238, 75, 43)
    white = (255, 255, 255)

    # Game State Variables
    is_game_over = False
    is_paused = False

    # Snake Position and Direction
    snake_head_position = Point(300, 300)
    snake_head_direction = Point(0, 0)
    movement_queue = []

    # Snake Body
    snake_body = [snake_head_position]
    snake_length = 1

    # Food and Food Score
    food_position = Point(random.randint(0, screen_width - pixel_size) // pixel_size * pixel_size,
                          random.randint(0, screen_height - pixel_size) // pixel_size * pixel_size)
    while food_position in snake_body:
        food_position = Point(random.randint(0, screen_width - pixel_size) // pixel_size * pixel_size,
                              random.randint(0, screen_height - pixel_size) // pixel_size * pixel_size)

    print("Head", snake_head_position.to_string())
    while is_game_over is False:
        print("Food", food_position.to_string())
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
                print("Head", snake_head_position.to_string())
                bot_service = SnakeBot(screen, snake_body, pixel_size, show_debug=False)
                bot_service.plan_route(snake_head_position, food_position)
                movement_queue = bot_service.get_movement_list()
        else:
            movement_queue = get_keyboard_movement(events)

        # Paused Game Check
        if is_paused is True:
            continue

        # Snake out of Screen Check
        if not (0 <= snake_head_position.get_x() < screen_width) or not (
                0 <= snake_head_position.get_y() < screen_height):
            is_game_over = True
        # Snake head-body collision check
        for i in range(0, len(snake_body) - 1):
            if snake_body[i] == snake_head_position:
                is_game_over = True

        # Move Snake using Movement Queued in List
        if len(movement_queue) > 0:
            next_direction = movement_queue.pop(0)

            # Check and prevent reverse direction
            if snake_head_direction + next_direction != Point(0, 0):
                snake_head_direction = next_direction
        snake_head_position += snake_head_direction

        # Update Snake Segments
        snake_body.append(snake_head_position)
        if len(snake_body) > snake_length:
            snake_body.pop(0)

        # Draw Snake and Food
        screen.fill((0, 0, 0))
        for snake_segment in snake_body:
            pygame.draw.rect(screen, green, [snake_segment.get_x(), snake_segment.get_y(), pixel_size, pixel_size])
        pygame.draw.rect(screen, red, [food_position.get_x(), food_position.get_y(), pixel_size, pixel_size])

        # Update score
        show_food_score(screen, snake_length - 1)
        if snake_head_position == food_position:
            print("chew")
            print("Head", snake_head_position.to_string())

            while food_position in snake_body:
                food_position = Point(random.randint(0, screen_width - pixel_size) // pixel_size * pixel_size,
                                      random.randint(0, screen_height - pixel_size) // pixel_size * pixel_size)
            snake_length += 1

        pygame.display.update()
        clock.tick(snake_speed)

    game_over_screen(screen)
    print("Game Over")
    pygame.draw.rect(screen, white, [snake_head_position.get_x(), snake_head_position.get_y(), pixel_size, pixel_size])
    pygame.display.update()
    pygame.time.wait(4000)
