import pygame

pygame.init()

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

SCREEN_WIDTH= 800
SCREEN_HEIGHT = 800


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Stix n Brix')
# background 
background = pygame.image.load('assets/bg.png')
#mario 
mario = pygame.image.load('assets/mario.png')

# create font object
font = pygame.font.Font(None, 25)


pygame.display.update()


player_x = 300
player_y = 100
#game loop 
running = True 
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.blit(background,(0,0))
    screen.blit(mario, (player_x,player_y))


    pygame.display.update()

pygame.quit()

def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        screen.blit(background,(0,0))
        station1_button = 
        station1_button = 
        station1_button = 