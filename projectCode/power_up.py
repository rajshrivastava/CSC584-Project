class Power:
    def __init__(self, data):
        self.player_powerImg = loadShape('images/player_power.png')
        self.bot_powerImg = loadShape('images/bot_power.png')
        self.player_power_positions = data['player_power']
        self.bot_power_positions = data['bot_power']
    
    def draw_player_power(self, idx): #idx <- random index
        x,y = self.player_power_positions[idx]
        image(self.player_powerImg, x, y)
        
    def draw_bot_power(self, idx): #idx <- random index
        x,y = self.bot_power_positions[idx]
        image(self.bot_powerImg, x, y)
        
