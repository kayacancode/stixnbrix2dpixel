import pygame, sys
from button import Button
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")


def main_menu():
    font = pygame.font.Font('fonts/IBMPlexMono-Bold.ttf', 18)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    messages = ["Mario: Hello! My name is Mario and I am the owner of Stix n Brixs",
                "Welcome to my coffee shop.",
                "Welcome to your first shift, I am glad to have you here.",
                "Lets get started by visiting the stations. You have 3 options."]

    snip = font.render(' ', True, 'white')
    counter = 0
    speed = 3
    active_message = 0
    message = messages[active_message]
    done = False

    pygame.display.set_caption('Stix n Brix')
    # background 
    background = pygame.image.load('assets/bg.png')
    # mario 
    mario = pygame.image.load('assets/mario.png')

    player_x = 300
    player_y = 100

    # Create three buttons
    station1_img = font.render('Station 1', True, 'white')
    station2_img = font.render('Station 2', True, 'white')
    station3_img = font.render('Station 3', True, 'white')
    button_padding = 10
    button_width = station1_img.get_width() + button_padding * 2
    button_height = station1_img.get_height() + button_padding * 2
    button1 = Button(None, (SCREEN_WIDTH//2 - button_width, 50), 'Station 1', font, 'white', 'gray')
    button2 = Button(None, (SCREEN_WIDTH//2, 50), 'Station 2', font, 'white', 'gray')
    button3 = Button(None, (SCREEN_WIDTH//2 + button_width, 50), 'Station 3', font, 'white', 'gray')

    run = True
    while run:
        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        timer.tick(60)

        # Draw buttons
        button1.update(screen)
        button2.update(screen)
        button3.update(screen)

        pygame.draw.rect(screen, 'black', [0, 400, 800, 100])

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
        screen.blit(snip, (10, 400))
        screen.blit(mario, (player_x,player_y))

        pygame.display.flip()

    pygame.quit()
