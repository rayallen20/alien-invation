class GameStats:
    """游戏统计信息类"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        # Q: 为什么ships_left 作为GameStats的一个成员属性 不写在 __init__中呢?
        # A: 每当玩家开始一次新游戏时 有些统计信息 是要重置的
        #    因此 单独写一个方法用来统计玩家当前的统计信息(比如现在还剩下几条命)
        #    而不是都写在 __init__中
        self.ships_left = self.ai_settings.ship_limit
