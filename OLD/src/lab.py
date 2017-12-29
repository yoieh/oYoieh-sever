#List = [UcList]
#UcList = [[UcY][UcX][UpList]]
#UpList = [[UpY][UpX][GcList]]
#GcList = [[GcY][GcX][GpList]]
#GpList = [[GpY][GpX][ScList]]
#ScList = [[ScY][ScX][SpList]]
#SpList = [[SpY][SpX][EcList]]
#EcList = [[EcY][EcX][EpList]]
#EpList = [[EpY][EpX][PcList]]
#PcList = [[PcY][PcX][PpList]]
#PpList = [[PpY][PpX][TList]]
#TList = [[TY][TX]]



from random import randint
import time 
import pprint
import pygame, sys
import socket
from pygame.locals import *
import math

class Mapping():
    
    def wordMapList(self):
        mapHight = 256
        mapWith = mapHight * 2
        MList = [[[[[[[(randint(0,255), randint(0,255), randint(0,255))]
                        for Tx in xrange(0, 16)]
                            for Ty in xrange(0, 16)] 
                                for Cx in xrange(0, mapHight/16)] 
                                    for Cy in xrange(0, (mapWith / 16) / 2)]
                                        for Si in xrange(0, 2)] 
                                            for Mi in xrange(0, 1)]
        return MList
    
    def spaceMapList(self):
        mapHight = 256
        mapWith = mapHight
        TList = [[[0] for x in xrange(0, 16)] for y in xrange(0, 16)]
        CList = [[TList for x in xrange(0, mapHight/16)] for y in xrange(0, mapWith / 16)]
        MList = [CList for i in xrange(0, 1)]
        return MList

class World():
    def Maps(self):
        mapHight = 256
        mapWith = mapHight * 2
        wordlMapList = Mapping().wordMapList()
        
        colorList = []
        
        for S in xrange(0, 2):
            for Cy in xrange(0, mapHight / 16):
                for Cx in xrange(0, (mapWith / 16) / 2):
                    for Ty in xrange(16):
                        for Tx in xrange(16):
                            colorList.append(wordlMapList[0][S][Cy][Cx][Ty][Tx][0])
                            
                            
        self.tile_size = 1
        
        self.map = pygame.Surface((mapWith * self.tile_size,
                                   mapHight * self.tile_size))
                            
        for y in xrange(0, mapWith):
            for x in xrange(0, mapHight):
                
                color = (colorList[y*x])
                image = pygame.Surface((1, 1))
                image.fill(color)
                self.map.blit(image, (y * self.tile_size,
                                      x * self.tile_size))
            
            
            
    
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def contains(self, point):
        dx = point[0] - self.center[0]
        dy = point[1] - self.center[1]
        return math.sqrt(dx*dx + dy*dy) < self.radius
    
class planetshade():
    def planetshade(self, screenWith ,screenHigth, planetRadius):
        
        
        self.shade = pygame.Surface((screenWith, screenHigth), flags=pygame.SRCALPHA)
        
        c = Circle([screenWith/2, screenHigth/2], planetRadius)
        
        for y in xrange(0, screenWith):
                for x in xrange(0, screenHigth):
                    
                    
                    image = pygame.Surface((1,1))
                    
                    if c.contains([y,x]) == False:
                        image.set_alpha(255)
                        image.fill((0, 0, 0))
                    elif c.contains([y,x]) == True:
                        image.set_alpha(0)
                        image.fill((255, 255, 255))
                       
                    self.shade.blit(image, (y, x)) 
        
        



        
#wordlMapList = Mapping().wordMapList()
#wordlMapList[map][mapChunkY][mapChukX][mapTileY][mapTileX][0 or 1]
#wordlMapList[0][0 - 15][0 - 15][0 - 15][0 - 15][0]

#MList[map][mapChunkY][mapChukX][mapTileY][mapTileX][0]
#spaceMapList = Mapping().spaceMapList()
#pprint.pprint(spaceMapList[0][3][2][15][2])

World = World()
planetshade = planetshade()

def main():
    
    pygame.init()
    pygame.display.set_caption("oYoieh-client")
    
    #800x600
    #1024x768
    #1280x800
    #1280x1024
    #1366x768
    #1920x1080
    screenWith = 800
    screenHigth = 600
    resolution = (screenWith, screenHigth)
    
    screen = pygame.display.set_mode(resolution)
    
    FPS = 60
    clock = pygame.time.Clock()
    
    World.Maps()
    

    clock=pygame.time.Clock()
    speed=250
    
    planetHight = 256
    planetWith = (planetHight*2)
    planetMid = (planetWith/2)
    planetRadius = (planetMid/2)
    planetH = (planetMid + planetRadius)
    planetV = (planetMid - planetRadius)
    
    print planetMid
    
    screenMidy = (screenHigth/2)-(planetHight/2)
    screenMid = screenWith / 2
    screenH = screenMid + planetRadius
    screenV = screenMid - planetRadius
    print screenH
    print screenV

    planetshadeScreen = planetshade.planetshade(screenWith ,screenHigth, planetRadius)
    
    
    x1= screenV
    x2= screenH
    move=0
    
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    
                    clock.tick(FPS)
                            
                    World.Maps()
                
                elif event.key == pygame.K_d:
                    
                    move+=1
                    
                elif event.key == pygame.K_a:
                    move-=1

            elif event.type == KEYUP:
                if event.key == pygame.K_d:
                    move=0
                    
                elif event.key == pygame.K_a:
                    move=0
                    
        x1+=move
        x2+=move
        
        if x1+planetV < screenV:
            screen.blit(World.map, (x2 == planetH+x1, screenMidy))
        
        #if x1+planetH < screenV:
        #    x1==0
        
        #if x2+planetV < screenV:
        #    screen.blit(World.map, (x1 == planetH+x2, screenMidy))
            
        #if x2+planetH < screenV:
        #    x2==0
        
            
        
        screen.blit(World.map, (x1, screenMidy))
        screen.blit(World.map, (x2, screenMidy))
        
        
            
            
        #screen.blit(World.map, (x1, (screenHigth/2)-(planetHight/2)))
        
        #screen.blit(planetshade.shade, (1, 1))
        
        pygame.display.flip()

            
if __name__ == "__main__":
    main()
    #cProfile.run("main()")
    pygame.quit()

