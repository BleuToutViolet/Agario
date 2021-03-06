import random
import pygame
from pygame.math import Vector2
import core

drops = []
gravity=0.5

def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [400, 400]

    for i in range(0, 25):
        drops.append(Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(-400,0)))
    print("Setup END-----------")


def run():
    show()
    update()



def update():
    print(core.keyPressValue)
    for drop in drops:
        drop.y += gravity
        if drop.y > core.WINDOW_SIZE[1]:
            drop.x = random.randint(0, core.WINDOW_SIZE[0])
            drop.y = random.randint(-400, 0)

def show():
    core.cleanScreen()
    for drop in drops:
        pygame.draw.line(core.screen, (255, 0, 255), (drop.x, drop.y), (drop.x, drop.y + 10), 1)


core.main(setup, run)
