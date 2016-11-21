#template

import pygame
from pygame import *
from pygame.sprite import *
from random import *

pygame.init();


#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Main_Paddle(Sprite): # define Gold as Sprite (collission detection, rectangle), define its methods by def gold.move
    def __init__(self):
        Sprite.__init__(self)
        self.width = 70
        self.height = 20
        self.image = Sprite.surface([self.width,self.height]) 


        # take all Sprite code, and make brand new Sprite for me, afterlines create non-generic attributes
        self.image = image.load("gold.bmp").convert_alpha() # picture #convert_alpha png transparency recognition 
        self.rect = self.image.get_rect() # rectangle

    # move gold to a new random location
    def move(self): # nothing to do with Sprites
        randX = randint(0, 600) # function from random library 
        randY = randint(0, 400)
        self.rect.center = (randX,randY) 




gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("Those Darn Blocks")

pygame.display.update()		#only updates portion specified

# object measurements
brick_width = 70
brick_height = 20
paddle_width = 70
paddle_height = 15
ball_diameter = 12
ball_radius = ball_diameter / 2

main_paddle = screen

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		print(event)

def dra

