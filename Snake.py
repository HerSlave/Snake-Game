import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Define the snake class
class Snake:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = "right"
    
    def move(self):
        x, y = self.body[0]
        if self.direction == "right":
            x += 10
        elif self.direction == "left":
            x -= 10
        elif self.direction == "up":
            y -= 10
        elif self.direction == "down":
            y += 10
        self.body = [(x, y)] + self.body[:-1]
    
    def grow(self):
        x, y = self.body[0]
        if self.direction == "right":
            x += 10
        elif self.direction == "left":
            x -= 10
        elif self.direction == "up":
            y -= 10
        elif self.direction == "down":
            y += 10
        self.body = [(x, y)] + self.body
    
    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(window, green, (x, y, 10, 10))

# Define the food class
class Food:
    def __init__(self):
        self.x = random.randint(0, window_width-10)
        self.y = random.randint(0, window_height-10)
    
    def draw(self):
        pygame.draw.rect(window, red, (self.x, self.y, 10, 10))

# Create the snake and food objects
snake = Snake(400, 300)
food = Food()

# Main game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != "left":
                snake.direction = "right"
            elif event.key == pygame.K_LEFT and snake.direction != "right":
                snake.direction = "left"
            elif event.key == pygame.K_UP and snake.direction != "down":
                snake.direction = "up"
            elif event.key == pygame.K_DOWN and snake.direction != "up":
                snake.direction = "down"
    
    # Move the snake
    snake.move()
    
    # Check for collision with the food
    if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
        snake.grow()
        food = Food()
    
    # Check for collision with the walls
    if snake.body[0][0] < 0 or snake.body[0][0] >= window_width or \
        snake.body[0][1] < 0 or snake.body[0][1] >= window_height:
        game_over = True
    
    # Check for collision with the snake's body
    for i in range(1, len(snake.body)):
        if snake.body[0] == snake.body[i]:
            game_over 
