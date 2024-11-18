# simulation/environment.py
class Environment:
    def __init__(self, width, height):
        """Initialize the environment dimensions."""
        self.width = width
        self.height = height

    def limit_position(self, x, y):
        """Ensure the agent’s position wraps around the environment boundaries."""
        x = x % self.width  # Wrap around horizontally
        y = y % self.height  # Wrap around vertically
        return x, y
