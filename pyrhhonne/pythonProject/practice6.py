#users = {
#    "Оман": {
#        "телефон": "+971478745",
#        "емейл": "omanDolan12@gmail.com"
#    }
#}
from turtledemo.nim import SCREENWIDTH

#oman_skype = users["Оман"].get("skype", "Undefined")
#print(oman_skype)

#users = {"Jumanji", "Timothy", "IZH-412"}0

#user = "IZH-412"
#if user in users:
#    users.remove(user)

#print(users)

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Негровик")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.circle(screen, BLACK, (400, 480), 100, 5)
    pygame.draw.circle(screen, BLACK, (400, 320), 75, 5)
    pygame.draw.circle(screen, BLACK, (400, 190), 50, 5)

    pygame.draw.circle(screen, BLACK, (380, 180), 8, 0)
    pygame.draw.circle(screen, BLACK, (400, 180), 8, 0)

    pygame.draw.polygon(screen, ORANGE, [(400, 190), (450, 200), (400, 210)])

    pygame.draw.circle(screen, BLACK, (400, 280), 7, 0)
    pygame.draw.circle(screen, BLACK, (400, 320), 7, 0)
    pygame.draw.circle(screen, BLACK, (400, 360), 7, 0)

    pygame.draw.line(screen, BLACK, (200, 200), (330, 300), (5))
    pygame.draw.line(screen, BLACK, (600, 200), (470, 300), (5))



    pygame.display.flip()

pygame.quit()
