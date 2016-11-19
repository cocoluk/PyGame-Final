#template

import pygame
pygame.init();

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("Those Darn Blocks")

pygame.display.update()		#only updates portion specified


gameExit = False
while not gameExit:
	for event in pygame.event.get():
		print(event)