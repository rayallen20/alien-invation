import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 向右移动flag
        self.moving_right = False
        # 向左移动flag
        self.moving_left = False

    def update(self):
        """根据flag 调整飞船位置"""
        # 持续向右移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 左右移动最小单位为1个像素?
            # self.rect.centerx += 1
            # 更新飞船的center值 而不更新rect
            self.center += self.ai_settings.ship_speed_factor
        # 持续向左移动
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center来更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """设定飞船在屏幕上的位置为底部居中"""
        self.center = self.screen_rect.centerx

"""
解释:
__init__()中的screen: 即self,screen 指定了将飞船绘制到什么地方
pygame.image.load() 返回一个表示图片的surface 将这个surface给了self.image
get_rect() 获取该surface的属性rect (rect本身也是一个对象)
image.get_rect() 获取图片的rect对象
screen.get_rect() 获取屏幕的rect对象
get_rect()概述:
也就是说 在代码中处理的 并不是 "飞船" 这个游戏元素 而是 "飞船图片" 这个rect形状
处理rect对象时 使用矩形四角和中心的x,y坐标 通过设置这些值 来指定矩形的位置
位置属性概述:
center centerx centery 设置rect对象居中常用
top bottom left right 设置rect对象与屏幕边缘对齐常用
x y 调整rect对象的水平或垂直位置
x y 坐标系概述:
pygame中 以左上角为原点 水平向右为x轴正方向 垂直向下为y轴正方向
self.rect.centerx = self.screen_rect.centerx 将飞船的中心点的x坐标 设置为 屏幕中心点的x坐标
self.rect.bottom = self.screen_rect.bottom 将飞船下边缘的y坐标 设置为 屏幕下边缘的y坐标
blitme()方法中  screen.blit(要绘制的图像surface, 背景surface) 即根据__init__中的rect的位置 在screen上绘制图像


"""
"""
centerx:只接受整数数值 如果需要小数数值 则按上述代码修改
self.rect.centerx 是一个int 所以拿它去 += -= 一个float 就会出现 只接受整数部分并进行计算的情况
所以此处的解决办法是 用self.center = float(self.rect.centerx)  使代表位置的那个值 能进行浮点数运算 然后 再将这个运算后的值 赋给 self.rect.centerx
"""


"""
检测ship.rect.right时  因为不知道屏幕有多宽 所以需要用ship.rect.right < ship.screen_rect.right 作为判断条件
但是 检测ship.rect.left时 因为屏幕左侧一定是从0开始计算 所以 只需要比较 ship.rect.left > 0 即可
"""