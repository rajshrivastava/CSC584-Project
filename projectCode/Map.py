import json
class Map:
    def __init__(self):
        self.playerPosition = None
        self.guard1Position = None
        self.guard2Position = None
        self.obstacles = []
        self.key_locations = []
        self.safehousePosition = None
        self.treasurePosition = None   
        self.dead1Position = None
        self.dead2Position = None
        self.dead3Position = None
        self.dead4Position = None
        self.normal1Position = None
        self.normal2Position = None
        self.fire_i = 0
        self.loadData()
        
    def loadImages(self): #called in loadData()
        self.fireImages = [loadImage('images/fire/fire0.gif'), loadImage('images/fire/fire1.gif'), loadImage('images/fire/fire2.gif'),loadImage('images/fire/fire3.gif')]
        for i in range(len(self.fireImages)):
            self.fireImages[i].resize(180, 120) 
            
        self.normal1 = loadImage('images/corona.png')
        self.normal1.resize(30,30)
        self.normal2 = loadImage('images/corona.png')
        self.normal2.resize(30,30)
        self.safehouseImg = loadImage('images/safehouse.png')
        self.safehouseImg.resize(100,100)
        
        self.treasureImg = loadImage('images/treasure.png')
        self.treasureImg.resize(100,100)
        
    def loadData(self):    
        with open('map.json', 'r') as json_file:
            data = json.load(json_file)  
       
        # self.playerPosition = tuple(data['player_start'])
        # self.guard1Position = tuple(data['guard1'])
        # self.guard2Position = tuple(data['guard2'])
        
        self.obstacles = data['obstacles'].values()
        
        #key locations
        self.safehousePosition = tuple(data['key_locations']['safe_house'])
        self.treasurePosition = tuple(data['key_locations']['treasure'])
        self.dead1Position = tuple(data['key_locations']['dead1'])
        self.dead2Position = tuple(data['key_locations']['dead2'])
        self.dead3Position = tuple(data['key_locations']['dead3'])
        self.dead4Position = tuple(data['key_locations']['dead4'])
        
        self.normal1Position = tuple(data['key_locations']['normal1'])
        self.normal2Position = tuple(data['key_locations']['normal2'])
        
        self.loadImages()
        
            
    def drawStaticObstacles(self):
        for obstacle in self.obstacles:
            beginShape()
            for x, y in obstacle:
                vertex(x, y)
            endShape(CLOSE)
    
    def drawStaticKeys(self):    
        image(self.safehouseImg, self.safehousePosition[0], self.safehousePosition[1], self.safehouseImg.height/2, self.safehouseImg.width/2)    
        image(self.treasureImg, self.treasurePosition[0], self.treasurePosition[1], self.treasureImg.height/2, self.treasureImg.width/2)
        
        image(self.normal1, self.normal1Position[0], self.normal1Position[1])
        image(self.normal2, self.normal2Position[0], self.normal2Position[1])
        pass
    
    def drawDynamicObstacles(self):
        self.fire_i = (self.fire_i + 1)%40
        fire = self.fireImages[self.fire_i//10]
        image(fire, self.dead1Position[0], self.dead1Position[1], fire.height/4, fire.width/4)
        image(fire, self.dead2Position[0], self.dead2Position[1], fire.height/4, fire.width/4)
        image(fire, self.dead3Position[0], self.dead3Position[1], fire.height/4, fire.width/4)
        image(fire, self.dead4Position[0], self.dead4Position[1], fire.height/4, fire.width/4)
        
    def drawMap(self):
        self.drawStaticObstacles()
        self.drawStaticKeys()
        self.drawDynamicObstacles()
    
        
