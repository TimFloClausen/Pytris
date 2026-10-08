# Imported libraries
import pygame
# initializing pygames
pygame.init()


DELAY = 150  # Time in milliseconds between frames
WIN_SIZE_W = 700  # Window size (width) in pixels
WIN_SIZE_H = 900  # Window size (height) in pixels
board_x = 400 + 40
board_y = 800 + 40
    

window = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))
pygame.display.set_caption("Pytris")



run = True
while run:
    pygame.time.delay(DELAY)
    window.fill((0, 0, 0))
    x = 150
    counter = 0
    pygame.draw.rect(window, (0, 0, 255), 
                 [150, 50, 400, 800], 4)
    for i in range(20):
                line_pos = 153
                line_pos2 = 53
                pygame.draw.rect(window, (255, 255, 255),
                                [159, line_pos, 40, 40], 2)
                line_pos += 40
                pygame.draw.rect(window, (255, 255, 255),
                                [line_pos2, 50, 40, 40], 2)
                line_pos2 += 40
                
    
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False








