import pygame
import time

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
