# 游戏主要入口

import pygame

from source import tools, setup
from source.states import level


def main():
    state_dict = {
        'level': level.level()
    }
    game = tools.Game(state_dict, 'level')
    game.run()
if __name__ == '__main__':
    main()
