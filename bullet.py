import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所在的位置 创建一个子弹对象"""
        super().__init__()
        self.screen = screen

        # 在(0,0)的位置上 创建一个表示子弹的矩形
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 然后再根据飞船的位置 设置子弹的正确位置
        # 子弹x轴位置
        self.rect.centerx = ship.rect.centerx
        # 子弹顶部位置
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹y轴位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示位置的浮点数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

"""
注解:
pygame.Rect(矩形左上角x坐标, 矩形左上角y坐标,矩形surface宽度,矩形surface高度) 因为子弹并非基于图像 所以要自己创建一个矩形
self.rect.top 矩形surface的顶部
self.y 矩形surface的y轴位置
问题1.Sprite类:将游戏中相关元素编组 进而同时操作编组中的所有元素(这句话不太明白是什么意思)
可以使用pygame.sprite.group类 来管理所有sprite类的子类？
pygame.sprite.group类 类似于一个列表 但提供了有助于开发游戏的额外功能
问题2.rect.y 和 rect.top 有什么区别
"""