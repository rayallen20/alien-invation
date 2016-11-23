# 本模块用于处理让游戏运行起来的方法 目的在于避免主循环中的代码太长
import sys
import pygame


def check_events(ship):
    """
    :param ship: 飞船对象
    检查事件是否为退出
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 检查是否为键盘事件
        elif event.type == pygame.KEYDOWN:
            # 检查是否为键盘→键被按下了
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """
    主循环时 重绘 刷新屏幕
    :param ai_settings: 设置类的对象
    :param screen: pygame.display.set_mode 屏幕
    :param ship: 飞船类的实例化对象
    :return:
    """
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 刷新屏幕
    pygame.display.flip()

"""
对"事件"的解读:
每当用户按键或者点击鼠标时 都将在Pygame中注册一个事件
事件都是通过pygame.event.get()获取到的
因此 需要在check_events()中 指定要检查哪类事件
注:按键为KEYDOWN事件 →为K_RIGHT
"""

"""
此时 有几个问题
1.只有按一下→ 飞船才会向右移动 按住→ 没有反应
2.如果一直按→ 则飞船会移出屏幕
"""