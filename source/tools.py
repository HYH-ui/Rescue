# 工具和游戏主控


import pygame
import os
from . import constants as C

class Game:
    def __init__(self, state_dict, start_state):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.state_dict = state_dict
        self.start = self.state_dict[start_state]

    def update(self):
        if self.start.finished:
            next_state = self.start.next
            self.start.finished = False
            self.start = self.state_dict[next_state]
        self.start.update(self.screen, self.keys)

    def run(self):
        done = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    quit()
                # 按下按键时触发
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                    print('按下下键')
                # 抬起按键时触发
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
                    print('抬起按键')

            self.update()
            pygame.display.update()
            self.clock.tick(60)


# 读取图片并返回


def load_graphics(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics
# sheet传入一张图片，(x,y)传入左上角坐标，(width,height)方框的宽高，colorkey图片底色，scale放大倍数

#  绘画，更新


def get_image(sheet, x, y, width, height, colorkey, scale):
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
    return image
