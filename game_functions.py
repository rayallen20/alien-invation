# 本模块用于处理让游戏运行起来的方法 目的在于避免主循环中的代码太长
import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 按→向右移动飞船
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # 按←向左移动飞船
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # 按z键创建并发射一颗子弹
    elif event.key == pygame.K_z:
        fire_bullet(ai_settings, screen, ship, bullets)
    # 按q键退出
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """
    :param ai_settings 设置类
    :param screen 屏幕surface
    :param ship: 飞船对象
    :param bullets: 子弹类的Group
    检查事件是否为退出
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 检查是否为按下键盘事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        # 检查是否为抬起键盘事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """
    主循环时 重绘 刷新屏幕
    :param ai_settings: 设置类的对象
    :param screen: pygame.display.set_mode 屏幕
    :param ship: 飞船类的实例化对象
    :param aliens: 外星人Group
    :param bullets: 子弹类的Group
    :return:
    """
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)

    # 在飞船和外星人后边重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 刷新屏幕
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置 并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到限制数,就发射一颗子弹"""
    if len(bullets) < ai_settings.bullet_allowed:
        bullet = Bullet(ai_settings, screen, ship)
        bullets.add(bullet)


def get_numbers_alien_x(ai_settings, alien_width):
    """
    计算每行可容纳多少个外星人
    :param ai_settings: 设置类
    :param alien_width: 外星人宽度
    :return: int number_aliens_x: 每行可容纳的外星人的数量
    """
    # 可以用来显示外星人的宽度 (因为外星人的左边和右边 都有间距 所以 - 2 * alien_width)
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    # 一行中可显示的外星人的数量 = 可用空间 / (外星人宽度 + 间距) 因为 外星人宽度 = 间距 所以 2 * alien_width
    numbers_aliens_x = int(available_space_x / (2 * alien_width))
    return numbers_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """
    创建一个外星人 并放在当前行
    :param ai_settings: 设置类
    :param screen: 屏幕surface对象
    :param aliens: 外星人Group
    :param alien_number: 每行能显示的外星人数量
    :param row_number: 共应显示多少列外星人
    :return:
    """
    # 外星人的x轴间距为外星人图片宽度
    alien = Alien(ai_settings, screen)
    # 外星人宽度
    alien_width = alien.rect.width
    # 外星人x坐标 = 左边距 + (外星人surface对象宽度 + 间距) * 外星人数量
    alien.x = alien_width + 2 * alien_width * alien_number
    # 设置每一个外星人 距左侧的位置
    alien.rect.x = alien.x
    # 外星人y坐标 = 外星人群距上侧高度(即外星人高度) + (外星人高度 + 行间距) * 所在行数
    alien.y = alien.rect.height + alien.rect.height * 2 * row_number
    # 设置每一个外星人 距上侧的位置
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """
    创建外星人群
    :param ai_settings: 设置类
    :param screen: 屏幕的surface对象
    :param ship: 飞船类
    :param aliens: 外星人的Group类
    :return:
    """
    # 创建一个外星人 并计算一行可容纳多少个外星人
    # 外星人的x轴间距为外星人图片宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_numbers_alien_x(ai_settings, alien.rect.width)
    # 外星人的y轴间距为外星人图片高度
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    # 循环y行
    for row_number in range(number_rows):
        # 循环x列
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_rows(ai_settings, ship_height, alien_height):
    """
    本函数用于计算屏幕高度可容纳多少行外星人
    :param ai_settings: 设置类
    :param ship_height: 飞船高度
    :param alien_height: 外星人高度
    :return: number_rows: int 飞船的行数
    """
    # 最上边那一行的上边距 为外星人的高度
    # 外星人群与飞船之间的距离 为2倍的外星人的高度
    # 所以加在一起为 3 * alien_height
    # 下面这行代码的意思为: 外星人群可用的高度 =  屏幕总高度 - 外星人群上边距 - 外星人群距离飞船高度 - 飞船高度
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    # 外星人群的每一行: 由2部分组成 1. 外星人本身的高度 2. 外星人群的行间距 此处 第2部分为 外星人的高度
    # 所以 下面这行代码的意思为: 外星人群行数 = 外星人群可用高度 / (外星人本身高度 + 外星人群行间距)
    # 然后取整
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

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

"""
重构check_events() 将监听按下按键和松开按键两部分代码写成2个函数
"""

"""
因加入子弹元素 而对check_keydown_events()函数做出修改 解读如下
bullets 即 主循环中 子弹类的编组 这个编组 可以当做一个list来使用
对新增的创建子弹对象的说明:
如果按下的是z键 就创建一个子弹对象
"""

"""
aliens.draw(screen): Group.draw() 绘制编组中的每个元素 元素的位置由rect属性决定
"""