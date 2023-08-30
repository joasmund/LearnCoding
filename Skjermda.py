import pygame
import sys

# Initialize pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'MyMans.jpg'
image = pygame.image.load(image_path)

# Get the dimensions of the image
image_width, image_height = image.get_rect().size

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with black

    # Display the image in the center of the screen
    screen.blit(image, ((screen_width - image_width) // 2, (screen_height - image_height) // 2))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
