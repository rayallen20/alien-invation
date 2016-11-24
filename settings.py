class Settings:
    """存储 alien_invasion 的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船移动速度
        self.ship_speed_factor = 0.5
