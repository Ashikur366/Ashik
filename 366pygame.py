# simulation/run.py
# simulation/run.py
import pygame
from agent import Agent
from environment import Environment

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agent Simulation")

# Create environment and agent
environment = Environment(WIDTH, HEIGHT)
agent = Agent(x=WIDTH // 2, y=HEIGHT // 2, speed=5, environment=environment)

# Colors
BACKGROUND_COLOR = (139, 69, 19)  # Brown background color
AGENT_COLOR = (210, 180, 140)     # Light brown agent color
TEXT_COLOR = (210, 180, 140)      # Light brown text color
font = pygame.font.SysFont('Arial', 24)  # Simple Arial font for a minimalistic look

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        agent.move("up")
    if keys[pygame.K_DOWN]:
        agent.move("down")
    if keys[pygame.K_LEFT]:
        agent.move("left")
    if keys[pygame.K_RIGHT]:
        agent.move("right")

    # Fill the screen with the brown background color
    screen.fill(BACKGROUND_COLOR)

    # Draw agent with light brown color
    pygame.draw.circle(screen, AGENT_COLOR, (int(agent.x), int(agent.y)), 10)

    # Display position text in light brown
    position_text = font.render(f"Position: ({int(agent.x)}, {int(agent.y)})", True, TEXT_COLOR)
    screen.blit(position_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
