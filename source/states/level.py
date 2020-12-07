# 状态机

from ..component import player, enemy
import pygame
from .. import tools, setup
from .. import constants as C

class level:
    def __init__(self):
        self.finished = False
        self.next = None
        self.setup_background()
        self.setup_player()

    def setup_player(self):
        # 创建马里奥
        self.player = player.Player()
        self.player.rect.x = 100
        self.player.rect.y = 300

    def setup_background(self):
        # 设置关卡地图
        self.background = setup.GRAPHICS['maps']
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(rect.width * C.BG_MULTI),
                                                                   int(rect.h * C.BG_MULTI)))
        self.background_rect = self.background.get_rect()
        self.game_window = setup.SCREEN.get_rect()

    def update(self, surface, keys):
        # 更新画面和游戏数据
        self.player.update(keys)
        self.update_player_position()
        self.updata_game_windown()
        self.draw(surface)

    def updata_game_windown(self):
        self.game_window.x += self.player.x_vel
        if self.game_window.x <= 0:
            self.game_window.x = 0
        elif self.game_window.x >= 1675:
            self.game_window.x = 1675
        print(self.game_window.x)


    def update_player_position(self):
        # 根据玩家速度更新位置更新
        # self.player.rect.x += self.player.x_vel
        self.player.rect.y += self.player.y_vel

    def draw(self, surface):
        # 将玩家的图片画在画布上
        surface.blit(self.background, (0, 0), self.game_window)
        surface.blit(self.player.image, self.player.rect)
