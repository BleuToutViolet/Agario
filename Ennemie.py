import random
import pygame
from pygame.math import Vector2
import core

class Ennemie :
    def __init__(self):
        self.rayon = 10
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = Vector2(random.randint(0,1200), random.randint(0, 800))
        self.mass = (self.rayon*1.5)
        self.nom = 0
        self.direction = Vector2()
        self.vMax=5
        self.vue = 75

    def mourir (self):
        self.position = Vector2(random.randint(0, 1200), random.randint(0, 800))

    def deplacer (self):

        self.Ux = Vector2(random.randint(-1, 1), random.randint(-1, 1))

        self.direction = self.Ux + self.direction

        self.position = self.position + self.direction

    def grossir (self):
        self.rayon = self.rayon + 0.2


    def draw (self, screen):
        pygame.draw.circle(screen, self.couleur, self.position,  self.rayon)
