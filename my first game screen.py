import pygame
import sys
pygame.init()

screen_width=600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")
player_color = (255, 0, 0) 
player_size = 50
player_pos = [screen_width // 2, screen_height // 2]  # Center of the screen
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
