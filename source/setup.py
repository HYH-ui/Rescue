# 启动代码
from source import tools

import pygame
from . import constants as C

pygame.init()
pygame.display.set_mode(C.SCREEN_SIZE)


# 传入图片路径参数
GRAPHICS = tools.load_graphics('resource/')
