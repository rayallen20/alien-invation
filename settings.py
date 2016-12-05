class Settings:
    """存储 alien_invasion 的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船移动速度
        self.ship_speed_factor = 0.5

        # 子弹的相关设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # 允许出现在屏幕中的子弹数量
        # 此处 我做过测试 手速最快也只能同屏幕有5颗子弹 所以设置为10颗应该是看不出来的
        self.bullet_allowed = 50

        # 存储外星人的横向移动速度
        self.alien_speed_factor = 0.75
        # 外星人群向下移动的速度
        self.fleet_drop_speed = 7.5
        # fleet_direction: 1表示右移 -1表示左移
        self.fleet_direction = 1
