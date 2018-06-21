import math

from pygame.math import Vector2
from pygame import Rect

from block import KineticBlock

class Ball:
    """
    base class for bouncing objects
    """
    def __init__(self, bounds, position, velocity, color, radius):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.radius = radius
        self.collision_rectangle = self.update_rectangle()

    def update_rectangle(self):
        return Rect(self.position.x - self.radius,
                                        self.position.y - self.radius,
                                        self.radius*2, self.radius*2)

    def update(self, **kwargs):
        if self.position.x <= 0 + self.radius: # screen width
            self.position.x = self.radius + 1
            self.velocity.x *= -1
        if self.position.x >= self.bounds[0] - self.radius:
            self.position.x = self.bounds[0] - self.radius - 1
            self.velocity.x *= -1
        if self.position.y <= 0 + self.radius: # screen height
            self.position.y = self.radius + 1
            self.velocity.y *= -1
        if self.position.y >= self.bounds[1] - self.radius:
            self.position.y = self.bounds[1] - self.radius - 1
            self.velocity.y *= -1

        self.position += self.velocity
        self.collision_rectangle = self.update_rectangle()

    def check_collision(self):
        # No collision on base models
        pass

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

class GameBall(Ball):
    """
    A ball that collides with blocks
    """
    def __init__(self, mass, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        self.mass = mass
        super().__init__(bounds, position, velocity, color, radius)

    def collide_with_ball(self, object, relative_vector):

        #TODO:  Calculate the correct position and move there directly
        while relative_vector.length() <= self.radius + object.radius:
            self.position += relative_vector.normalize()
            object.position -= relative_vector.normalize()
            relative_vector = self.position - object.position

        self_speed = self.velocity.length()
        object_speed = object.velocity.length()

        self.velocity = self.velocity.reflect(relative_vector).normalize()
        self.velocity *= object_speed

        object.velocity = object.velocity.reflect(relative_vector).normalize()
        object.velocity *= self_speed

        self.position += self.velocity
        object.position += object.velocity

    def collide_with_rectangle(self, object):
        # This function is called after a first-pass test, that is the collision
        # rectangles overlap. 
        
        left, right, top, bottom = False, False, False, False
        # TODO:  This can probably be optimized
        if (
            object.position.x > self.position.x and
            object.position.x - object.rectangle.width/2 <= self.position.x + self.radius and 
            self.position.y <= object.position.y+object.rectangle.height/2 and 
            self.position.y >= object.position.y - object.rectangle.height/2
        ):
            left = True

        if (
            object.position.x < self.position.x and
            object.position.x + object.rectangle.width/2 >= self.position.x - self.radius and 
            self.position.y <= object.position.y+object.rectangle.height/2 and 
            self.position.y >= object.position.y - object.rectangle.height/2
        ):
            right = True

        if (
            object.position.y > self.position.y and
            object.position.y - object.rectangle.height/2 <= self.position.y + self.radius and 
            self.position.x <= object.position.x+object.rectangle.width/2 and 
            self.position.x >= object.position.x - object.rectangle.width/2
        ):
            top = True

        if (
            object.position.y < self.position.y and
            object.position.y + object.rectangle.width/2 >= self.position.y - self.radius and 
            self.position.x <= object.position.x+object.rectangle.width/2 and 
            self.position.x >= object.position.x - object.rectangle.width/2
        ):
            bottom = True

        test = left + right + top + bottom
        
        if test == 1:
            object.touched_by_ball = True
            # the ball has collided with an edge
            # TODO:  # fix sticky edges
            if left or right:
                self.velocity.x *= -1
                if left:
                    self.position.x = object.position.x - object.rectangle.width/2 - self.radius - 1
                else:
                    self.position.x = object.position.x + object.rectangle.width/2 + self.radius + 1

            if top or bottom:
                self.velocity.y *= -1
                if top:
                    self.position.y = object.position.y - object.rectangle.height/2 - self.radius - 1
                else:
                    self.position.y = object.position.y + object.rectangle.height/2 + self.radius + 1

        elif test == 4:
            # TODO:  Better error handling
            print('error:  ball inside rectangle')

        elif test == 0:
            # We are at a corner.  Either it narrowly missed, or it hit the corner
            corners = [
                Vector2(object.position.x - object.rectangle.width/2, object.position.y - object.rectangle.height/2),
                Vector2(object.position.x + object.rectangle.width/2, object.position.y - object.rectangle.height/2),
                Vector2(object.position.x - object.rectangle.width/2, object.position.y + object.rectangle.height/2),
                Vector2(object.position.x + object.rectangle.width/2, object.position.y + object.rectangle.height/2)
            ]

            for corner in corners:
                relative_vector = self.position - corner
                if relative_vector.length() <= self.radius:
                    object.touched_by_ball = True
                    # Create a dummy object to make use of ball to ball collision, because the math is the same
                    # Give it a velocity of the same magnitude as the current ball to cause it to reflect at
                    # the same speed
                    stand_in = Ball(self.bounds, corner, Vector2(0, self.velocity.length()), [0,0,0], 0)
                    self.collide_with_ball(stand_in, relative_vector)

    def check_collision(self):
        # Warning!:  This is a primitive method of collision detection
        # Consider time complexity when adding more of this type
        index = self.object_list.index(self)
        for object in self.object_list[index+1:]:  # TODO: Check effeciency
            # Balls colliding with blocks
            if issubclass(type(object), KineticBlock) and object != self:
                # Do a first round pass for collision (we know object is a KineticBlock)
                if self.collision_rectangle.colliderect(object.rectangle):
                    self.collide_with_rectangle(object)
