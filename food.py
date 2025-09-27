# Import necessary modules
import random
from turtle import Turtle

class Food(Turtle):
    """
    Represents the food that the snake eats to grow and increase score.
    Inherits from Turtle class to create a visual food object that appears
    randomly on the screen when eaten or when the game starts.
    """

    def __init__(self):
        """Initialize the food object with its appearance and place it randomly on screen."""
        super().__init__()  # Initialize parent Turtle class
        
        # Configure food appearance
        self.shape("circle")    # Set food shape to circle
        self.penup()           # Don't draw lines when moving
        
        # Make food smaller than default turtle size
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Scale to 50% of original size
        
        self.color("blue")     # Set food color to blue for visibility
        self.speed("fastest")  # Set movement speed to fastest (for instant positioning)
        
        # Place food at initial random location
        self.refresh()

    def refresh(self):
        """
        Move the food to a new random location on the screen.
        Called when snake eats the food or when game resets.
        Uses screen boundaries of ±280 pixels to keep food within playable area.
        """
        # Generate random coordinates within screen boundaries
        random_x = random.randint(-280, 280)  # Random X coordinate (-280 to 280)
        random_y = random.randint(-280, 280)  # Random Y coordinate (-280 to 280)
        
        # Move food to the new random position instantly
        self.goto(random_x, random_y)
