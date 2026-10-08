# Imported libraries
import pygame
# initializing pygames
pygame.init()

def start():
    DELAY = 150  # Time in milliseconds between frames
    WIN_SIZE_W = 700  # Window size (width) in pixels
    WIN_SIZE_H = 900  # Window size (height) in pixels
    

    screen = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))
    pygame.display.set_caption("Pytris")

    run = True
    while run:
        pygame.time.delay(DELAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


start()