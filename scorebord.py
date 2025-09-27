# Import necessary modules
from turtle import Turtle

# === DISPLAY CONSTANTS ===
ALIGNMENT = "center"                    # Text alignment for scoreboard display
FONT = ("Courier", 24, "normal")       # Font style, size, and weight for text

class Scoreboard(Turtle):
    """
    Manages the game's scoreboard with persistent high score tracking.
    Inherits from Turtle class to display text on screen and handles file I/O
    for saving/loading high scores between game sessions.
    """

    def __init__(self):
        """Initialize scoreboard with current score, persistent high score, and display setup."""
        super().__init__()  # Initialize parent Turtle class
        
        # Score tracking variables
        self.score = 0                          # Current game score (starts at 0)
        self.high_score = self.fetch_high_score()  # Load high score from file
        
        # Configure turtle for text display
        self.color("white")    # Set text color to white (visible on black background)
        self.penup()          # Don't draw lines when moving
        self.goto(0, 260)     # Position scoreboard at top center of screen
        self.hideturtle()     # Hide the turtle cursor/shape
        
        # Display initial scoreboard
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Refresh the scoreboard display with current score and high score.
        Clears previous text and writes updated information.
        """
        self.clear()  # Remove previous text from screen
        # Display both current score and high score on one line
        self.write(f"Score: {self.score} High Score = {self.high_score}", 
                  align=ALIGNMENT, font=FONT)

    def reset(self):
        """
        Reset the game while preserving high score achievements.
        Updates high score if current score beats it, then resets current score.
        """
        # Check if current score is a new high score
        if self.score > self.high_score:
            self.high_score = self.score      # Update high score in memory
            self.update_high_score()          # Save new high score to file
        
        self.score = 0               # Reset current score to 0
        self.update_scoreboard()     # Refresh display with reset values

    # === LEGACY GAME OVER METHOD (COMMENTED OUT) ===
    # def game_over(self):
    #     """Display game over message in center of screen (no longer used)."""
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increment the current score by 1 and update display.
        Called when snake successfully eats food.
        """
        self.score += 1          # Add 1 to current score
        self.update_scoreboard() # Refresh display with new score

    def fetch_high_score(self):
        """
        Load the high score from persistent storage (data.txt file).
        
        Returns:
            int: The high score value from the file
        """
        with open("data.txt") as file:     # Open file in read mode (default)
            h_score = int(file.read())     # Read file content and convert to integer
            return h_score                 # Return the high score value

    def update_high_score(self):
        """
        Save the current high score to persistent storage (data.txt file).
        Overwrites the existing file content with the new high score.
        """
        with open("data.txt", mode="w") as file:  # Open file in write mode
            file.write(f"{self.high_score}")     # Write high score as string to file
