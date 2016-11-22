#template

import pygame
from pygame import *
from pygame.sprite import *
from random import *


#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

block_width = 60
block_height = 25

class Block(Sprite):
	def __init__(self, color = red, width = 80, height = 30):
		#self.blockwidth = block_width
		#self.blockheight = block_height
		Sprite.__init__(self)
		#self.image = pygame.Surface((self.block_width,self.block_height))
		self.image = pygame.Surface((width,height))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		#self.name = Block
	def position(self,x,y):
		self.rect.x = x
		self.rect.y = y

class Ball(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.moving = False
		self.image = pygame.Surface((12,12))
		self.image.fill(white)
		self.rect = self.image.get_rect()


if (__name__ == '__main__'):
	pygame.init()

	gameDisplay = pygame.display.set_mode((820,600)) #initialize with a tuple
	#lets add a title, aka "caption"
	pygame.display.set_caption("Those Darn Blocks")
	gameDisplay.fill(white)
	clock = pygame.time.Clock()
	frames_per_second = 60

	# now start initializing things in the window

	# 3 ROWS OF BLOCKS ARE GOING TO BE CREATED

	block_group = pygame.sprite.Group()
	one_block = Block()
	one_block.position(10,10)
	two_block = Block(blue)
	two_block.position(10,50)
	three_block = Block(green)
	three_block.position(10,90)
	block_group.add(one_block,two_block, three_block)

	block_count = 9
	counting = 0
	for column in range(0,block_count):
		counting += 90
		block1 = Block()
		block1.position(10+counting,10)
		block2 = Block(blue)
		block2.position(10+counting,50)
		block3 = Block(green)
		block3.position(10+counting,90)
		block_group.add(block1,block2,block3)

	# now going to draw the block group sprites in the window
	block_group.draw(gameDisplay) # adding sprites to window surface

	running = True

	while(running):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		clock.tick(frames_per_second)
		pygame.display.update()

	pygame.quit()	


	#def update(self):


class Paddle(Sprite):
	def __init__(self):
		self.blockwidth = block_width
		self.blockheight = block_height
		Sprite.__init__(self)
		#self.image = image.load("paddle.png").convert_alpha() # getting paddle image
		self.image = pygame.Surface((self.blockwidth,self.blockheight))
		self.rect = self.image.get_rect() 
    #def update(self):
    #	self.rect.center = mouse.get_pos()

# block = Block()
# ball = Ball()
# paddle = Paddle()

# sprites = RenderPlain(block, ball, paddle)



# def main():
# 	pygame.init();

# 	gameDisplay = pygame.display.set_mode((800,600))

# 	clock = pygame.time.Clock() # calling clock object

# 	running = True

# 	while running:
# 		clock.tick(65)
# 		for event in pygame.event.get():
# 			if event.type == QUIT:
# 				pygame.quit()
# 				running = False
# 		screen.fill((0,0,0)) 
# 		pygame.display.flip() # update to different screen

# 	pygame.quit() # prevents error message in terminal when game shuts down


#pygame.display.update()		#only updates portion specified

# # object measurements
# brick_width = 70
# brick_height = 20
# paddle_width = 70
# paddle_height = 15
# ball_diameter = 12
# ball_radius = ball_diameter / 2

# main_paddle = screen



