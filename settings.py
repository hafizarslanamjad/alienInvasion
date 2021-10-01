class Settings():
    """ A class to store all the settings for Alien Invasion """
    def __init__(self):
        """Initialize the game settings """
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = 250,250,250

        #Ship Settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3

        #Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50

        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
