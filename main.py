import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 700  # Adjust the width and height of the window
ROWS, COLS = 6, 8         # Number of rows and columns in the game board
SQUARE_SIZE = WIDTH // COLS  # Size of each square
HAND_SIZE = 5              # Number of tiles in the player's hand
PADDING = 10               # Padding between the board and the hand

# Colors
WHITE = (255, 255, 255)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Impact Rift")

# Load images from the 'images' directory
blank_square = pygame.image.load('images/blank_square.png').convert()
mountain_square = pygame.image.load('images/mountain_square.png').convert()
river_square = pygame.image.load('images/river_square.png').convert()
ocean_square = pygame.image.load('images/ocean_square.png').convert()
plains_square = pygame.image.load('images/plains_square.png').convert()
forest_square = pygame.image.load('images/forest_square.png').convert()
desert_square = pygame.image.load('images/desert_square.png').convert()
tundra_square = pygame.image.load('images/tundra_square.png').convert()
volcano_square = pygame.image.load('images/volcano_square.png').convert()
meadow_square = pygame.image.load('images/meadow_square.png').convert()
plateau_square = pygame.image.load('images/plateau_square.png').convert()
swamp_square = pygame.image.load('images/swamp_square.png').convert()
canyon_square = pygame.image.load('images/canyon_square.png').convert()

# Scale images to fit squares
blank_square = pygame.transform.scale(blank_square, (SQUARE_SIZE, SQUARE_SIZE))
mountain_square = pygame.transform.scale(mountain_square, (SQUARE_SIZE, SQUARE_SIZE))
river_square = pygame.transform.scale(river_square, (SQUARE_SIZE, SQUARE_SIZE))
ocean_square = pygame.transform.scale(ocean_square, (SQUARE_SIZE, SQUARE_SIZE))
plains_square = pygame.transform.scale(plains_square, (SQUARE_SIZE, SQUARE_SIZE))
forest_square = pygame.transform.scale(forest_square, (SQUARE_SIZE, SQUARE_SIZE))
desert_square = pygame.transform.scale(desert_square, (SQUARE_SIZE, SQUARE_SIZE))
tundra_square = pygame.transform.scale(tundra_square, (SQUARE_SIZE, SQUARE_SIZE))
volcano_square = pygame.transform.scale(volcano_square, (SQUARE_SIZE, SQUARE_SIZE))
meadow_square = pygame.transform.scale(meadow_square, (SQUARE_SIZE, SQUARE_SIZE))
plateau_square = pygame.transform.scale(plateau_square, (SQUARE_SIZE, SQUARE_SIZE))
swamp_square = pygame.transform.scale(swamp_square, (SQUARE_SIZE, SQUARE_SIZE))
canyon_square = pygame.transform.scale(canyon_square, (SQUARE_SIZE, SQUARE_SIZE))

all_images = [
    blank_square, mountain_square, river_square, ocean_square, plains_square, forest_square,
    desert_square, tundra_square, volcano_square, meadow_square, plateau_square, swamp_square, canyon_square
]
# List of possible non-river, non-ocean images
non_special_images = [
    blank_square, mountain_square, plains_square, forest_square, desert_square, tundra_square, volcano_square,
    meadow_square, plateau_square, swamp_square, canyon_square
]

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

# Function to generate the player's hand
def generate_hand():
    return [random.choice(all_images) for _ in range(HAND_SIZE)]

# Generate the player's hand
hand = generate_hand()
selected_tile = None  # Track the currently selected tile from the hand

# Function to draw the game board and the player's hand
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            screen.blit(board[row][col], (col * SQUARE_SIZE, row * SQUARE_SIZE))
    # Draw the player's hand at the bottom of the screen, centered
    hand_start_x = (WIDTH - (HAND_SIZE * SQUARE_SIZE)) // 2
    hand_start_y = HEIGHT - SQUARE_SIZE + PADDING
    for i, tile in enumerate(hand):
        screen.blit(tile, (hand_start_x + i * SQUARE_SIZE, hand_start_y))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click event
            mouse_x, mouse_y = event.pos
            hand_start_x = (WIDTH - (HAND_SIZE * SQUARE_SIZE)) // 2
            hand_start_y = HEIGHT - SQUARE_SIZE - PADDING
            clicked_row = mouse_y // SQUARE_SIZE
            clicked_col = mouse_x // SQUARE_SIZE
            if hand_start_y <= mouse_y < hand_start_y + SQUARE_SIZE:
                for i in range(HAND_SIZE):
                    if hand_start_x + i * SQUARE_SIZE <= mouse_x < hand_start_x + (i + 1) * SQUARE_SIZE:
                        selected_tile = hand[i]  # Select the tile from the hand
            elif 0 <= clicked_row < ROWS and 0 <= clicked_col < COLS and selected_tile:
                board[clicked_row][clicked_col] = selected_tile  # Place the selected tile on the board

    screen.fill(WHITE)  # Fill the screen with white color
    draw_board()  # Draw the game board

    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()