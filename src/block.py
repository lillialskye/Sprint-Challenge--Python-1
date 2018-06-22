import pygame

from pygame.math import Vector2
from pygame import Rect

BLOCK_WIDTH = 40
BLOCK_HEIGHT = 20

#PADDLE_WIDTH = 40
#PADDLE_HEIGHT = 10

class Block:
    """
    Base class for square or rectangular object
    """

    def __init__(self, position, BLOCK_WIDTH, BLOCK_HEIGHT, color):
        # Create a rectangle centered around the x and y
        self.position = position
        self.rectangle = pygame.Rect(
                                    position.x - (BLOCK_WIDTH/2),
                                    position.y - (BLOCK_HEIGHT/2),
                                    BLOCK_WIDTH,
                                    BLOCK_HEIGHT)
        self.color = color
        self.touched_by_ball = False
    #creating rectangles
    def create_blocks(self):
        self.blocks =[]
            for w in range(8) #8 blocks wide
            for h in range(7) #7 blocks high
            self.blocks.append(pygame.Rect(w, h, BLOCK_WIDTH, BLOCK_WIDTH))




    def update(self, **kwargs):
        self.touched_by_ball = False

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass


