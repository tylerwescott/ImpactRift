import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 2200, 1400
HEX_RADIUS = 80  # Hexagon radius
PADDING = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Impact Rift")


# Helper function to calculate hexagon points
def hexagon_points(center_x, center_y, radius):
    points = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((x, y))
    return points


# Helper function to create a hexagon mask
def create_hex_mask(radius):
    mask = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    mask = mask.convert_alpha()
    mask.fill((0, 0, 0, 0))
    points = hexagon_points(radius, radius, radius)
    pygame.draw.polygon(mask, (255, 255, 255, 255), points)
    return mask


# Helper function to apply a mask to an image
def apply_hex_mask(image, mask):
    masked_image = image.copy()
    masked_image.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return masked_image


# Scale images to fit hexagons and apply mask
def scale_and_mask_image(image, radius):
    scaled_image = pygame.transform.scale(image, (int(2 * radius), int(2 * radius)))
    mask = create_hex_mask(radius)
    return apply_hex_mask(scaled_image, mask)


# Load and process images
try:
    blank_square = scale_and_mask_image(pygame.image.load('images/blank_square.png').convert_alpha(), HEX_RADIUS)
    mountain_square = scale_and_mask_image(pygame.image.load('images/mountain_square.png').convert_alpha(), HEX_RADIUS)
    river_square = scale_and_mask_image(pygame.image.load('images/river_square.png').convert_alpha(), HEX_RADIUS)
    ocean_square = scale_and_mask_image(pygame.image.load('images/ocean_square.png').convert_alpha(), HEX_RADIUS)
    plains_square = scale_and_mask_image(pygame.image.load('images/plains_square.png').convert_alpha(), HEX_RADIUS)
    forest_square = scale_and_mask_image(pygame.image.load('images/forest_square.png').convert_alpha(), HEX_RADIUS)
    desert_square = scale_and_mask_image(pygame.image.load('images/desert_square.png').convert_alpha(), HEX_RADIUS)
    tundra_square = scale_and_mask_image(pygame.image.load('images/tundra_square.png').convert_alpha(), HEX_RADIUS)
    volcano_square = scale_and_mask_image(pygame.image.load('images/volcano_square.png').convert_alpha(), HEX_RADIUS)
    meadow_square = scale_and_mask_image(pygame.image.load('images/meadow_square.png').convert_alpha(), HEX_RADIUS)
    plateau_square = scale_and_mask_image(pygame.image.load('images/plateau_square.png').convert_alpha(), HEX_RADIUS)
    swamp_square = scale_and_mask_image(pygame.image.load('images/swamp_square.png').convert_alpha(), HEX_RADIUS)
    canyon_square = scale_and_mask_image(pygame.image.load('images/canyon_square.png').convert_alpha(), HEX_RADIUS)

    # Load the element images without masks
    fire_square = pygame.image.load('images/fire_square.png').convert_alpha()
    fire_square = pygame.transform.scale(fire_square, (int(2 * HEX_RADIUS), int(2 * HEX_RADIUS)))

    light_square = pygame.image.load('images/light_square.png').convert_alpha()
    light_square = pygame.transform.scale(light_square, (int(2 * HEX_RADIUS), int(2 * HEX_RADIUS)))

    air_square = pygame.image.load('images/air_square.png').convert_alpha()
    air_square = pygame.transform.scale(air_square, (int(2 * HEX_RADIUS), int(2 * HEX_RADIUS)))

    water_square = pygame.image.load('images/water_square.png').convert_alpha()
    water_square = pygame.transform.scale(water_square, (int(2 * HEX_RADIUS), int(2 * HEX_RADIUS)))

    dark_square = pygame.image.load('images/dark_square.png').convert_alpha()
    dark_square = pygame.transform.scale(dark_square, (int(2 * HEX_RADIUS), int(2 * HEX_RADIUS)))

    earth_square = pygame.image.load('images/earth_square.png').convert_alpha()
    earth_square = pygame.transform.scale(earth_square, (int(2 * HEX_RADIUS), int(2 * HEX_RADIUS)))

    push_square = pygame.image.load('images/push_square.png').convert_alpha()
    push_square = pygame.transform.scale(push_square, (int(2 * HEX_RADIUS), int(2 * HEX_RADIUS)))

    pull_square = pygame.image.load('images/pull_square.png').convert_alpha()
    pull_square = pygame.transform.scale(pull_square, (int(2 * HEX_RADIUS), int(2 * HEX_RADIUS)))

except pygame.error as e:
    print(f"Error loading image: {e}")
    sys.exit(1)

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

