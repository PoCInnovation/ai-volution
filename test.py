from src.game_scene.game_scene import game_scene
from classes.class_world import *

def endgame_scene(world):
    for event in py.event.get():
        if event.type == py.QUIT:
            world.running = False

    world.draw_endgame()
    py.display.flip()


def main():
    py.init()
    world = class_world()
    FPS = 200
    clock = py.time.Clock()
    clock.tick(FPS)

    while world.running:
        if world.scene == scene(1):
            game_scene(world)
        if world.scene == scene(2):
            endgame_scene(world)
    py.quit()


if __name__ == '__main__':
    main()