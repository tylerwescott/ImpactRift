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
RED = (255, 0, 0)
GREEN = (0, 255, 0)

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

# List of all possible images and their types
all_images = [
    (blank_square, "Blank"), (mountain_square, "Mountain"), (river_square, "River"), (ocean_square, "Ocean"),
    (plains_square, "Plains"), (forest_square, "Forest"), (desert_square, "Desert"), (tundra_square, "Tundra"),
    (volcano_square, "Volcano"), (meadow_square, "Meadow"), (plateau_square, "Plateau"), (swamp_square, "Swamp"),
    (canyon_square, "Canyon")
]

# List of possible non-river, non-ocean images
non_special_images = [
    blank_square, mountain_square, plains_square, forest_square, desert_square, tundra_square, volcano_square,
    meadow_square, plateau_square, swamp_square, canyon_square
]

# Function to check if a river square can be placed at (row, col)
def can_place_river(board, row, col):
    if board[row][col] == river_square:
        return False, "A river square is already here"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
    adjacent_rivers = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == river_square:
                adjacent_rivers += 1
    if adjacent_rivers == 1:
        return True, ""
    else:
        return False, "A river square must be adjacent to exactly one other river square"

# Function to check if an ocean square can be placed at (row, col)
def can_place_ocean(board, row, col):
    if board[row][col] == ocean_square:
        return False, "An ocean square is already here"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == ocean_square:
            return True, ""
    return False, "An ocean square must be adjacent to at least one other ocean square"

# Function to generate the initial board
def generate_board():
    board = [[random.choice(all_images)[0] for _ in range(COLS)] for _ in range(ROWS)]

    # Guarantee one river and one ocean tile
    river_start_row, river_start_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
    ocean_start_row, ocean_start_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)

    # Ensure that the starting positions are not the same
    while ocean_start_row == river_start_row and ocean_start_col == river_start_col:
        ocean_start_row, ocean_start_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)

    board[river_start_row][river_start_col] = river_square
    board[ocean_start_row][ocean_start_col] = ocean_square

    # Place additional river and ocean tiles based on their placement rules
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] not in [river_square,
                                       ocean_square]:  # Only attempt to place if the square is not already set
                if random.choice([True, False]):  # Randomly decide to attempt to place a river
                    valid, _ = can_place_river(board, row, col)
                    if valid:
                        board[row][col] = river_square
                elif random.choice([True, False]):  # Randomly decide to attempt to place an ocean
                    valid, _ = can_place_ocean(board, row, col)
                    if valid:
                        board[row][col] = ocean_square
    return board

# Generate the initial board
board = generate_board()

# Function to generate the player's hand
def generate_hand():
    return [random.choice(all_images)[0] for _ in range(HAND_SIZE)]

# Generate the player's hand
hand = generate_hand()
selected_tile = None  # Track the currently selected tile from the hand
valid_positions = []  # Track valid positions for the selected tile

# Function to draw the game board and the player's hand
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            screen.blit(board[row][col], (col * SQUARE_SIZE, row * SQUARE_SIZE))
    # Draw the player's hand at the bottom of the screen, centered
    hand_start_x = (WIDTH - (HAND_SIZE * SQUARE_SIZE)) // 2
    hand_start_y = HEIGHT - SQUARE_SIZE - PADDING
    for i, tile in enumerate(hand):
        screen.blit(tile, (hand_start_x + i * SQUARE_SIZE, hand_start_y))

# Function to display the tooltip
def display_tooltip(messages, position, color):
    font = pygame.font.Font(None, 24)
    y_offset = 0
    for message in messages:
        text = font.render(message, True, color)
        screen.blit(text, (position[0], position[1] + y_offset))
        y_offset += text.get_height() + 2

# Function to draw outlines for valid positions
def draw_valid_outlines(valid_positions):
    for row, col in valid_positions:
        pygame.draw.rect(screen, GREEN, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

# Function to get the type of square at (row, col)
def get_square_type(square):
    for image, name in all_images:
        if square == image:
            return name
    return "Unknown"

# Main loop
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    hand_start_x = (WIDTH - (HAND_SIZE * SQUARE_SIZE)) // 2
    hand_start_y = HEIGHT - SQUARE_SIZE - PADDING
    hovered_row = mouse_y // SQUARE_SIZE
    hovered_col = mouse_x // SQUARE_SIZE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click event
            if hand_start_y <= mouse_y < hand_start_y + SQUARE_SIZE:
                for i in range(HAND_SIZE):
                    if hand_start_x + i * SQUARE_SIZE <= mouse_x < hand_start_x + (i + 1) * SQUARE_SIZE:
                        selected_tile = hand[i]  # Select the tile from the hand
                        # Determine valid positions for the selected tile
                        valid_positions = []
                        for row in range(ROWS):
                            for col in range(COLS):
                                if selected_tile == river_square:
                                    valid, _ = can_place_river(board, row, col)
                                    if valid:
                                        valid_positions.append((row, col))
                                elif selected_tile == ocean_square:
                                    valid, _ = can_place_ocean(board, row, col)
                                    if valid:
                                        valid_positions.append((row, col))
                                elif selected_tile not in [river_square, ocean_square] and board[row][col] != selected_tile:
                                    valid_positions.append((row, col))
            elif 0 <= hovered_row < ROWS and 0 <= hovered_col < COLS and selected_tile:
                if selected_tile == river_square:
                    valid, reason = can_place_river(board, hovered_row, hovered_col)
                    if valid:
                        board[hovered_row][hovered_col] = selected_tile  # Place the selected river tile on the board
                elif selected_tile == ocean_square:
                    valid, reason = can_place_ocean(board, hovered_row, hovered_col)
                    if valid:
                        board[hovered_row][hovered_col] = selected_tile  # Place the selected ocean tile on the board
                elif selected_tile not in [river_square, ocean_square] and board[hovered_row][hovered_col] != selected_tile:
                    valid = True
                    board[hovered_row][hovered_col] = selected_tile  # Place the selected tile on the board
                else:
                    valid = False
                    reason = "A {} square is already here".format(get_square_type(selected_tile))

                # Clear selection and valid positions after placement
                if valid:
                    selected_tile = None
                    valid_positions = []

    screen.fill(WHITE)  # Fill the screen with white color
    draw_board()  # Draw the game board

    # Draw outlines for valid positions if a tile is selected
    if selected_tile:
        draw_valid_outlines(valid_positions)

    # Display the tooltip near the cursor
    if 0 <= hovered_row < ROWS and 0 <= hovered_col < COLS:
        square_type = get_square_type(board[hovered_row][hovered_col])
        messages = [f"Square type: {square_type}"]
        if selected_tile:
            if selected_tile == river_square:
                valid, reason = can_place_river(board, hovered_row, hovered_col)
                if valid:
                    messages.append("Valid placement")
                else:
                    messages.append(f"Invalid placement: {reason}")
            elif selected_tile == ocean_square:
                valid, reason = can_place_ocean(board, hovered_row, hovered_col)
                if valid:
                    messages.append("Valid placement")
                else:
                    messages.append(f"Invalid placement: {reason}")
            else:
                if board[hovered_row][hovered_col] != selected_tile:
                    messages.append("Valid placement")
                else:
                    messages.append("Invalid placement: This tile is already here")
        display_tooltip(messages, (mouse_x + 15, mouse_y), RED if "Invalid" in messages[-1] else GREEN)

    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()