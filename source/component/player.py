# 主角
import pygame
from .. import constants as C
from .. import tools
from .. import setup

class palyer:
    def __init__(self):
        self.run_x()
        self.blood = C.PLAYER_BLOOD

    def run_x(self):
        self.x_vel = 0
        pass

    def shoot(self):
        pass

    def load_images(self):
        self.frames = []
        self.frames.append(tools.get_image(setup.GRAPHICS['mario_bros'],96, 0, 16, 32, (0, 0, 0), C.PLAYER_MULTI))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self,key):
        if key[pygame.K_RIGHT]:
            self.x_vel = 5
        if key[pygame.K_LEFT]:
            self.x_vel = -5

    def die(self):
        pass

    def damage(self):
        pass

