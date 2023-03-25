import pygame

pygame.init()

SCREEN_WIDTH= 800
SCREEN_HEIGHT = 550

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Stix n Brix')
# background 
background = pygame.image.load('assets/bg.png')
#mario 
mario = pygame.image.load('assets/baldman.png')

def add_character_at_location(x,y):
    screen.blid(mario, (x,y))

x = (SCREEN_WIDTH * 0.95)
y = (SCREEN_HEIGHT * 0.5)

#game loop 
running = True 
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    screen.blit(background,(0,0))
    add_character_at_location(x,y)
    pygame.display.update()

pygame.quit()