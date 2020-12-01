#游戏主要入口
print('123')

import pygame

from source import tools,setup

def main():
    print('test冲突')
    game = tools.Game()
    game.run(setup.GRAPHICS)


if __name__ == '__main__':
    main()
