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

    core.memory("centredecercle", pygame.Vector2(400, 400))
    core.memory("rayonducercle", 10)
    core.memory("couleurducercle", (0, 0,255))
    core.memory("direction", pygame.Vector2(0,0))
    core.memory("L", 0)
    core.memory("l", 10)
    core.memory("lo", 0)
    core.memory("Ux", 0)
    core.memory("TableCreep", [])
    core.memory("TableEnnemie", [])
    core.memory("TableJoueur", [])


    for i in range(300):
        core.memory("TableCreep").append(Creep())

    for i in range(5):
        core.memory("TableEnnemie").append(Ennemie())

    core.memory("joueur",Joueur())
    core.memory("ennemie", Ennemie())




    print("setup END-----------")


def run():
    print("running")
    core.cleanScreen()

    core.memory("joueur").deplacer(core.getMouseLeftClick())


    core.printMemory()
    core.memory("centredecercle", core.memory("direction")+core.memory("centredecercle"))

    core.printMemory()
    for i in core.memory("TableCreep"):
        i.draw(core.screen)
    core.printMemory()
    for i in core.memory("TableEnnemie"):
        i.draw(core.screen)
    core.printMemory()
    core.memory("joueur").draw(core.screen)

    for i in core.memory("TableCreep") :
        if i.position.distance_to(core.memory("joueur").position) < core.memory("joueur").rayon + i.rayon :
            i.mourir()
            core.memory("joueur").grossir()
    for i in core.memory("TableCreep"):
        if i.position.distance_to(core.memory("ennemie").position) < core.memory("ennemie").rayon + i.rayon:
            i.mourir()
            core.memory("ennemie").grossir()
    for i in core.memory("TableEnnemie"):
        if i.position.distance_to(core.memory("joueur").position) < core.memory("joueur").rayon + i.rayon:
            i.mourir()
            core.memory("joueur").grossir()
        else :
            core.memory("joueur").mourir()
            i.grossir()
    for i in core.memory("TableJoueur"):
        if i.position.distance_to(core.memory("ennemie").position) < core.memory("ennemie").rayon + i.rayon:
            i.mourir()
            core.memory("ennemie").grossir()
        else :
            i.grossir
            core.memory("ennemie").mourir()
core.main(setup, run)
