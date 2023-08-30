import pygame
import time

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

# Initialize pygame
pygame.init()

# Set the path to your MP3 file
mp3_file_path = 'Barbiesong.mp3'

# Initialize the mixer module
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load(mp3_file_path)

# Play the MP3 file
pygame.mixer.music.play()

# Allow time for the music to play
time.sleep(30)  # Adjust the duration as needed

# Stop the music
pygame.mixer.music.stop()

# Quit pygame
pygame.quit()
