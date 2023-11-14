import pygame as py

def endgame_scene(world):
    for event in py.event.get():
        if event.type == py.QUIT:
            world.running = False

    world.draw_endgame()
    py.display.flip()