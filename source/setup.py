# 启动代码 将
import pygame
from . import tools
from . import constants as C

pygame.init()
pygame.display.set_mode(C.SCREEN_SIZE)
SCREEN = pygame.display.set_mode((C.SCREEN_W, C.SCREEN_H))

# 传入图片路径参数
GRAPHICS = tools.load_graphics('source/resources/graphics/')

PLAYER_GRAPHICS = tools.load_graphics('source/resources/graphics/player_attack/')
