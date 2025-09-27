# Import necessary modules
from turtle import Turtle, Screen

# === SNAKE CONFIGURATION CONSTANTS ===
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions for 3 snake segments
MOVE_DISTANCE = 20                                   # Distance snake moves each step (matches segment size)
# Direction constants (in degrees for turtle heading)
UP = 90      # North direction
DOWN = 270   # South direction  
LEFT = 180   # West direction
RIGHT = 0    # East direction

class Snake:
    """
    Represents the snake player object with movement, growth, and collision detection.
    Manages a collection of turtle segments that move together as a cohesive snake,
    with the head leading and body segments following in a chain-like motion.
    """

    def __init__(self):
        """Initialize the snake with starting segments and set up the head reference."""
        self.segments = []      # List to store all snake segment turtle objects
        self.create_snake()     # Create initial 3-segment snake
        self.head = self.segments[0]  # Reference to first segment (the head)

    def create_snake(self):
        """
        Create the initial snake with 3 segments at predefined starting positions.
        Each segment is placed 20 pixels behind the previous one.
        """
        for position in STARTING_POSITIONS:  # Loop through starting positions
            self.add_segment(position)       # Create segment at each position

    def add_segment(self, position):
        """
        Create a new snake segment at the specified position.
        
        Args:
            position (tuple): (x, y) coordinates where the new segment should be placed
        """
        new_segment = Turtle("square")  # Create square-shaped turtle segment
        new_segment.color("white")      # Set segment color to white
        new_segment.penup()            # Don't draw lines when moving
        new_segment.goto(position)     # Move segment to specified position
        self.segments.append(new_segment)  # Add segment to snake's segment list

    def reset_snake(self):
        """
        Reset the snake to its initial state (used when game resets after collision).
        Moves old segments off-screen, clears the list, and creates a fresh snake.
        """
        # Move all existing segments far off-screen to hide them
        for seg in self.segments:
            seg.goto(1000, 1000)      # Move segment to coordinates outside visible area
        
        self.segments.clear()          # Remove all segments from the list
        self.create_snake()           # Create new snake with initial 3 segments
        self.head = self.segments[0]  # Reset head reference to new first segment

    def extend(self):
        """
        Add a new segment to the snake's tail (called when snake eats food).
        The new segment is placed at the current position of the last segment.
        """
        # Add segment at the position of the current tail segment
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Move the entire snake forward by one step.
        Each body segment moves to the position of the segment in front of it,
        while the head moves forward in its current direction.
        """
        # Move body segments: start from tail and work backwards
        for seg_num in range(len(self.segments) - 1, 0, -1):  # From last to second segment
            # Get position of segment in front
            new_x = self.segments[seg_num - 1].xcor()  # X coordinate of previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Y coordinate of previous segment
            # Move current segment to that position
            self.segments[seg_num].goto(new_x, new_y)
        
        # Move head forward in its current direction
        self.head.forward(MOVE_DISTANCE)

    # === DIRECTION CONTROL METHODS ===
    # These methods prevent the snake from reversing into itself
    
    def up(self):
        """Change snake direction to up, unless it's currently moving down."""
        if self.head.heading() != DOWN:  # Prevent reversing into body
            self.head.setheading(UP)

    def down(self):
        """Change snake direction to down, unless it's currently moving up."""
        if self.head.heading() != UP:    # Prevent reversing into body
            self.head.setheading(DOWN)

    def left(self):
        """Change snake direction to left, unless it's currently moving right."""
        if self.head.heading() != RIGHT: # Prevent reversing into body
            self.head.setheading(LEFT)

    def right(self):
        """Change snake direction to right, unless it's currently moving left."""
        if self.head.heading() != LEFT:  # Prevent reversing into body
            self.head.setheading(RIGHT)
