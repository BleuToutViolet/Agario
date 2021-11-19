import random
import pygame
from pygame.math import Vector2


class Creep :
    def __init__(self):
        self.rayon = 3
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = Vector2(random.randint(0,1200), random.randint(0, 800))


    def mourir (self):
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = Vector2(random.randint(0, 1200), random.randint(0, 800))


    def draw (self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)

