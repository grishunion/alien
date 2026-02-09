
class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""
    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.sittings = ai_game.settings
        self.reset_stats()
        #Игра AI запускается в активном состоянии
        self.game_active = True

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.sittings.ship_limit    
