import pygame
import random
import math

SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_Y=40
ENEMY_SPEED_X=4
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27

pygame.init()

screen=pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

bg_image=pygame.image.load('animated-space.jpg')
pygame.display.set_caption("space invader")
icon=pygame.image.load('space-icon-png-removebg-preview.png')
pygame.display.set_icon(icon)

player_image=pygame.image.load('rocket.png')
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change=0

enemy_image=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
number_of_enemies=6