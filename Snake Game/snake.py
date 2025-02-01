import pygame
import random

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# Load sound effects
eat_sound = pygame.mixer.Sound("eat.mp3")  # Play when eating fruit
game_over_sound = pygame.mixer.Sound("game_over.mp3")  # Play on collision

# Set screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Player 1 Snake
BLUE = (0, 0, 255)   # Player 2 Snake
RED = (255, 0, 0)    # Fruit
BLACK = (0, 0, 0)    # Background
GRAY = (100, 100, 100)

# Fonts
title_font = pygame.font.Font(None, 50)
menu_font = pygame.font.Font(None, 35)
score_font = pygame.font.Font(None, 25)

# Game Clock
clock = pygame.time.Clock()

# Fruit position
fruit_x = random.randrange(0, WIDTH - 10, 10)
fruit_y = random.randrange(0, HEIGHT - 10, 10)


def draw_text(text, font, color, x, y, center=True):
    """ Helper function to draw centered text """
    render = font.render(text, True, color)
    text_rect = render.get_rect(center=(x, y)) if center else (x, y)
    screen.blit(render, text_rect)


def show_menu():
    """ Displays the start menu with options """
    screen.fill(BLACK)

    draw_text("SNAKE GAME", title_font, GREEN, WIDTH // 2, HEIGHT // 4)
    draw_text("Press 1:  Single Player", menu_font, WHITE, WIDTH // 2, HEIGHT // 2 - 30)
    draw_text("Press 2: Multiplayer", menu_font, WHITE, WIDTH // 2, HEIGHT // 2 + 10)
    draw_text("Press 1 or 2 to Select", score_font, GRAY, WIDTH // 2, HEIGHT - 50)

    pygame.display.flip()


def game_over_screen(winner):
    """ Displays the Game Over screen """
    pygame.mixer.Sound.play(game_over_sound)
    screen.fill(BLACK)

    draw_text(f"Game Over!", title_font, RED, WIDTH // 2, HEIGHT // 3)
    draw_text(f"{winner} Lost", menu_font, WHITE, WIDTH // 2, HEIGHT // 2)
    draw_text("Press any key to return to menu", score_font, GRAY, WIDTH // 2, HEIGHT - 50)

    pygame.display.flip()
    wait_for_key()


def wait_for_key():
    """ Waits for player input to return to the menu """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                return


def select_mode():
    """ Handles mode selection """
    show_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "single"
                elif event.key == pygame.K_2:
                    return "multi"


def single_player():
    """ Single Player Mode """
    snake = [[300, 200]]
    direction = "RIGHT"
    score = 0

    global fruit_x, fruit_y

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # Move the snake
        if direction == "UP":
            snake.insert(0, [snake[0][0], snake[0][1] - 10])
        elif direction == "DOWN":
            snake.insert(0, [snake[0][0], snake[0][1] + 10])
        elif direction == "LEFT":
            snake.insert(0, [snake[0][0] - 10, snake[0][1]])
        elif direction == "RIGHT":
            snake.insert(0, [snake[0][0] + 10, snake[0][1]])

        # Collision detection
        if snake[0] in snake[1:] or snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT:
            game_over_screen("Player")
            return

        # Eating fruit
        if snake[0][0] == fruit_x and snake[0][1] == fruit_y:
            pygame.mixer.Sound.play(eat_sound)
            score += 1
            fruit_x = random.randrange(0, WIDTH - 10, 10)
            fruit_y = random.randrange(0, HEIGHT - 10, 10)
        else:
            snake.pop()

        # Draw elements
        pygame.draw.rect(screen, RED, pygame.Rect(fruit_x, fruit_y, 10, 10))
        for pos in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

        draw_text(f"Score: {score}", score_font, WHITE, 50, 20, center=False)
        pygame.display.flip()
        clock.tick(10)


def multiplayer():
    """ Multiplayer Mode """
    snake1, snake2 = [[100, 200]], [[500, 200]]
    direction1, direction2 = "RIGHT", "LEFT"
    score1, score2 = 0, 0

    global fruit_x, fruit_y

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                # Player 1 controls
                if event.key == pygame.K_UP and direction1 != "DOWN":
                    direction1 = "UP"
                elif event.key == pygame.K_DOWN and direction1 != "UP":
                    direction1 = "DOWN"
                elif event.key == pygame.K_LEFT and direction1 != "RIGHT":
                    direction1 = "LEFT"
                elif event.key == pygame.K_RIGHT and direction1 != "LEFT":
                    direction1 = "RIGHT"

                # Player 2 controls
                if event.key == pygame.K_w and direction2 != "DOWN":
                    direction2 = "UP"
                elif event.key == pygame.K_s and direction2 != "UP":
                    direction2 = "DOWN"
                elif event.key == pygame.K_a and direction2 != "RIGHT":
                    direction2 = "LEFT"
                elif event.key == pygame.K_d and direction2 != "LEFT":
                    direction2 = "RIGHT"

        # Move snakes
        def move_snake(snake, direction):
            if direction == "UP":
                snake.insert(0, [snake[0][0], snake[0][1] - 10])
            elif direction == "DOWN":
                snake.insert(0, [snake[0][0], snake[0][1] + 10])
            elif direction == "LEFT":
                snake.insert(0, [snake[0][0] - 10, snake[0][1]])
            elif direction == "RIGHT":
                snake.insert(0, [snake[0][0] + 10, snake[0][1]])

        move_snake(snake1, direction1)
        move_snake(snake2, direction2)

        # Collision detection
        def check_collision(snake):
            return (
                snake[0] in snake[1:] or  # Self-collision
                snake[0][0] < 0 or snake[0][0] >= WIDTH or  # Wall collision
                snake[0][1] < 0 or snake[0][1] >= HEIGHT
            )

        if check_collision(snake1):
            game_over_screen("Player 1")
            return
        if check_collision(snake2):
            game_over_screen("Player 2")
            return

        # Eating fruit
        if snake1[0] == [fruit_x, fruit_y]:
            pygame.mixer.Sound.play(eat_sound)
            score1 += 1
            fruit_x, fruit_y = random.randrange(0, WIDTH - 10, 10), random.randrange(0, HEIGHT - 10, 10)
        else:
            snake1.pop()

        if snake2[0] == [fruit_x, fruit_y]:
            pygame.mixer.Sound.play(eat_sound)
            score2 += 1
            fruit_x, fruit_y = random.randrange(0, WIDTH - 10, 10), random.randrange(0, HEIGHT - 10, 10)
        else:
            snake2.pop()

        # Draw elements
        pygame.draw.rect(screen, RED, pygame.Rect(fruit_x, fruit_y, 10, 10))
        for pos in snake1:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
        for pos in snake2:
            pygame.draw.rect(screen, BLUE, pygame.Rect(pos[0], pos[1], 10, 10))

        draw_text(f"P1 Score: {score1}", score_font, WHITE, 100, 20, center=False)
        draw_text(f"P2 Score: {score2}", score_font, WHITE, 400, 20, center=False)

        pygame.display.flip()
        clock.tick(10)



# Start game loop
while True:
    mode = select_mode()
    if mode == "single":
        single_player()
    else:
        multiplayer()
