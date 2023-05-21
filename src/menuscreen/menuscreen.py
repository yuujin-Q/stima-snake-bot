import pygame
import sys


def view_menu_screen(screen):
    pygame.init()

    # Colors and fonts
    white = (255, 255, 255)
    black = (0, 0, 0)
    title_font = pygame.font.Font(None, 80)
    menu_font = pygame.font.Font(None, 40)
    field_font = pygame.font.Font(None, 32)

    # Set up text
    title_text = title_font.render("SNAKE", True, white)
    play_text = menu_font.render("Play", True, white)
    autoplay_text = menu_font.render("Autoplay", True, white)
    quit_text = menu_font.render("Quit", True, white)

    # Set up text positions
    title_text_rect = title_text.get_rect(center=(400, 100))
    play_text_rect = play_text.get_rect(center=(400, 200))
    autoplay_text_rect = autoplay_text.get_rect(center=(400, 250))
    quit_text_rect = quit_text.get_rect(center=(400, 450))

    # Seed box
    is_typing = False
    seed_input = ""

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_text_rect.collidepoint(event.pos):
                    print("Play button clicked!")
                    # TODO: game logic (1)
                elif autoplay_text_rect.collidepoint(event.pos):
                    print("Autoplay!")
                    # TODO: game logic (2)
                elif seed_text_rect.collidepoint(event.pos):
                    is_typing = True
                    print("Seed Input Active")
                elif quit_text_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN and is_typing:
                if event.key == pygame.K_RETURN:
                    print("Seed:", seed_input)
                    is_typing = False
                elif event.key == pygame.K_BACKSPACE:
                    seed_input = seed_input[:-1]
                else:
                    seed_input += event.unicode

        # Seed text input
        if seed_input == "":
            seed_placeholder = "Input Food Seed Here"
        else:
            seed_placeholder = seed_input
        seed_text = field_font.render(seed_placeholder, True, white)
        seed_text_rect = seed_text.get_rect(center=(400, 300))

        # Draw title
        screen.fill(black)
        screen.blit(title_text, title_text_rect)

        # Draw play buttons
        pygame.draw.rect(screen, white, play_text_rect, 2)
        screen.blit(play_text, play_text_rect)
        pygame.draw.rect(screen, white, autoplay_text_rect, 2)
        screen.blit(autoplay_text, autoplay_text_rect)

        # Draw seed box, quit button
        pygame.draw.rect(screen, white, seed_text_rect, 2)
        screen.blit(seed_text, seed_text_rect)
        pygame.draw.rect(screen, white, quit_text_rect, 2)
        screen.blit(quit_text, quit_text_rect)

        pygame.display.flip()

    return
