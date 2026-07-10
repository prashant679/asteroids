from circleshape import CircleShape
import pygame
import constants
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x:float, y:float, radius:float)-> None:
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,
                           "white",
                           self.position,
                           self.radius,
                           constants.LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        Asteroid.kill(self)
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        aster1 = self.velocity.rotate(angle)
        aster2 = self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        aster_1 = Asteroid(self.position.x,self.position.y,new_radius)
        aster_1.velocity += aster1 * 1.2
        aster_2 = Asteroid(self.position.x,self.position.y,new_radius)
        aster_2.velocity += aster2 * 1.2
