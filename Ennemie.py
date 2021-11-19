import random
import pygame
from pygame.math import Vector2
import core

class Ennemie :
    def __init__(self):
        self.rayon = (random.randint(15, 30))
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = Vector2(random.randint(0,1200), random.randint(0, 800))
        self.mass = (self.rayon*2)
        self.nom = "Bleu"
        self.vitesse = 5
        self.vue = 75

    def mourir (self):
        self.position = Vector2(random.randint(0, 1200), random.randint(0, 800))


    def déplacer (self):
        pass

    def grossir (self):
        self.rayon = self.rayon + 1


    def draw (self, screen):
        pygame.draw.circle(screen, self.couleur, self.position,  self.rayon)
