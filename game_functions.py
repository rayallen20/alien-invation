# 本模块用于处理让游戏运行起来的方法 目的在于避免主循环中的代码太长
import sys
import pygame


def check_events():
    """
    检查事件是否为退出
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """

    :param ai_settings: 设置
    :param screen: 屏幕
    :param ship: 飞船
    :return:
    """
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 刷新屏幕
    pygame.display.flip()

