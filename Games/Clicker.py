import pygame
import math


class CircleButton:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def is_clicked(self, mouse_pos):
        dx = mouse_pos[0] - self.center[0]
        dy = mouse_pos[1] - self.center[1]
        distance = math.hypot(dx, dy)
        return distance <= self.radius


def main():
    # Setup
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 32)

    # Colors
    red = (255, 0, 0)
    white = (255, 255, 255)

    # Game state
    counter = 0
    circle = CircleButton(center=(300, 200), radius=70, color=red)
    running = True

    while running:
        screen.fill(white)

        # Draw circle
        circle.draw(screen)

        # Draw counter text
        text = font.render(f"Counter: {counter}", True, red, white)
        text_rect = text.get_rect(center=(400, 100))
        screen.blit(text, text_rect)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if circle.is_clicked(pygame.mouse.get_pos()):
                    counter += 1

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
