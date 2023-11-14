from src.game_scene.game_scene import game_scene
from classes.class_world import *
from src.game_scene.endgame import  endgame_scene

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