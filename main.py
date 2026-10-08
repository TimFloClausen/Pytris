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
    window.fill((10, 10, 10))

    
    pygame.draw.rect(window, (0, 0, 255), 
                 [148, 50, 408, 808], 4)
    lenght = 155
    counter = 0
    high = 14

    for i in range(200):
        if counter % 10 == 0 and counter <= 200:
                high += 40
        if counter % 10 == 0 and counter <= 200:
             lenght = 153
          
        for i in range(10):
            pygame.draw.rect(window, (255, 255, 255),
                                [lenght, high, 40, 40], 1)
        counter += 1      
        lenght += 40
                
                
                
    
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False








