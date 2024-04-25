import pygame
import sys


WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
GRAY = (230, 230, 230)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TEAL = (0, 255, 255)
PURPLE = (255, 0, 255)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(GRAY)

    pygame.draw.line(window, BLUE, (20, 20), (60, 20), 4)
    pygame.draw.line(window, BLUE, (20, 20), (20, 60), 4)
    pygame.draw.line(window, BLUE, (20, 60), (60, 60), 4)
    pygame.draw.line(window, BLUE, (60, 20), (60, 60), 4)
    pygame.draw.line(window, BLUE, (20, 20), (60, 60), 1)
    pygame.draw.line(window, BLUE, (20, 60), (60, 20), 1)

    # HOMEWORK: draw clover (zero clue)
    # using aalines would be better for clearify this code.
    # Part 1: Top
    pygame.draw.line(window, BLUE, (100, 10), (100, 30), 4)
    pygame.draw.line(window, BLUE, (100, 10), (120, 10), 4)
    pygame.draw.line(window, BLUE, (120, 10), (120, 30), 4)
    # Part 2: Left
    pygame.draw.line(window, BLUE, (80, 30), (80, 50), 4)
    pygame.draw.line(window, BLUE, (80, 30), (100, 30), 4)
    pygame.draw.line(window, BLUE, (80, 50), (100, 50), 4)
    # Part 3: Right
    pygame.draw.line(window, BLUE, (120, 30), (140, 30), 4)
    pygame.draw.line(window, BLUE, (120, 50), (140, 50), 4)
    pygame.draw.line(window, BLUE, (140, 30), (140, 50), 4)
    # Part 4: Bottom
    pygame.draw.line(window, BLUE, (100, 50), (100, 70), 4)
    pygame.draw.line(window, BLUE, (120, 50), (120, 70), 4)
    pygame.draw.line(window, BLUE, (100, 70), (120, 70), 4)

    pygame.draw.circle(window, GREEN, (250, 50), 30, 0)
    pygame.draw.circle(window, GREEN, (400, 50), 30, 2)

    pygame.draw.rect(window, RED, (250, 150, 100, 50), 0)
    pygame.draw.rect(window, RED, (400, 150, 100, 50), 1)

    pygame.draw.ellipse(window, YELLOW, (250, 250, 80, 40), 0)
    pygame.draw.ellipse(window, YELLOW, (400, 250, 80, 40), 2)

    pygame.draw.polygon(window, TEAL, ((240, 350), (350, 350),
                                       (410, 410), (350, 470),
                                       (240, 470), (170, 410)))

    pygame.draw.arc(window, BLUE, (20, 400, 100, 100), 0, 2, 5)

    pygame.draw.aaline(window, RED, (500, 400), (540, 470), 1)
    pygame.draw.aalines(window, BLUE, True,
                        ((580, 400), (587, 450),
                         (595, 460), (600, 444)), 1)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
