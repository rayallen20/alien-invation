import pygame.font


class Button:
    """按钮类"""

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性

        # 按钮宽/高
        self.width, self.height = 200, 50

        # 按钮背景颜色
        self.button_color = (0, 255, 0)

        # 按钮文本颜色
        self.text_color = (255, 255, 255)

        # 按钮字体样式和大小
        self.font = pygame.font.SysFont(None, 32)

        # 创建按钮对象 并使其居中

        # 创建按钮对象
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # 设置按钮位置为屏幕中心 即 按钮的中心点坐标 = 屏幕的中心点坐标
        self.rect.center = self.screen_rect.center

        # 创建按钮上的文字 并将这段文字渲染为图像 放在按钮的中心位置上
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将字符串 msg 渲染为图像 并使这个图像在按钮上的位置为居中"""

        # 将 字符串msg 渲染为图像
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # 字符串图像的 surface对象
        self.msg_image_rect = self.msg_image.get_rect()
        # 字符串图像的位置
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮 再绘制文本"""
        # 在屏幕上绘制按钮并用颜色填充
        self.screen.fill(self.button_color, self.rect)

        # 绘制文本
        self.screen.blit(self.msg_image, self.msg_image_rect)

"""
注释:
pygame.font模块:作用:将文本渲染到屏幕上
pygame.font.Sysfont(字体样式, 字体大小)
将文本渲染到屏幕上的方法:将文本渲染为图像
完成这个工作的方法: self.font.rendet(待渲染字符串,是否开启抗锯齿,文本颜色,背景色)
screen.fill(按钮背景色,按钮surface对象)
screen.blit(图像,该图像的surface对象)
"""