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
ball_speed = 4

class Paddle(Sprite):
	def __init__(self, color = red, width = 80, height = 30):
		Sprite.__init__(self)
		#self.image = image.load("paddle.png").convert_alpha() # getting paddle image
		self.image = pygame.Surface((width,height))
		self.image.fill(color)
		self.rect = self.image.get_rect() 
		self.screenheight = pygame.display.get_surface().get_height
		self.screenwidth = pygame.display.get_surface().get_width
		self.rect.topleft = (0,self.screenheight-self.height)
   # Update the player)
	def update(self):
		self.rect.center = mouse.get_pos()
		self.rect.left = pos[0]
		#if self.rect.left > self.scree
    #def update(self, mouse_position):

    #	self.rect.center = mouse.get_pos()

class Block(Sprite):
	def __init__(self, color = red, width = 80, height = 30): # default block color is red
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
	#def update(self):
		#if self.rect.collidepoint


	# def detect_collision(self, sprite1, sprite2):
	# 	collide = pygame.sprite.collide_rect(sprite1, sprite2)
	# 	if collide == True:
	# 		sprite2

class Ball(Sprite):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.change_x = 0 # look up what this does
		self.change_y = 0
		self.size = 10
		self.color = black
	def movement(self):
		self.x += self.change_x
		self.y += self.change_y
	#def update(self):
		old_x = self.rect.x
		new_x = old_x + self.change_x
		self.rect.x = new_x
	def update(self, mousex, blocks, paddle, *args):
        if self.moving == False:
            self.rect.centerx = mousex

        else:
            self.rect.y += self.vectory

            hitGroup = pygame.sprite.Group(paddle, blocks)

            spriteHitList = pygame.sprite.spritecollide(self, hitGroup, False)
            if len(spriteHitList) > 0:
                for sprite in spriteHitList:
                    if sprite.name == BLOCK:
                        sprite.kill()
                        self.score += 1
                self.vectory *= -1
                self.rect.y += self.vectory
            
            self.rect.x += self.vectorx
            
            blockHitList = pygame.sprite.spritecollide(self, blocks, True)
                
            if len(blockHitList) > 0:
                self.vectorx *= -1
                self.score += 1


	def draw(self,screen):
		pygame.draw.circle(screen,self.color,[self.x,self.y],self.size)

class Boundaries(Sprite):
	def __init__(self,x,y,width,height):
		Sprite.__init__(self)
		self.image = pygame.Surface((width,height))
		self.image.fill(black)
		self.rect = self.image.get_rect()
	def position(self,x,y):
		self.rect.y = y
		self.rect.x = x 

# class Ball(Sprite):
# 	speed = 10
# 	x = 0
# 	y = 180
# 	direction = 150
# 	width = 15
# 	height = 15
# 	def __init__(self):
# 		Sprite.__init__(self)
# 		#self.moving = False
# 		self.image = pygame.Surface([self.width,self.height])
# 		self.image.fill(white)
# 		self.rect = self.image.get_rect()
# 	def react(self):
# 		self.x += self.speed # change position of ball's x and y coordinates based on speed and direction
# 		self.y += self.speed
# 		if self.y <= 0:
# 			self.speed


if (__name__ == '__main__'):
	pygame.init()

	gameDisplay = pygame.display.set_mode((820,600)) #initialize with a tuple
	#lets add a title, aka "caption"
	pygame.display.set_caption("Those Darn Blocks")
	gameDisplay.fill(white)
	clock = pygame.time.Clock()
	frames_per_second = 60

	# now start initializing things in the window

	# 3 ROWS OF BLOCKS ARE GOING TO BE CREATED - block placement

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


	the_ball = Ball() #ball class initiated
	the_ball.x = 410 # starting x position of ball
	the_ball.y = 500 # starting y position of ball
	the_ball.change_x = 3 
	the_ball.change_y = 2
	the_ball.movement()
	the_ball.draw(gameDisplay)

	#going to make the boundaries now
	bound_group = pygame.sprite.Group()
	bound_top = Boundaries(0,0,820,5) #(x,y,width,height)
	bound_bottom = Boundaries(500,100,820,5) # (find how to make borders also on side)
	bound_group.add(bound_top,bound_bottom)

	bound_group.draw(gameDisplay)

	main_player = Paddle()
	main_player.draw(gameDisplay)




	running = True

	while(running):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		clock.tick(frames_per_second)
		pygame.display.update()

	pygame.quit()	


	#def update(self):



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


import pygame
#from pygame import *
from pygame.sprite import *
from random import *


#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Borders(Sprite):
	def __init__(self,x,y,height,width,color):
		Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

#use bitmap for images

class Player(Sprite):
	change_x = 10
	change_y = 10
	speed = 2
	def __init__(self,x,y):
		Sprite.__init__(self)
		self.image = pygame.Surface([30,30])
		self.image.fill(black)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	def change_speed(self,x,y):
		self.change_x += x
		self.change_y += y 
	def movement(self,borders):
		self.rect.x += self.change_x # update position based on change (move left and right)
		borders_hit = Sprite.spritecollide(self,borders,False)
		for border in borders_hit:
			if self.change_x > 0: # if moved right, place right side to hit object's left
				self.rect.right = border.rect.left
			else:
				self.rect.left = border.rect.right # if moved left, place left side to hit object's right
		self.rect.y += self.change_y
		borders_hit = Sprite.spritecollide(self,borders,False)
		for border in borders_hit:
			if self.change_y > 0:
				self.rect.bottom = border.rect.top
			else:
				self.rect.top = border.rect.bottom

class Maze_Base():
	borders = None
	enemies = None

	def __init__(self):
		self.borders = Sprite.Group()
		self.enemies = Sprite.Group()