# List of element images and their corresponding land types
element_to_land = {
    fire_square: volcano_square,  # Volcano represents Fire
    light_square: meadow_square,  # Meadow represents Light
    air_square: mountain_square,  # Mountain represents Air
    push_square: plateau_square,  # Plateau represents Push
    water_square: ocean_square,  # Ocean represents Water
    dark_square: swamp_square,  # Swamp represents Dark
    earth_square: forest_square,  # Forest represents Earth
    pull_square: canyon_square  # Canyon represents Pull
}

# List of element names
element_names = {
    fire_square: "Fire",
    light_square: "Light",
    air_square: "Air",
    water_square: "Water",
    dark_square: "Dark",
    earth_square: "Earth",
    push_square: "Push",
    pull_square: "Pull"
}

# Define HAND_SIZE after element_images is defined
HAND_SIZE = len(element_to_land)


# Function to draw a hexagon
def draw_hexagon(surface, color, center_x, center_y, radius, border_width=0):
    points = hexagon_points(center_x, center_y, radius)
    pygame.draw.polygon(surface, color, points, border_width)


# Function to generate the initial board
def generate_board():
    board = [
        [None, None, None, random.choice(all_images)[0], random.choice(all_images)[0], random.choice(all_images)[0],
         None, None, None],
        [None, random.choice(all_images)[0], random.choice(all_images)[0], random.choice(all_images)[0],
         random.choice(all_images)[0], random.choice(all_images)[0],
         random.choice(all_images)[0], random.choice(all_images)[0], None],
        [None, random.choice(all_images)[0], random.choice(all_images)[0], random.choice(all_images)[0],
         random.choice(all_images)[0],
         random.choice(all_images)[0], random.choice(all_images)[0], random.choice(all_images)[0], None],
        [None, random.choice(all_images)[0], random.choice(all_images)[0], random.choice(all_images)[0],
         random.choice(all_images)[0], random.choice(all_images)[0], random.choice(all_images)[0],
         random.choice(all_images)[0], None],
        [None, random.choice(all_images)[0], random.choice(all_images)[0], random.choice(all_images)[0],
         random.choice(all_images)[0],
         random.choice(all_images)[0], random.choice(all_images)[0], random.choice(all_images)[0], None],
        [None, None, random.choice(all_images)[0], random.choice(all_images)[0], random.choice(all_images)[0],
         random.choice(all_images)[0],
         random.choice(all_images)[0], None, None],
        [None, None, None, None, random.choice(all_images)[0], None, None, None, None]
    ]
    return board


# Generate the initial board
board = generate_board()


# Function to generate the player's hand
def generate_hand():
    return list(element_to_land.keys())


# Generate the player's hand
hand = generate_hand()
selected_tile = None  # Track the currently selected tile from the hand
valid_positions = []  # Track valid positions for the selected tile


