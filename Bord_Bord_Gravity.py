import core
import pygame


def setup():
    print("setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [400, 400]

    core.memory("centredecercle", pygame.Vector2(200, 200))
    core.memory("rayonducercle", 50)
    core.memory("couleurducercle", (255, 255, 43))

    core.memory("gravity", 1)

    print("setup END-----------")


def run():
    print("running")
    core.cleanScreen()
    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"),
                       core.memory("rayonducercle"))
    core.memory("centredecercle", pygame.Vector2(core.memory("centredecercle").x, core.memory("centredecercle").y + core.memory("gravity")))
    if core.memory("centredecercle").y + core.memory("rayonducercle") > core.WINDOW_SIZE[1]:
        core.memory("gravity", core.memory("gravity") * -1)

    if core.memory("centredecercle").y - core.memory("rayonducercle") < 0:
        core.memory("gravity", core.memory("gravity") * -1)

    if core.getKeyPressList(pygame.K_r) :
        core.memory("centredecercle", pygame.Vector2(200, 200))
        core.memory("gravity", 1)


core.main(setup, run)
