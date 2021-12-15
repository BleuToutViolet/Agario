import core
import pygame
import random
from pygame.math import Vector2
from Creep import Creep
from Joueur import Joueur
from Ennemie import Ennemie

def setup():
    print("setup START---------")
    core.fps = 144
    core.WINDOW_SIZE = [1200, 800]


    core.memory("TableCreep", [])
    core.memory("TableEnnemie", [])
    core.memory("joueur", Joueur())
    core.memory("Ennemie", Ennemie())


    for i in range(300):
        core.memory("TableCreep").append(Creep())

    for i in range(5):
        core.memory("TableEnnemie").append(Ennemie())

    print("setup END-----------")


def run():
    core.cleanScreen()
    if core.getKeyPressList("r"):
        core.memory("joueur", Joueur())


    for i in core.memory("TableCreep"):
        i.draw(core.screen)


    for i in core.memory("TableEnnemie"):
        i.draw(core.screen)
        i.deplacer()
#Contrôle pour le joueur
    if core.memory("joueur").vivant:
        core.memory("joueur").draw(core.screen)
        core.memory("joueur").deplacer(core.getMouseLeftClick())


        for i in core.memory("TableCreep") :
            if i.position.distance_to(core.memory("joueur").position) < core.memory("joueur").rayon + i.rayon :
                i.mourir()
                core.memory("joueur").grossir()

    #Gestion de la mort à partir de l'ennemie
        for i in core.memory("TableEnnemie"):
            #qui mange qui?
            if i.position.distance_to(core.memory("joueur").position) < core.memory("joueur").rayon + i.rayon:
                if i.rayon > core.memory("joueur").rayon:
                    i.grossir()
                    core.memory("joueur").mourir()
                else:
                    i.mourir()
                    core.memory("joueur").grossir()


core.main(setup, run)
