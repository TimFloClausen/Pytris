# Imported libraries
import pygame
import random
# initializing pygames
pygame.init()


DELAY = 62 # Time in milliseconds between frames
WIN_SIZE_W = 700  # Window size (width) in pixels
WIN_SIZE_H = 900  # Window size (height) in pixels
SPAWNX = 350
SPAWNY = 50
SPEED_COUNTER = 0

landed_blocks = []

    
    


window = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))
pygame.display.set_caption("Pytris")

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, 40 - 2, 40 - 2)
field = [[0 for i in range(W)] for j in range(H)]

def draw():
    for i in range(4):
    figure_rect.x = figure[i].x * 40
    figure_rect.y = figure[i].y * 40
    pygame.draw.rect(game_sc, pygame.Color('white'), figure_rect)
         

        
        

def movement(x, y):
    keys = pygame.key.get_pressed()
    if y < 690:
        if keys[pygame.K_d] and x + 40 <= 510:
            x += 40
        elif keys[pygame.K_a] and x - 40 >= 150:
            x -= 40
        elif keys[pygame.K_s]:
            y += 40
    return x, y

def random_block():
    


run = True
while run:
    pygame.time.get_ticks()
    pygame.time.delay(DELAY)
    window.fill((10, 10, 10))
    block_locked = False

    
    pygame.draw.rect(window, (0, 0, 255), 
                 [146, 46, 408, 808], 4)
    
    lenght = 150
    counter = 0
    high = 10
    draw()
    SPAWNX, SPAWNY = movement(SPAWNX, SPAWNY)
    


         
    SPEED_COUNTER += 1

    if SPEED_COUNTER == 8:
            SPAWNY += 40
            SPEED_COUNTER = 0

     




         
         
    
    if SPAWNY >= 690:
        SPAWNY = 690
        landed_blocks.append((SPAWNX, SPAWNY))
        print(landed_blocks)
        block_0()
        SPAWNX, SPAWNY = movement(SPAWNX, SPAWNY)
    
    
    
    
         

    for i in range(200):
        if counter % 10 == 0 and counter <= 200:
                high += 40
        if counter % 10 == 0 and counter <= 200:
             lenght = 150
  
        for i in range(10):
            pygame.draw.rect(window, (255, 255, 255),
                                [lenght, high, 40, 40], 1)
        counter += 1      
        lenght += 40
    

    

                
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False