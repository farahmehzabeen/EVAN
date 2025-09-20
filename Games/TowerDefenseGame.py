import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Grid settings
GRID_SIZE = 50
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE


def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = GRID_SIZE
        self.color = RED
        self.speed = 2
        self.health = 3  # Enemy takes 3 hits to be defeated

    def move(self):
        self.x += self.speed  # Move right by 'speed' pixels per frame

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, rect)

    def get_center(self):
        return self.x + self.size // 2, self.y + self.size // 2


class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = GRID_SIZE * 3
        self.color = GREEN
        self.shoot_delay = 30  # Shoot every 30 frames
        self.shoot_timer = 0

    def in_range(self, enemy):
        tower_center = (self.x + GRID_SIZE // 2, self.y + GRID_SIZE // 2)
        enemy_center = enemy.get_center()
        distance = math.sqrt((tower_center[0] - enemy_center[0]) ** 2 + (tower_center[1] - enemy_center[1]) ** 2)
        return distance <= self.range

    def shoot(self, bullets, enemy):
        if self.shoot_timer == 0:
            bullets.append(Bullet(self.x + GRID_SIZE // 2, self.y + GRID_SIZE // 2, enemy))
            self.shoot_timer = self.shoot_delay  # Reset timer

    def update(self):
        if self.shoot_timer > 0:
            self.shoot_timer -= 1  # Decrease timer every frame

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, self.color, rect)

        # Draw range
        pygame.draw.circle(screen, (0, 255, 0, 50), (self.x + GRID_SIZE // 2, self.y + GRID_SIZE // 2),
                           self.range, 1)


class Bullet:
    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.target = target
        self.speed = 5
        self.color = BLUE
        self.radius = 5
        self.active = True

    def move(self):
        target_x, target_y = self.target.get_center()
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:
            dx, dy = dx / distance, dy / distance
            self.x += dx * self.speed
            self.y += dy * self.speed

        # Collision check
        if distance < 10:  # If the bullet is close enough, hit the enemy
            self.target.health -= 1
            if self.target.health <= 0:
                enemies.remove(self.target)  # Remove enemy if health is 0
            self.active = False  # Remove bullet

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


# Game objects
enemy = Enemy(0, HEIGHT // 2 - GRID_SIZE // 2)
tower = Tower(WIDTH // 2 - GRID_SIZE // 2, HEIGHT // 2 - GRID_SIZE // 2)
bullets = []
enemies = [enemy]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_grid()

    # Enemy logic
    for enemy in enemies[:]:  # Iterate over a copy in case an enemy is removed
        enemy.move()
        enemy.draw(screen)

    # Tower logic
    tower.update()
    for enemy in enemies:
        if tower.in_range(enemy):
            print("Enemy in range!")
            tower.shoot(bullets, enemy)

    tower.draw(screen)

    # Bullet logic
    for bullet in bullets[:]:  # Iterate over a copy since bullets are removed mid-loop
        bullet.move()
        if bullet.active:
            bullet.draw(screen)
        else:
            bullets.remove(bullet)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

