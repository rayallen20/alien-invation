import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


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

        # 此处 为避免主循环太过冗长 将有关监听事件的方法 都放在了game_functions这个模块中
        # 因此 不再需要在这个文件中import sys 因为只在game_functions中使用了这个模块 本文件中没有使用
        gf.check_events()

        # 此处 重构理由同上
        gf.update_screen(ai_settings, screen, ship)

run_game()
