# 主角
import pygame
from .. import constants as C
from .. import tools
from .. import setup


class Player:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_data()
        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()

        self.x_vel = 0
        self.y_vel = 0

    def load_data(self):
        pass

    def setup_states(self):
        pass

    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0

    def setup_timers(self):
        self.walking_timer = 0

    def load_images(self):
        player_frames = setup.PLAYER_GRAPHICS

        self.right_frames = []
        self.left_frames = []

        for name in player_frames:
            sheet = player_frames[name]
            right_f = tools.get_image(sheet, 0, 0, 128, 128, (0, 0, 0), C.PLAYER_MULTI)
            left_f = pygame.transform.flip(right_f, True, False)
            self.right_frames.append(right_f)
            self.left_frames.append(left_f)
        #frame_rects = self.player_data['image_frames']


        self.frames = self.right_frames

        self.frames_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frames_index]
        self.rect = self.image.get_rect()

    def update(self, keys):
        self.current_time = pygame.time.get_ticks()
        # 根据输入改变速度
        if keys[pygame.K_RIGHT]:
            self.x_vel = 5
            self.frames = self.left_frames
        elif keys[pygame.K_LEFT]:
            self.x_vel = -5
            self.frames = self.right_frames
        else:
            self.x_vel = 0
            self.frames_index = 3
        if self.current_time - self.walking_timer > 100:
            self.walking_timer = self.current_time
            self.frames_index += 1
            self.frames_index %= 12
            self.image = self.frames[self.frames_index]

    def damage(self):
        pass
