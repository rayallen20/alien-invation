import sys
import pygame


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 让最近绘制的屏幕可见
                pygame.display.flip()

run_game()


'''
解释:
pygame.init() 初始化背景设置 让Pygame能够正确工作
pygame.display.set_mode(): 创建一个显示窗口 该方法接收一个元组 (宽,高)
screen:是一个surface surface是屏幕的一部分 用于显示游戏元素
display.se_mode() 返回的surface表示整个窗口
激活游戏的动画循环后,每一次循环豆浆自动重绘这个surface
while循环中 包含一个事件循环 和 管理屏幕更新的代码
事件即js中的鼠标/键盘事件的概念
pygame.event.get() 监听所有的键盘/鼠标事件
例:pygame.QUIT 即为玩家单击游戏关闭按钮事件
pygame.display.flip():使Pygame让最近绘制的屏幕可见
即:每次while循环时 都绘制一个空屏幕 并擦去旧的屏幕 用以显示元素的新位置 并在原来的位置隐藏元素 达到平滑移动的效果
'''
