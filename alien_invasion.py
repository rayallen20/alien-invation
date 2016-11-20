import sys
import pygame

from settings import Settings


def run_game():
    # 初始化pygame 设置 屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')

    # 开始游戏主循环
    while True:

        # 监听键盘鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)

        # 使最后一次绘制的屏幕可见
        pygame.display.flip()

run_game()
