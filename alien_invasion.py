import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    # 初始化pygame 设置 屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船 必须在主while循环前创建Ship实例 否则将每次循环时都创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        # 监听键盘鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕
        # ship.blitme() 一定要在主屏幕绘制后再绘制 否则表示飞船的surface对象 会被主屏幕的srcface对象遮挡 就看不到飞船了
        # 屏幕的遮挡 类似于 美术的 互相遮挡概念 即最上层的surface对象 要最后被绘制 有点类似内存中堆栈的概念
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 使最后一次绘制的屏幕可见
        pygame.display.flip()

run_game()
