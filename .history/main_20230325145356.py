import pygame

pygame.init()

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

SCREEN_WIDTH= 800
SCREEN_HEIGHT = 700

font = pygame.font.Font('fonts/IBMPlexMono-Bold.ttf', 18)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
timer = pygame.time.Clock()
messages = ["Mario: Hello! My name is Mario and I am the owner of Stix n Brixs",
            "Welcome to my coffee shop.",
            "Welcome to your first shift, I am glad to have you here."]

snip = font.render(' ', True, 'white')
counter = 0
speed = 3
active_message = 0
message = messages[active_message]
done = False


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
run = True 
while run:
    timer.tick(60)
    pygame.draw.rect(screen, 'black', [0, 300, 800, 200])
    if counter < speed * len(message):
        counter += 1
    elif counter >= speed*len(message):
        done = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done and active_message < len(messages):
                active_message += 1
                done = False
                message = messages[active_message]
                counter = 0
    
    snip = font.render(message[0:counter//speed], True, 'white')
    screen.blit(snip, (10, 310))
    screen.blit(background,(0,0))
    screen.blit(mario, (player_x,player_y))


    pygame.display.update()

    # pygame.display.flip()

pygame.quit()
