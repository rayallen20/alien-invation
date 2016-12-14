class Settings:
    """存储 alien_invasion 的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 初始化游戏静态设置 start

        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船相关设置

        # 飞船移动速度
        # self.ship_speed_factor = 0.5
        # 可用飞船数量 说白了就是几条命
        self.ship_limit = 3

        # 子弹的相关设置

        # 子弹速度
        # self.bullet_speed_factor = 1
        # 子弹宽度
        self.bullet_width = 3
        # 子弹高度
        self.bullet_height = 15
        # 子弹颜色
        self.bullet_color = (60, 60, 60)
        # 允许出现在屏幕中的子弹数量
        # 此处 我做过测试 手速最快也只能同屏幕有5颗子弹 所以设置为10颗应该是看不出来的
        self.bullet_allowed = 50

        # 外星人相关设置

        # 外星人的横向移动速度
        # self.alien_speed_factor = 0.75
        # 外星人群向下移动的速度
        self.fleet_drop_speed = 7.5
        # fleet_direction: 1表示右移 -1表示左移
        self.fleet_direction = 1

        # 初始化游戏静态设置 end

        # 初始化游戏动态设置

        # 以何种速度加快游戏节奏
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置 即:动态设置"""

        # 飞船初始速度
        self.ship_speed_factor = 0.5
        # 子弹初始速度
        self.bullet_speed_factor = 1
        # 外星人群初始速度
        self.alien_speed_factor = 0.75
        # 方向flag 1表示向右 -1表示向左
        self.fleet_direction = 1

        # 击落每一个外星人的初始得分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置 此处的提高速度 是指 将飞船移速 子弹移速 外星人移速 同时提高"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
