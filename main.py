#游戏主要入口
print('123')

import pygame

from source import tools,setup

def main():
    game = tools.Game()
    game.run(setup.GRAPHICS)


if __name__ == '__main__':
    main()
