
class Settings():
    """Класс для хранения настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        #Параметры настройки игры
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Настройка корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        #ПАраметры снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 5
        #Настройка пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 3
        #fleet-direction = 1 обозначает движение вправо, а -1 влево
        self.fleet_direction = 1

