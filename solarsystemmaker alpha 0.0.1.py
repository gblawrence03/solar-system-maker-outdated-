import pygame
import sys
import math

screensize = (1280,720) 
gconst = 6.673 * 10**-11
systemSize = 7200000000
screenConversion = systemSize / screensize[1]
pygame.init()
screen = pygame.display.set_mode(screensize)
pygame.display.flip()

class planet:
    def __init__(self,name,colour,xpos,ypos):
        self.colour = colour
        self.name = name
        self.distance = math.sqrt(xpos**2 + ypos**2)

class star:
    def __init__(self,name,xpos,ypos,mass):
        self.xpos = xpos
        self.ypos = ypos
        self.name = name
        self.mass = mass
    def convertKmToPixels(self):
        global screenConversion
        self.screenx = self.xpos / screenConversion
        self.screeny = self.ypos / screenConversion
    def draw(self):
        pygame.draw.circle(screen,(255,255,0),(int(self.screenx),int(self.screeny)),5)

def main():
    print(systemSize)
    starX = int(input("X kilometres of star?"))
    starY = int(input("Y kilometres of star?"))
    global sun
    sun = star("sun",starX,starY,1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        drawFrame()

def drawFrame():
    sun.convertKmToPixels()
    sun.draw()
    pygame.display.update()
    
main()



                
    
