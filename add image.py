import pygame
pygame.init()
SCREEN_HEIGHT,SCREEN_WIDTH=(500,500)
display_surface=pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
pygame.display.set_caption('Adding image and background image')
background_image=pygame.transform.scale(pygame.image.load('backgroud.png').convert(),(SCREEN_HEIGHT,SCREEN_WIDTH))
