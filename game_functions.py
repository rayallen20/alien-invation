# 本模块用于处理让游戏运行起来的方法 目的在于避免主循环中的代码太长
import sys
from time import sleep
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
    # 按x键为开外挂
    elif event.key == pygame.K_x:
        ai_settings.bullet_width = ai_settings.screen_width
        fire_bullet(ai_settings, screen, ship, bullets)
        ai_settings.bullet_width = 3
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


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
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

    # 如果游戏处于非活动状态 就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 刷新屏幕
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹的位置 并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # 如果外星人群都被消灭了 那么就再生成一个新的外星人群
    if len(aliens) == 0:
        # 删除目前屏幕上的子弹 以免刚生成一批新的外星人 就有外星人中弹了
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


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


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将外星人群向下移动 并改变水平移动的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """
    响应被外星人撞到的飞船
    当有外星人撞到飞船时调用本函数
    本函数要做如下几件事:
    1. 将可用飞船数量 -1
    2. 清空子弹和外星人list
    3. 创建一群外星人
    4. 将新的飞船放置在底部中央
    5. 暂停一会儿 以便玩家反应过来是新的一轮游戏了
    :param ai_settings: 设置类
    :param stats: 统计当前信息类
    :param screen: 屏幕surface
    :param ship: 飞船surface
    :param aliens: 外星人Group
    :param bullets: 子弹Group
    :return:
    """
    if stats.ships_left > 0:
        # 飞船数量-1
        stats.ships_left -= 1

        # 清空子弹Group 和 外星人Group
        bullets.empty()
        aliens.empty()

        # 创建一群新的外星人
        create_fleet(ai_settings, screen, ship, aliens)

        # 将新的飞船放在屏幕底部中央位置
        ship.center_ship()

        # 暂停1.5秒 让玩家反应过来这是新游戏
        sleep(1.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端 如果有 调用ship_hit 即和飞船被外星人撞到了的情况 做同样的处理"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            # 调用 ship_hit 和飞船被撞 做同样的处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘 并更新外星人的位置 检查是否有外星人碰撞到了飞船"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # 检测是否有外星人到达屏幕底端 如果有 做处理
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

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

"""
pygame.sprite.groupcollide(GroupA, GroupB, 是否杀死A, 是否杀死B)
sprite.groupcollide()方法:将GroupA和GroupB的每个元素的rect进行对比 并返回一个dict 其中包含发生碰撞的元素
第三 四 两个参数 设置为是否删除掉这两个发生碰撞的元素
"""

"""
pygame.sprite.spritecollideany(Sprite,Group):这个方法检测编组(多个)中是否有成员与精灵(单个)发生碰撞
并在找到和精灵发生了碰撞的成员后就停止遍历编组 返回第一个与精灵发生碰撞的编组中的成员
如果没有发生碰撞 pygame.sprite.spritecollideany()方法会返回 None 因此 update_aliens()方法中的
if pygame.sprite.spritecollideany() 中的代码 是不会被执行的
"""