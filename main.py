import pygame
import sys

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
# Replace 'square_large.png' with the path to the downloaded image file
image = pygame.image.load('square.png').convert()
image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            # Draw the image on each square
            screen.blit(image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

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