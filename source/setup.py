# 启动代码
import pygame
from . import tools
from . import constants as C

pygame.init()
pygame.display.set_mode(C.SCREEN_SIZE)


# 传入图片路径参数
GRAPHICS = tools.load_graphics('source/resources/graphics/')
