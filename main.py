# Import necessary modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# === GAME SETUP ===
# Create and configure the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set screen dimensions to 600x600 pixels
screen.bgcolor("black")              # Set background color to black
screen.title("Snake Game")           # Set window title
screen.tracer(0)                     # Turn off animation for smoother gameplay

# Initialize game objects
snake = Snake()           # Create the snake object
food = Food()            # Create food object that snake will eat
scoreboard = Scoreboard() # Create scoreboard to track score and high score

# === CONTROLS SETUP ===
# Set up keyboard controls for snake movement
screen.listen()                    # Enable screen to listen for key presses
screen.onkey(snake.up, "Up")       # Bind Up arrow key to move snake up
screen.onkey(snake.down, "Down")   # Bind Down arrow key to move snake down
screen.onkey(snake.left, "Left")   # Bind Left arrow key to move snake left
screen.onkey(snake.right, "Right") # Bind Right arrow key to move snake right

# === MAIN GAME LOOP ===
game_on = True  # Game state flag
while game_on:
    screen.update()    # Refresh the screen to show updates
    time.sleep(0.09)   # Control game speed (pause for 0.09 seconds each frame)
    snake.move()       # Move the snake forward in its current direction

    # === FOOD COLLISION DETECTION ===
    # Check if snake's head collides with food
    if snake.head.distance(food) < 15:  # If snake head is within 15 units of food
        food.refresh()               # Generate new food at random location
        snake.extend()               # Add new segment to snake (make it longer)
        scoreboard.increase_score()  # Increase and display updated score

    # === WALL COLLISION DETECTION ===
    # Check if snake hits any of the four walls (boundaries at +-280)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # Original game over logic (commented out for reset functionality)
        # game_on = False
        # scoreboard.game_over()
        
        # Reset game instead of ending it
        scoreboard.reset()      # Reset score and update high score if needed
        snake.reset_snake()     # Reset snake to starting position and length
        
    # === TAIL COLLISION DETECTION ===
    # Check if snake's head collides with its own body
    for segment in snake.segments[1:]:  # Check all segments except the head (index 0)
        if snake.head.distance(segment) < 10:  # If head touches any body segment
            # Original game over logic (commented out for reset functionality)
            # game_on = False
            # scoreboard.game_over()
            
            # Reset game instead of ending it
            scoreboard.reset()      # Reset score and update high score if needed
            snake.reset_snake()     # Reset snake to starting position and length

# Keep the screen open until clicked
screen.exitonclick()
