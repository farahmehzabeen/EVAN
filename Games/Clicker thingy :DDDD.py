import pygame
import math

# Color & circle parameters
Red = 255, 0, 0
Blue = 0, 0, 255
Center = 300, 200
Radius = 1

Counter = 0

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)

running = True
while running:
    screen.fill("white")

    # Draw circle
    pygame.draw.circle(screen, Red, Center, Radius)

    # Counter text
    text = font.render(f"Counter: {Counter}", True, "red", "white")
    textRect = text.get_rect()
    textRect.center = (400, 100)
    screen.blit(text, textRect)

    # Game logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            mousepos = pygame.mouse.get_pos()
            # Distance from mouse to center
            dx = mousepos[0] - Center[0]
            dy = mousepos[1] - Center[1]
            dist = math.hypot(dx, dy)  # √(dx^2 + dy^2)
            if dist <= Radius:
                Counter += 10
                Radius += 10

        elif Counter >= 20:
            screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
            pygame.display.set_caption("U WIN YAY :DDDDDDDDD")

            # Create a font object
            font = pygame.font.SysFont('Arial', 40)

            # Render the text
            text_surface = font.render('YAYAYYA YOU WINN I GUESS IDK', False, (50, 0, 50))  # Black text

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                screen.fill((255, 255, 255))  # Fill screen with white
                screen.blit(text_surface, (100, 250))  # Blit the text

                pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
