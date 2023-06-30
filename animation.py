import pygame, sys, time
from pygame.locals import *

#setup pygame
pygame.init()

#setup the window
WINDOWWIDTH = 1100
WINDOWHEIGHT = 800
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

#setup direction variables
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 8

#setup the colors
BG = (0, 0, 0)
RED = (225, 0, 50)
GREEN = (50, 200, 100)
BLUE = (50, 50, 225)
LAVENDER = (175, 150, 200)
GREY = (150, 150, 150)
BURGANDY = (100, 0, 50)
PEACH = (250, 100, 100)
BABYBLUE = (40, 200, 250)
BROWN = (200, 150, 100)
DGREY = (50, 50, 50)

#setup the box data structure
b1 = {'rect':pygame.Rect(400, 400, 90, 90), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(500, 175, 100, 100), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(200, 30, 120, 120), 'color':BLUE, 'dir':DOWNLEFT}
b4 = {'rect':pygame.Rect(100, 10, 200, 200), 'color':LAVENDER, 'dir':DOWNRIGHT}
b5 = {'rect':pygame.Rect(300, 700, 150, 150), 'color':GREY, 'dir':UPLEFT}
b6 = {'rect':pygame.Rect(600, 250, 100, 100), 'color':BURGANDY, 'dir':DOWNRIGHT}
b7 = {'rect':pygame.Rect(700, 600, 250, 250), 'color':PEACH, 'dir':DOWNLEFT}
b8 = {'rect':pygame.Rect(900, 375, 180, 180), 'color':BABYBLUE, 'dir':UPRIGHT}
b9 = {'rect':pygame.Rect(800, 60, 160, 160), 'color':BROWN, 'dir':UPRIGHT}
b10 = {'rect':pygame.Rect(525, 300, 160, 160), 'color':DGREY, 'dir':UPRIGHT}
boxes = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]

#run the game loop
while True:
    #check for the Quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #draw the white background on the surface
    windowSurface.fill(BG)

    for b in boxes:
        #move the box data structure
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        #check whther the box has moved out of the window
        if b['rect'].top < 0:
            #the box has moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT

        if b['rect'].bottom > WINDOWHEIGHT:
            #the box has moved past the bottom
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            #the box has moved past the left side
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            #the box has moved past the right side
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT

        #draw the box onto the surface
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    #draw the window onto the screen
    pygame.display.update()
    time.sleep(0.02)
