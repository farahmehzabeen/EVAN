import pygame
import sys

pygame.init()

Width, Height = 400, 300
screen = pygame.display.set_mode((Width, Height), pygame.RESIZABLE)
pygame.display.set_caption("TD game")

White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)
Some_Random_Color = (52, 246, 112)

Clock_Thingy = pygame.time.Clock()

time_to_defend = True


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = Blue

    def draw(self, screen):
        pygame.draw.polygon(screen, Blue, [[100, 200], [50, 30], [70, 80]], 6)


enemy = Enemy(0, 0)

while time_to_defend:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            time_to_defend = False

    screen.fill(Black)
    enemy.draw(screen)
    pygame.display.flip()

    Clock_Thingy.tick(60)

pygame.quit()
sys.exit()
