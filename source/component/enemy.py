# 敌人
from .. import constants as C
from .. import tools,setup
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, driection, name, frame_rects):
        self.driection = driection
        self.name = name
        self.frames_index = 0
        self.left_frames = []
        self.right_frames = []

        self.load_frames(frame_rects)
        self.frames = self.left_frames if self.driection == 0 else self.right_frames

    def load_frames(self, frames):
        for frames_rect in frames:
            left_fames = tools.get_image(setup.GRAPHICS['enemies'], *frames_rect, (0, 0, 0), C.Enemy_MULTI)
            right_fames = pygame.transform.flip(left_fames, True, False)
            self.left_frames.append(left_fames)
            self.right_frames.append(right_fames)

    def damage(self):
        pass

    def update(self):
        pass


class Goomba(Enemy):
    def __init__(self, x, y, direction, name):
        frame_rects = [(0, 16, 16, 16), (16, 16, 16, 16), (32, 16, 16, 16)]
        Enemy.__init__(x, y, direction, name, frame_rects)