import random
import pygame
from pygame.math import Vector2

class Joueur :
    def __init__(self):
        self.rayon = 5
        self.couleur = (255, 255, 255)
        self.position = Vector2(random.randint(0,1200), random.randint(0, 800))
        self.mass = 20
        self.nom = "Bleu"
        self.vitesse = 5
        self.direction = Vector2()
        self.vitesseMax = 3


        self.L = Vector2(0, 0)
        self.l = 0
        self.lo = 10
        self.Ux = 0
        self.Fx = 0
    def mourir (self):
        self.position = Vector2(random.randint(0, 1200), random.randint(0, 800))

    def deplacer (self,clique):
        if clique is not None:
            self.Ux = Vector2(clique) - self.position
            self.l= self.Ux.length()
            self.Ux= self.Ux.normalize()
            self.L= abs(self.l - self.lo)
            self.Fx= 0.00004 * self.L * self.Ux
            self.direction= self.direction + self.Fx

        self.position = self.position + self.direction

    def grossir (self):
        self.rayon = self.rayon + 1


    def draw (self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)

