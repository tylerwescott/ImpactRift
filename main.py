import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400  # Adjust the width and height of the window
ROWS, COLS = 4, 6         # Number of rows and columns in the game board
SQUARE_SIZE = WIDTH // COLS  # Size of each square

# Colors
WHITE = (255, 255, 255)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Impact Rift")

# Load images
blank_square = pygame.image.load('images/blank_square.png').convert()
mountain_square = pygame.image.load('images/mountain_square.png').convert()
river_square = pygame.image.load('images/river_square.png').convert()
ocean_square = pygame.image.load('images/ocean_square.png').convert()

# Scale images to fit squares
blank_square = pygame.transform.scale(blank_square, (SQUARE_SIZE, SQUARE_SIZE))
mountain_square = pygame.transform.scale(mountain_square, (SQUARE_SIZE, SQUARE_SIZE))
river_square = pygame.transform.scale(river_square, (SQUARE_SIZE, SQUARE_SIZE))
ocean_square = pygame.transform.scale(ocean_square, (SQUARE_SIZE, SQUARE_SIZE))

# List of possible non-river, non-ocean images
non_special_images = [blank_square, mountain_square]

# Function to check if a river square can be placed at (row, col)
def can_place_river(board, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == river_square:
            return True
    return False

# Function to check if an ocean square can be placed at (row, col)
def can_place_ocean(board, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == ocean_square:
            return True
    return False

# Function to generate the initial board
def generate_board():
    board = [[random.choice(non_special_images) for _ in range(COLS)] for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            if random.choice([True, False]):  # Randomly decide to attempt to place a river
                if can_place_river(board, row, col) or (row == 0 and col == 0):  # Allow first square to be river
                    board[row][col] = river_square
            elif random.choice([True, False]):  # Randomly decide to attempt to place an ocean
                if can_place_ocean(board, row, col) or (row == 0 and col == 0):  # Allow first square to be ocean
                    board[row][col] = ocean_square
    return board

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