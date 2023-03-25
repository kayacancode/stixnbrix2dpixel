import pygame

pygame.init()

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

SCREEN_WIDTH= 800
SCREEN_HEIGHT = 800
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 30
PADDING = 10
BORDER_WIDTH = 2
BORDER_COLOR = BLACK

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Stix n Brix')
# background 
background = pygame.image.load('assets/bg.png')
#mario 
mario = pygame.image.load('assets/mario.png')

# create font object
font = pygame.font.Font(None, 25)

# create the buttons
button1 = pygame.Rect((SCREEN_WIDTH - (BUTTON_WIDTH * 3 + PADDING * 2)) / 2, SCREEN_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)
button2 = pygame.Rect(button1.right + PADDING, SCREEN_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)
button3 = pygame.Rect(button2.right + PADDING, SCREEN_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)

# draw the buttons with border
pygame.draw.rect(screen, BORDER_COLOR, button1, BORDER_WIDTH)
pygame.draw.rect(screen, GRAY, button1.inflate(-BORDER_WIDTH * 2, -BORDER_WIDTH * 2))
pygame.draw.rect(screen, BORDER_COLOR, button2, BORDER_WIDTH)
pygame.draw.rect(screen, GRAY, button2.inflate(-BORDER_WIDTH * 2, -BORDER_WIDTH * 2))
pygame.draw.rect(screen, BORDER_COLOR, button3, BORDER_WIDTH)
pygame.draw.rect(screen, GRAY, button3.inflate(-BORDER_WIDTH * 2, -BORDER_WIDTH * 2))

# add text to the buttons
text1 = font.render("Button 1", True, WHITE)
text2 = font.render("Button 2", True, WHITE)
text3 = font.render("Button 3", True, WHITE)

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

    screen.blit(text1, (button1.centerx - text1.get_width() / 2, button1.centery - text1.get_height() / 2))
    screen.blit(text2, (button2.centerx - text2.get_width() / 2, button2.centery - text2.get_height() / 2))
    screen.blit(text3, (button3.centerx - text3.get_width() / 2, button3.centery - text3.get_height() / 2))

    pygame.display.update()

pygame.quit()