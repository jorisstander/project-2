import pygame #help us access pygame
import time
from pygame.locals import *



red    = (0, 255, 0)
black  = (0, 0, 0)
bg     = pygame.image.load("C:/Users/PC Joris/Documents/Visual Studio 2015/Projects/game/bg.jpg")
menubg = pygame.image.load("C:/Users/PC Joris/Documents/Visual Studio 2015/Projects/game/main menu.jpg")
score  = 0

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                return False
    return True


#main program logic
def program():
    pass
    #start pygame functionality
    pygame.init()

    #font of intro
    title = pygame.font.Font("C:/Windows/Fonts/Bad Coma.ttf", 150)
    font  = pygame.font.Font("C:/Windows/Fonts/headliner.ttf",80)
    #size of display
    width = 1920
    heigth = 1080
    size = (width, heigth)    
    #give display a variable
    screen = pygame.display.set_mode(size)

        # startscherm
    while process_events():
        # background draw
        screen.fill(black)
        screen.blit(bg,(0,0))     
        # draw text  
        intro_name     = title.render(        "BATTLEPORT"    , 1, (255, 255, 255))
        enter_continue = font.render("Press enter to continue", 1, (255, 255, 255))
        screen.blit(intro_name,    ( 150, 250))
        screen.blit(enter_continue,(450,900)) 
        pygame.display.flip()

    while process_events():
        #background draw
        screen.fill(black)
        screen.blit(menubg,(0,0))
        #draw score
        intro_name     = title.render(        "BATTLEPORT"    , 1, (255, 255, 255))
        enter_continue = font.render("Press enter to continue", 1, (255, 255, 255))
        screen.blit(intro_name,    ( 150, 250))
        screen.blit(enter_continue,(450,900))
        pygame.display.flip()
        
#run the main program
program()