# Imported libraries
import pygame
# initializing pygames
pygame.init()


DELAY = 150  # Time in milliseconds between frames
WIN_SIZE_W = 700  # Window size (width) in pixels
WIN_SIZE_H = 900  # Window size (height) in pixels
    

window = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))
pygame.display.set_caption("Pytris")

run = True
while run:
    pygame.time.delay(DELAY)
    pygame.draw.rect(window, (0, 0, 255), 
                 [150, 50, 400, 800], 2)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
window.fill((0, 0, 0))




