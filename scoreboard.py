import pygame.font


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

    def prep_score(self):
        """
        将得分转换为渲染的图像
        :return:
        """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将分数放置在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """
        在屏幕上显示得分
        :return:
        """
        self.screen.blit(self.score_image, self.score_rect)
