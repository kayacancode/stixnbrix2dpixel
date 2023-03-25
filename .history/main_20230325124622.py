import pygame

pygame.init()

SCREEN_WIDTH= 800
SCREEN_HEIGHT = 550

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Stix n Brix')
# background 
background = pygame.image.load('assets/bg.png')
#mario 
mario = pygame.image.load('assets/mario.png')



player_x = 500
player_y = 500
#game loop 
running = True 
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    screen.blit(background,(0,0))
    screen.blit(mario, (player_x,player_y))
    pygame.display.update()

pygame.quit()