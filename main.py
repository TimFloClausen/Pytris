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
SPAWN = (SPAWNX, SPAWNY)

landed_blocks = []

ROTATION = False
    
    


window = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))
pygame.display.set_caption("Pytris")

def block_I():
        block_I_1 = pygame.image.load("pictures/I_Block_1.png")
        window.blit(block_I_1, (SPAWNX, SPAWNY))

def block_O():
    block_O_1 = pygame.image.load("pictures/O_Block.png")
    window.blit(block_O_1, (SPAWNX, SPAWNY))

def movement(SPAWNX, SPAWNY):
    keys = pygame.key.get_pressed()
    if SPAWNY < 690:
        if keys[pygame.K_d] and SPAWNX + 40 <= 510:
            SPAWNX += 40
        elif keys[pygame.K_a] and SPAWNX - 40 >= 150:
            SPAWNX -= 40
        elif keys[pygame.K_s]:
            SPAWNY += 40
        elif keys[pygame.K_SPACE]:
            print
    return SPAWNX, SPAWNY




def random_block():
    random(1, 2,)



run = True
while run:
    ROTATION = True
    pygame.time.get_ticks()
    pygame.time.delay(DELAY)
    window.fill((10, 10, 10))
    block_locked = False

    
    pygame.draw.rect(window, (0, 0, 255), 
                 [146, 46, 408, 808], 4)
    
    lenght = 150
    counter = 0
    high = 10
    block_I()

    SPAWNX, SPAWNY = movement(SPAWNX, SPAWNY)
    
   
    
    


         
    SPEED_COUNTER += 1

    if SPEED_COUNTER == 8:
            SPAWNY += 40
            SPEED_COUNTER = 0

     




         
         
    
    if SPAWNY >= 690:
        SPAWNY = 690
        landed_blocks.append((SPAWNX, SPAWNY))
        block_O()
        
    
    
    
    
         

    for i in range(200):
        if counter % 10 == 0 and counter <= 200:
                high += 40
        if counter % 10 == 0 and counter <= 200:
             lenght = 150
  
        for i in range(10):
            pygame.draw.rect(window, (200, 200, 200),
                                [lenght, high, 40, 40], 1)
        counter += 1      
        lenght += 40
    

    

                
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False