# 本模块用于处理让游戏运行起来的方法 目的在于避免主循环中的代码太长
import sys
import pygame
from bullet import Bullet


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


def update_screen(ai_settings, screen, ship, alien, bullets):
    """
    主循环时 重绘 刷新屏幕
    :param ai_settings: 设置类的对象
    :param screen: pygame.display.set_mode 屏幕
    :param ship: 飞船类的实例化对象
    :param alien: 外星人类的实例化对象
    :param bullets: 子弹类的Group
    :return:
    """
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.blitme()

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