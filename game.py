import pygame
import random
import sys

# Define color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Define character colors (from image_0.png)
PANDA_WHITE = (235, 235, 235)  # Off-white
PANDA_BLACK = (10, 10, 10)  # Near-black
GLASSES_BLUE = (0, 0, 255)  # Electric Blue

# Game dimensions
dis_width = 800
dis_height = 600

# Initialize pygame
pygame.init()

# Setup display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Miraj: The Berry Hunter')

# Clock for controlling game speed
clock = pygame.time.Clock()

# Block sizes
block_size = 20
miraj_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def our_snake(miraj_block, snake_list):
    """Draws the growing Miraj character."""
    # Head block (always the last element in snake_list)
    head_x = snake_list[-1][0]
    head_y = snake_list[-1][1]
    
    # Draw simple character - A slightly bigger head (like a cool bear)
    # White head section
    pygame.draw.rect(dis, PANDA_WHITE, [head_x, head_y, block_size, block_size])
    # Blue 'cool glasses' section
    pygame.draw.rect(dis, GLASSES_BLUE, [head_x + 3, head_y + 3, block_size - 6, block_size // 2 - 3])
    # Black body/mask element
    pygame.draw.rect(dis, PANDA_BLACK, [head_x + block_size // 4, head_y + block_size // 2, block_size // 2, block_size // 2])

    # Draw body segments (a simple block for growth)
    for index, x in enumerate(snake_list[:-1]): # Exclude the new head we just handled
        # Use simple blocks for the body to match the retro aesthetic
        color = PANDA_BLACK if index % 2 == 0 else PANDA_WHITE
        pygame.draw.rect(dis, color, [x[0], x[1], block_size, block_size])


def message(msg, color):
    """Displays a message on the screen."""
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(dis_width/2, dis_height/2))
    dis.blit(mesg, text_rect)


def your_score(score):
    """Displays the player's current score."""
    value = score_font.render("Cherries: " + str(score), True, WHITE)
    dis.blit(value, [0, 0])


def draw_cherries(x, y):
    """Draws the special cherry based on the emoji and image_0.png."""
    cherry_size = block_size - 4
    cherry_x = x + 2
    cherry_y = y + 2
    
    # Small double-cherry clusters,