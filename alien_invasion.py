import pygame

from pygame.sprite import Group
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
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:

        # 此处 为避免主循环太过冗长 将有关监听事件的方法 都放在了game_functions这个模块中
        # 因此 不再需要在这个文件中import sys 因为只在game_functions中使用了这个模块 本文件中没有使用
        gf.check_events(ai_settings, screen, ship, bullets)

        # 在主循环中调用ship对象的update方法 只有在这个位置上调用update() 才能保证按住→飞船能一直移动
        ship.update()

        # 同ship.update() 主循环中调用update方法 更新位置 但是 这是对所有Bullet对象都生效的
        # 当子弹超过屏幕上方时 删除这个surface
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        # print(len(bullets))

        # 更新子弹位置
        gf.update_aliens(ai_settings, ship, aliens)

        # 此处 重构理由同上
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
