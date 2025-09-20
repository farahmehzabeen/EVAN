# 🔹 import pygame → Loads the Pygame library so we can use it.
# 🔹 import random → Will be used later if we want to randomize platform positions.
# 🔹 pygame.init() → Initializes Pygame’s built-in features like graphics, sound, and input handling.
import pygame
import random

# Initialize pygame
pygame.init()

# 🔹 WIDTH, HEIGHT = 600, 400 → Defines the game screen size (600 pixels wide, 400 pixels tall).
# 🔹 pygame.display.set_mode((WIDTH, HEIGHT)) → Creates the game window.
# 🔹 pygame.display.set_caption("Simple Platformer") → Sets the game title in the window bar.
# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")

# 🔹 Colors are defined using RGB values (Red, Green, Blue).
# 🔹 Example: (0, 0, 255) is blue because the blue value is 255 while red & green are 0.
# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 🔹 GRAVITY = 0.5 → Controls how fast the player falls.
# 🔹 PLAYER_JUMP = -10 → Controls how high the player jumps (negative means moving up).
# 🔹 PLAYER_SPEED = 5 → Controls how fast the player moves left & right.
# Game variables
GRAVITY = 0.5
PLAYER_JUMP = -10
PLAYER_SPEED = 5

# 🔹 class Player: → Defines a Player object that will be controlled by the user.
# 🔹 self.rect = pygame.Rect(x, y, 30, 30) → Creates a rectangle (30x30) for the player at position (x, y).
# 🔹 self.vel_y = 0 → This stores the vertical speed (used for jumping & gravity).
# 🔹 self.on_ground = False → Keeps track of whether the player is standing on a platform.
# Player class
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.vel_y = 0
        self.on_ground = False

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

    def jump(self):
        if self.on_ground:
            self.vel_y = PLAYER_JUMP
            self.on_ground = False

    def update(self, platforms):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Collision detection
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform) and self.vel_y > 0:
                self.rect.bottom = platform.top
                self.vel_y = 0
                self.on_ground = True

        # Prevent falling off screen
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.on_ground = True

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)


# Platform class
class Platform(pygame.Rect):
    def draw(self):
        pygame.draw.rect(screen, GREEN, self)


# Create platforms
platforms = [
    Platform(100, 300, 100, 10),
    Platform(250, 200, 100, 10),
    Platform(400, 250, 100, 10),
    Platform(150, 100, 100, 10),
]

# Create player
player = Player(WIDTH // 2, HEIGHT - 60)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.jump()

    player.move(keys)
    player.update(platforms)

    # Draw everything
    for platform in platforms:
        platform.draw()
    player.draw()

    pygame.display.update()
    clock.tick(30)

pygame.quit()
