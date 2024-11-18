# simulation/agent.py
class Agent:
    def __init__(self, x, y, speed, environment):
        """Initialize the agent with position, speed, and environment link."""
        self.x = x
        self.y = y
        self.speed = speed
        self.environment = environment

    def move(self, direction):
        """Move the agent based on the direction input ('up', 'down', 'left', 'right')."""
        if direction == "up":
            self.y -= self.speed
        elif direction == "down":
            self.y += self.speed
        elif direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed

        # Wrap around if the agent moves out of bounds
        self.x, self.y = self.environment.limit_position(self.x, self.y)
