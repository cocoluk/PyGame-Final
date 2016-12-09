#template

import pygame
import sys
from pygame import *
from pygame.sprite import *
from random import *


#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

background = white
block_space = 2 # space in between blocks
block_width = 62
block_height = 25
layout_width = 20 # block organization dimensions
layout_height = 10
paddle_width = 65
paddle_height = 5
block = 'block'
ball = 'ball'
paddle = 'paddle'
ball_speed = 8.5

screen_width = 640
screen_height = 480


class Block(Sprite):
	def __init__(self):
		self.block_width = block_width
		self.block_height = block_height
		Sprite.__init__(self)
		self.image = pygame.Surface((self.block_width, self.block_height))
		self.image.fill(red)
		self.rect = self.image.get_rect()
		self.name = block

class Paddle(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		#self.image = image.load("paddle.png").convert_alpha() # getting paddle image
		self.image = pygame.Surface((paddle_width,paddle_height))
		self.image.fill(black)
		self.rect = self.image.get_rect() 
		self.name = paddle
   # Update the player)
	def update(self,mouse_x,*args): # only deals with x postion because only suppose to be moving horizontally
		if self.rect.x >= 0:
			if self.rect.right <= screen_width: # paddle within boundaries
				self.rect.centerx = mouse_x # set paddle center coordinates to mouse's current coordinates
		if self.rect.x < 0: # if paddle gets off screen
			self.rect.x = 0 # move back on screen
		elif self.rect.right > screen_width: # paddle's right side further than screen width (gets off screen)
			self.rect.right = screen_width # move back on screen
			#ultimately creating boundaries for paddle to move within

class Ball(Sprite):
	def __init__(self,display_surface):
		Sprite.__init__(self)
		self.name = ball
		self.moving = False
		self.image = pygame.Surface((10,10))
		self.image.fill(red)
		self.rect = self.image.get_rect()
		self.vectorx = ball_speed # vectors to represent speed and angle move right
		self.vectory = ball_speed * -1 # move left
		self.score = 0
	def update(self,mouse_x,blocks,paddle,*args): # need *args to pass arbitrary amount of arguments
		if self.moving == False: # if ball is not moving
			self.rect.centerx = mouse_x # position of ball follows mouse
		else:
			self.rect.y = self.rect.y + self.vectory # ball y position - 10
			collisions = pygame.sprite.Group(paddle,blocks) # list of things that ball can collide with, contains our paddle and blocks
			hit_sprites = pygame.sprite.spritecollide(self,collisions,False) # required so paddle still exists after ball hits paddle for the first time
			if len(hit_sprites) > 0: # if the ball hits something
				for sprite in hit_sprites: # for the sprites in our list containing the blocks and paddle
					if sprite.name == block: # if the ball hit a block
						#pygame.mixer.music.load('hit.wav')
						#pygame.mixer.music.play(-1,0)
						sprite.kill() # get rid of the block that was just hit
						self.score = self.score + 1 # increase score by 1
				self.vectory = self.vectory * -1 # ball speed * -1 = -10 * -1 = 10 new position
				self.rect.y += self.vectory
				#print("5")
			self.rect.x += self.vectorx
			hit_blocks = pygame.sprite.spritecollide(self,blocks,True) # see if sprite block collided with blocks group, True removes block from group
			if len(hit_blocks) > 0: # if the list of colliding sprites is greater than 0
				self.vectorx *= -1  # return ball at ball speed, simulate it being bounced backwards towards the paddle
				self.score += 1
				#print("1")
			elif self.rect.right > screen_width: #if ball's right side is off the screen
				self.vectorx *= -1 #
				self.rect.right = screen_width #bring the ball's right side back to the screen width dimensions so it stays within game window
				#print("2")
			elif self.rect.left < 0: # if the left side of the ball is off the screen
				self.vectorx *= -1 # bring back so ball moves towards right (+ goes right, - goes left)
				self.rect.left = 0 # position the left side of the ball 
				#print("3")
			elif self.rect.top < 0: 
				self.vectory *= -1
				self.rect.top = 0
				#print("4")
			elif self.rect.top > screen_height-5:
				print ("So close, play again!")
				pygame.display.quit()
				pygame.quit()
				sys.exit()

class Score(object):
	def __init__(self):
		self.score = 0
		self.font = pygame.font.Font(None,25)
		self.render = self.font.render('Score = ' + str(self.score), True, blue, white) #score, text color, background color
		self.rect = self.render.get_rect()
		self.rect.x = 0
		self.rect.bottom = screen_height

class Game(object):
	def __init__(self):
		pygame.init()
		pygame.mixer.music.load('music.wav') # has to be a .wav file 
		pygame.mixer.music.play(-1,0)
		self.display_surface, self.display_rect = self.create_screen()
		self.mouse_x = 0 # starting mouse position
		self.blocks = self.create_blocks()
		self.paddle = self.create_paddle()
		self.ball = self.create_ball()
		self.score = Score()
		self.all_sprites = pygame.sprite.Group(self.blocks,self.paddle,self.ball)
	def create_screen(self):
		pygame.display.set_caption('Destroy Those Blocks!')
		display_surface = pygame.display.set_mode((screen_width,screen_height))
		display_rect = display_surface.get_rect()
		display_surface.fill(background)
		#font = pygame.font.Font(None,36)
		#text = font.render("Press Space to Play",1,(10,10,10))
		#text_position = text.get_rect()
		#text_position.centerx = 20
		#text_position.bottom = screen_height
		display_surface.convert()
		return display_surface, display_rect
	def update_score_instructions(self): #from score class
		self.score.score = self.ball.score # get the score from the score defined in ball class
		self.score.render = self.score.font.render('Press the Space Bar to Start, Control with Mouse                             Score = ' + str(self.score.score), True, blue, white)
		self.score.rect = self.score.render.get_rect()
		self.score.rect.x = 0
		self.score.rect.bottom = screen_height
	def create_blocks(self):
		blocks_group = pygame.sprite.Group()
		for y in range(layout_height): # assembling blocks within the layout specified above
			for x in range(layout_width):
				block = Block() # create blocks using Block class
				block.rect.x = x * (block_width+block_space) # block x position equals x of layout width times set block width plus block space
				block.rect.y = y * (block_height+block_space) # block y position equals y of layout height times block height plus block space
				block.color = self.block_color(block,y,x)
				block.image.fill(block.color)
				blocks_group.add(block)
		return blocks_group
	def block_color(self,block,row,column):
		if row == 0:
			return green
		if row == 1:
			return yellow
		if row == 2:
			return red
		if row == 3:
			return blue
		if row == 4:
			return green
		if row == 5:
			return yellow
		if row == 6:
			return red
		if row == 7:
			return blue
		if row == 8:
			return green
		if row == 9:
			return yellow
		if row == 10:
			return red
		else:
			return blue
	def create_paddle(self):
		paddle = Paddle()
		paddle.rect.centerx = self.display_rect.centerx
		paddle.rect.bottom = self.display_rect.bottom
		return paddle
	def create_ball(self):
		ball = Ball(self.display_surface)
		ball.rect.centerx = self.paddle.rect.centerx
		ball.rect.bottom = self.paddle.rect.top # place bottom of ball on top of paddle for starting position
		return ball
	def event_detection(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEMOTION:
				self.mouse_x = event.pos[0]
			elif event.type == KEYUP:
				if event.key == K_SPACE:
					self.ball.moving = True
	def run_game(self):
		while True:
			self.display_surface.fill(background)
			self.update_score_instructions()
			self.display_surface.blit(self.score.render,self.score.rect)
			self.all_sprites.update(self.mouse_x,self.blocks,self.paddle)
			self.all_sprites.draw(self.display_surface)
			pygame.display.update()
			self.event_detection()

if __name__ == '__main__':
	play_game = Game()
	play_game.run_game()






