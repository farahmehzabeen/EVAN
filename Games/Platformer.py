# 🚀 Your Challenge: Create a simple platformer game in Python using Pygame! 🎮
import pygame
# I have no idea what I'm doing :DDDDD
import pygame

Timmy = 255, 255, 255

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)
    screen.fill(Timmy)

x = 0
y = 0

# Game Goals:
# 1️⃣ A player character (a square) can move left and right.
def update():
    pygame.display.update()

class Player:
    def __init__(self):
        self.x = 0
        self.keys = pygame.key.get_pressed()
        self.rect = pygame.Rect(x, y, 30, 30)
        self.y = 0
        self.centered = True

    def move(self, keys, x):
        self.keys = pygame.key.get_pressed()
        self.x = 0
        if keys[K_RIGHT]:
            x += 4
        else:
            x += 0

        if keys[K_LEFT]:
            x -= 4
        else:
            x += 0

    def jump(self, y):
        self.y = 0
        if pygame.key.get_pressed()[K_SPACE]:
            y += 20
        else:
           y -= 10


# # 2️⃣ The player falls due to gravity and lands on platforms.
#
# while True:
#     y /= 1
#
#
class platform:
   #  def Platform(self):
      #  pygame.draw.rect(x, y, 20, 10)

# 3️⃣ The player can jump when on a platform.

# for platform in platform:
   # if self.rect.top = self.rect.bottom:
        

# 4️⃣ The game stops the player from falling off the screen.





# Steps to Follow:
# 1️⃣ Create the Game Window:
# Set up Pygame and create a 600x400 window.
# 2️⃣ Make the Player:

# Use a rectangle to represent the player.
# The player should be able to move left and right.
# 3️⃣ Add Gravity & Jumping:
Gravity = 0.5
Height = 5
Speed = 5


# The player should fall down naturally (simulate gravity).
# The player should be able to jump when on a platform.
# 4️⃣ Add Platforms:




# Create a few platforms for the player to land on.
# The player should stop falling when standing on a platform.
# 5️⃣ Prevent Falling Off the Screen:

pygame.quit()
# If the player falls below the screen, reset their position.
# Hints & Ideas:
# 💡 Hint 1: Use pygame.Rect(x, y, width, height) to create rectangles for the player and platforms.
# 💡 Hint 2: To move the player, check pygame.key.get_pressed().
# 💡 Hint 3: To apply gravity, increase the player’s vertical speed (player_velocity_y).
# 💡 Hint 4: To stop the player when landing, check for collisions with platforms.


# 🕹️ Step 1: Set Up Pygame
# What to Do?
# Import pygame and initialize it.
# Create a screen with a width and height.
# Set a game title.
# Make a game loop so the window stays open.

# Hints
# Use pygame.init() to start Pygame.
# To create a window, use pygame.display.set_mode((WIDTH, HEIGHT)).
# The game loop runs until the player quits. It should use while running:.
# Quit when the player closes the window (pygame.QUIT).

# 🕹️ Step 2: Draw the Player
# What to Do?
# Create a player using a rectangle (pygame.Rect()).
# Draw the player inside the game loop.
# Make the player move left and right when arrow keys are pressed.
# Hints
# A rectangle can be drawn with pygame.draw.rect().
# To move left, decrease player.x. To move right, increase it.
# Use pygame.key.get_pressed() to check if a key is being held down.

# 🕹️ Step 3: Add Gravity and Jumping
# What to Do?
# Add a velocity (speed) for the player’s movement.
# Make the player fall down (gravity).
# Make the player jump when pressing SPACE.
# Hints
# Use a variable like player_velocity_y to control the falling speed.
# To apply gravity, increase player_velocity_y every frame.
# When jumping, set player_velocity_y to a negative number.
# Jumping should only happen when the player is on a platform (not mid-air).

# 🕹️ Step 4: Add Platforms
# What to Do?
# Create a list of platforms using pygame.Rect().
# Draw all platforms inside the game loop.
# Make sure the player lands on platforms instead of falling through.
# Hints
# Store platforms in a list: platforms = [pygame.Rect(x, y, width, height), ...].
# Use a for loop to draw all platforms.
# When the player touches a platform from above, stop them from falling (player.bottom = platform.top).

# 🕹️ Step 5: Prevent Falling Off the Screen
# What to Do?
# Make sure the player stays within the screen.
# If the player falls below the screen, reset them.
# Hints
# Check if player.bottom is greater than HEIGHT (screen bottom).
# If the player falls off, reset their position to the top.
