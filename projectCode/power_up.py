import random
class Power:
    def __init__(self, data):
        self.powerUp_img = loadImage('images/powerUp.png')
        self.powerUp_img.resize(30,30)
        self.powerUp_positions = data['powerUp']
        
        self.powerDown_img = loadImage('images/powerDown.png')
        self.powerDown_img.resize(30,30)
        self.powerDown_positions = data['powerDown']
        
        self.immunity_img = loadImage('images/immunity.png')
        self.immunity_img.resize(30,30)
        self.immunity_positions = data['immunity']
        
        self.isPowerUp_drawn = False
        self.isPowerDown_drawn = False
        self.isImmunity_drawn = False
    
    def draw_powerUp(self, idx): #idx <- random index
        x,y = self.powerUp_positions[idx]
        image(self.powerUp_img, x, y)
        
    def draw_powerDown(self, idx): #idx <- random index
        x,y = self.powerDown_positions[idx]
        image(self.powerDown_img, x, y)
    
    def draw_immunity(self, idx): #idx <- random index
        x,y = self.immunity_positions[idx]
        image(self.immunity_img, x, y)
        
