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
        
        self.isPowerUp_active = False
        self.isPowerDown_active = False
        self.isImmunity_active = False
    
    def activate_powerUp(self, idx): #idx <- random index
        self.isPowerUp_active = True
        self.powerUp_location = self.powerUp_positions[idx]
        
    def activate_powerDown(self, idx): #idx <- random index
        self.isPowerDown_active = True
        self.powerDown_location = self.powerDown_positions[idx]
    
    def activate_immunity(self, idx): #idx <- random index
        self.isImmunity_active = True
        self.immunity_location = self.immunity_positions[idx]
        
    def draw_powers(self):
        if self.isPowerUp_active:
            x,y = self.powerUp_location
            image(self.powerUp_img, x, y)
        
        if self.isPowerDown_active:
            x,y = self.powerDown_location
            image(self.powerDown_img, x, y)
        
        if self.isImmunity_active:
            x,y = self.immunity_location
            image(self.immunity_img, x, y)
        
