import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """单个外星人类"""
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像 设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定的位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """
        如果外星人位于屏幕边缘 就返回True
        两种情况为"位于屏幕边缘":1.距右侧距离大于屏幕右侧距离 2.距左侧距离小于屏幕左侧距离
        :return:
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
"""
解释:
self.rect.x : 左边距
self.rect.y : 上边距
此处设置
每一个外星人的左边距都等于其图像宽度
每一个外星人的上边距都等于其图像高度
"""