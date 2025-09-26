
import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Кублоид")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    for x in range(1,800,50):
        for y in range(1, 800, 50):
            pygame.draw.rect(screen, RED, (x, y, 40, 40), 2)

font = pygame.font.SysFont('Arial', 30)
text_surface = font.render('1', True, (255, 255, 255))



    pygame.display.update()
quit()