import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 300  # Width and height of the window
ROWS, COLS = 3, 5         # Number of rows and columns in the game board
SQUARE_SIZE = WIDTH // COLS  # Size of each square

# Colors
WHITE = (255, 255, 255)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Impact Rift")

# Load images
blank_square = pygame.image.load('images/blank_square.png').convert()
mountain_square = pygame.image.load('images/mountain_square.png').convert()

# Scale images to fit squares
blank_square = pygame.transform.scale(blank_square, (SQUARE_SIZE, SQUARE_SIZE))
mountain_square = pygame.transform.scale(mountain_square, (SQUARE_SIZE, SQUARE_SIZE))

# List of possible images
images = [blank_square, mountain_square]

# Function to generate the initial board
def generate_board():
    return [[random.choice(images) for _ in range(COLS)] for _ in range(ROWS)]

# Generate the initial board
board = generate_board()

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            screen.blit(board[row][col], (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)  # Fill the screen with white color
    draw_board()  # Draw the game board

    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()