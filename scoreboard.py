import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """本类用于显示得分信息"""

    def __init__(self, ai_settings, screen, stats):
        """
        初始化显示得分所需要用到的属性
        :param ai_settings: 设置对象
        :param screen: 屏幕
        :param stats: 统计信息对象
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 分数的字体设置
        self.text_color = (20, 20, 20)
        self.font = pygame.font.SysFont(None, 36)

        # 准备初始得分图像
        self.prep_score()
        # 准备最高得分图像
        self.prep_high_score()
        # 准备当前等级图像
        self.prep_level()
        # 准备飞船图像
        self.prep_ships()

    def prep_score(self):
        """
        将得分转换为渲染的图像
        :return:
        """
        # 前边在settings类中设置的分数提升规则为1.5倍 这样就会造成一个现象 分数不整齐
        # 使用round(num, -1) 将得分转换为10的整数倍 round()方法的第二个参数为-1时 即为将num整齐化到10的整数倍
        rounded_score = round(self.stats.score, -1)

        # "{:,}".format(num): 在数字中插入,
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将分数放置在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """
        在屏幕上显示得分和最高得分
        :return:
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将最高得分放置在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render(
            str(self.stats.level), True, self.text_color, self.ai_settings.bg_color
        )

        # 将等级图像放置在得分图像下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
