import pygame
import sys
import math

global planetdict
planetdict = {}
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
        self.xpos = xpos
        self.ypos = ypos
        self.distance = math.sqrt(xpos**2 + ypos**2)
    def convertKmToPixels(self):
        global screenConversion
        self.screenx = self.xpos / screenConversion
        self.screeny = self.ypos / screenConversion
    def draw(self):
        pygame.draw.circle(screen,self.colour,(int(self.screenx),int(self.screeny)),5)

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
    collectInput()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(planetdict)
                pygame.quit()
                sys.exit()
        drawFrame()

def drawFrame():    
    sun.convertKmToPixels()
    sun.draw()
    drawPlanets()
    pygame.display.update()

def collectInput():
    global planetdict
    totalPlanets = int(input("How many planets would you like? "))
    for i in range(0,totalPlanets):
        message = "What would you like planet " + str(i+1) + " to be called? "
        name = input(message)
        message = "How much red would you like " + name + " to contain? "
        red = int(input(message))
        message = "How much green would you like " + name + " to contain? "
        green = int(input(message))
        message = "How much blue would you like " + name + " to contain? "
        blue = int(input(message))
        colour = (red,green,blue)
        message = "What would you like the X Kilometres of " + name + " to be? "
        xpos = int(input(message))
        message = "What would you like the Y Kilometres of " + name + " to be? "
        ypos = int(input(message))
        planetdict[i] = planet(name,colour,xpos,ypos)

def drawPlanets():
    for i in range (0,len(planetdict)):
        planetdict[i].convertKmToPixels()
        planetdict[i].draw()
        
main()



    
