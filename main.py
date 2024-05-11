import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600  # Adjust the width and height of the window
ROWS, COLS = 6, 8         # Number of rows and columns in the game board
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
plains_square = pygame.image.load('images/plains_square.png').convert()

# Scale images to fit squares
blank_square = pygame.transform.scale(blank_square, (SQUARE_SIZE, SQUARE_SIZE))
mountain_square = pygame.transform.scale(mountain_square, (SQUARE_SIZE, SQUARE_SIZE))
river_square = pygame.transform.scale(river_square, (SQUARE_SIZE, SQUARE_SIZE))
ocean_square = pygame.transform.scale(ocean_square, (SQUARE_SIZE, SQUARE_SIZE))
plains_square = pygame.transform.scale(plains_square, (SQUARE_SIZE, SQUARE_SIZE))

# List of possible non-river, non-ocean images
non_special_images = [blank_square, mountain_square, plains_square]

# Function to check if a river square can be placed at (row, col)
def can_place_river(board, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
    adjacent_rivers = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == river_square:
                adjacent_rivers += 1
    return adjacent_rivers == 1

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

    # Guarantee one river and one ocean tile
    river_start_row, river_start_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
    ocean_start_row, ocean_start_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)

    # Ensure that the starting positions are not the same
    while ocean_start_row == river_start_row and ocean_start_col == river_start_col:
        ocean_start_row, ocean_start_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)

    board[river_start_row][river_start_col] = river_square
    board[ocean_start_row][ocean_start_col] = ocean_square

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] in non_special_images:  # Only attempt to place if the square is not already set
                if random.choice([True, False]):  # Randomly decide to attempt to place a river
                    if can_place_river(board, row, col):
                        board[row][col] = river_square
                elif random.choice([True, False]):  # Randomly decide to attempt to place an ocean
                    if can_place_ocean(board, row, col):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click event
            mouse_x, mouse_y = event.pos
            clicked_row = mouse_y // SQUARE_SIZE
            clicked_col = mouse_x // SQUARE_SIZE
            if 0 <= clicked_row < ROWS and 0 <= clicked_col < COLS:
                board[clicked_row][clicked_col] = mountain_square  # Change the tile to a mountain

    screen.fill(WHITE)  # Fill the screen with white color
    draw_board()  # Draw the game board

    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()