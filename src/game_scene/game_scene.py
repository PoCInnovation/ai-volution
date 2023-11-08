import pygame as py

from classes.class_world import *

def game_scene(world: class_world):

    for event in py.event.get():
        if event.type == py.QUIT:
            world.running = False

    world.actualised_time()
    world.draw_game()

    py.display.flip()