# Function to draw the game board and the player's hand
def draw_board():
    offset_x = WIDTH // 2  # Center the board horizontally
    offset_y = HEX_RADIUS  # Move the board up to just below the top of the window

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] is not None:
                x = offset_x + (col - 4) * (HEX_RADIUS * 3 // 2)  # Center the diamond shape with 9 columns
                y = offset_y + row * (math.sqrt(3) * HEX_RADIUS)  # Adjusted for additional rows
                if col % 2 == 1:
                    y += HEX_RADIUS * math.sqrt(3) / 2  # Offset for odd columns
                draw_hexagon(screen, WHITE, x, y, HEX_RADIUS)
                tile = board[row][col] if board[row][col] is not None else blank_square
                screen.blit(tile, (x - HEX_RADIUS, y - HEX_RADIUS))

    # Draw the player's hand at the bottom of the screen, centered
    hand_start_x = (WIDTH - (HAND_SIZE * HEX_RADIUS * 2) - (HAND_SIZE - 1) * PADDING) // 2
    hand_start_y = HEIGHT - HEX_RADIUS * 2 - PADDING
    for i, tile in enumerate(hand):
        x = hand_start_x + i * (HEX_RADIUS * 2 + PADDING)
        y = hand_start_y
        draw_hexagon(screen, WHITE, x, y, HEX_RADIUS)
        screen.blit(tile, (x - HEX_RADIUS, y - HEX_RADIUS))


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
    offset_x = WIDTH // 2  # Center the board horizontally
    offset_y = HEX_RADIUS  # Move the board up to just below the top of the window

    for row, col in valid_positions:
        x = offset_x + (col - 4) * (HEX_RADIUS * 3 // 2)  # Center the diamond shape with 9 columns
        y = offset_y + row * (math.sqrt(3) * HEX_RADIUS)  # Adjusted for additional rows
        if col % 2 == 1:
            y += HEX_RADIUS * math.sqrt(3) / 2  # Offset for odd columns
        draw_hexagon(screen, GREEN, x, y, HEX_RADIUS, border_width=3)


# Function to get the type of square at (row, col)
def get_square_type(tile):
    for image, name in all_images:
        if tile == image:
            return name
    for image, name in element_names.items():
        if tile == image:
            return name
    return "Unknown"


# Function to get the type of element and the corresponding land type
def get_element_and_land_type(element_tile):
    for element, land in element_to_land.items():
        if element_tile == element:
            element_name = element_names.get(element, "Unknown")
            land_name = get_square_type(land)
            return element_name, land_name
    return "Unknown", "Unknown"


# Main loop
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    hand_start_x = (WIDTH - (HAND_SIZE * HEX_RADIUS * 2) - (HAND_SIZE - 1) * PADDING) // 2
    hand_start_y = HEIGHT - HEX_RADIUS * 2 - PADDING

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hand_start_y <= mouse_y < hand_start_y + HEX_RADIUS * 2:
                for i in range(HAND_SIZE):
                    hand_x = hand_start_x + i * (HEX_RADIUS * 2 + PADDING)
                    if hand_x <= mouse_x < hand_x + HEX_RADIUS * 2:
                        selected_tile = hand[i]  # Select the tile from the hand
                        # Determine valid positions for the selected tile
                        valid_positions = []
                        for row in range(len(board)):
                            for col in range(len(board[row])):
                                if board[row][col] is not None:
                                    valid = board[row][col] != selected_tile
                                    if valid:
                                        valid_positions.append((row, col))
            elif 0 <= mouse_x < WIDTH and 0 <= mouse_y < HEIGHT and selected_tile:
                for row in range(len(board)):
                    for col in range(len(board[row])):
                        if board[row][col] is not None:
                            offset_x = WIDTH // 2  # Center the board horizontally
                            offset_y = HEX_RADIUS  # Move the board up to just below the top of the window
                            x = offset_x + (col - 4) * (HEX_RADIUS * 3 // 2)  # Center the diamond shape with 9 columns
                            y = offset_y + row * (math.sqrt(3) * HEX_RADIUS)  # Adjusted for additional rows
                            if col % 2 == 1:
                                y += HEX_RADIUS * math.sqrt(3) / 2  # Offset for odd columns
                            if math.sqrt((mouse_x - x) ** 2 + (mouse_y - y) ** 2) <= HEX_RADIUS:
                                # Place the corresponding land tile on the board, not the element image
                                if selected_tile in element_to_land:
                                    board[row][col] = element_to_land[selected_tile]
                                    selected_tile = None
                                    valid_positions = []

    screen.fill(WHITE)  # Fill the screen with white color
    draw_board()  # Draw the game board

    # Draw outlines for valid positions if a tile is selected
    if selected_tile:
        draw_valid_outlines(valid_positions)

    # Display the tooltip near the cursor
    if 0 <= mouse_x < WIDTH and 0 <= mouse_y < HEIGHT:
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] is not None:
                    offset_x = WIDTH // 2  # Center the board horizontally
                    offset_y = HEX_RADIUS  # Move the board up to just below the top of the window
                    x = offset_x + (col - 4) * (HEX_RADIUS * 3 // 2)  # Center the diamond shape with 9 columns
                    y = offset_y + row * (math.sqrt(3) * HEX_RADIUS)  # Adjusted for additional rows
                    if col % 2 == 1:
                        y += HEX_RADIUS * math.sqrt(3) / 2  # Offset for odd columns
                    if math.sqrt((mouse_x - x) ** 2 + (mouse_y - y) ** 2) <= HEX_RADIUS:
                        square_type = get_square_type(board[row][col])
                        messages = [f"Square type: {square_type}"]
                        display_tooltip(messages, (mouse_x + 15, mouse_y), BLACK)
                        break

    # Display the tooltip for the hand
    if hand_start_y <= mouse_y < hand_start_y + HEX_RADIUS * 2:
        for i in range(HAND_SIZE):
            hand_x = hand_start_x + i * (HEX_RADIUS * 2 + PADDING)
            if hand_x <= mouse_x < hand_x + HEX_RADIUS * 2:
                element_name, land_name = get_element_and_land_type(hand[i])
                display_tooltip([f"Element: {element_name}", f"Creates: {land_name}"], (mouse_x + 15, mouse_y), BLACK)

    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()