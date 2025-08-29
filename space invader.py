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
for i in range(number_of_enemies):
    enemy_image.append(pygame.image.load('alien_image-removebg-preview.png'))
    enemyX.append(random.randint(0,SCREEN_WIDTH-64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
bullet_image=pygame.image.load('bullet-removebg-preview.png')
bulletX=0
bulletY=PLAYER_START_Y
bulletX_change=0
bulletY_change=BULLET_SPEED_Y
bullet_state="ready"

score_value=0
font=pygame.font.Font('timesnewroman',64)
def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=font.render("GAMEOVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(player_image,(x,y))
def enemy(x,y,i):
    screen.blit(enemy_image[i],(x,y))
def bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_image,(x+16,y+10))
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
    return distance<COLLISION_DISTANCE
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(bg_image,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-5
            if event.key==pygame.K_RIGHT:
                playerX_change=+5
            if event.key==pygame.K_SPACE and bullet_state=="ready":
                bulletX=playerX
                bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerX_change=0
        