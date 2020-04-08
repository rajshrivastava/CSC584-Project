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
        self.loadData()
        
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
            
    def drawStaticObstacles(self):
        for obstacle in self.obstacles:
            beginShape()
            for x, y in obstacle:
                vertex(x, y)
            endShape(CLOSE)
    
    def drawStaticKeys(self):
        # playerImg = loadShape('images/player.svg')
        # playerImg.scale(0.07)
        # shape(playerImg, self.playerPosition[0], self.playerPosition[1])
    
        # guard1Img = loadShape('images/guard1.svg')
        # guard1Img.scale(0.07)
        # shape(guard1Img, self.guard1Position[0], self.guard1Position[1])
    
        # guard2Img = loadShape('images/guard2.svg')
        # guard2Img.scale(0.06)
        # shape(guard1Img, self.guard2Position[0], self.guard2Position[1])
    
        safehouseImg = loadShape('images/safehouse.svg')
        safehouseImg.scale(0.1)
        shape(safehouseImg, self.safehousePosition[0], self.safehousePosition[1])
    
        treasureImg = loadShape('images/treasure.svg')
        treasureImg.scale(0.1)
        shape(treasureImg, self.treasurePosition[0], self.treasurePosition[1])
        
        dead1Img = loadShape('images/dead1.svg')
        dead1Img.scale(0.5)
        shape(dead1Img, self.dead1Position[0], self.dead1Position[1])
        
        dead2Img = loadShape('images/dead2.svg')
        dead2Img.scale(0.5)
        shape(dead2Img, self.dead2Position[0], self.dead2Position[1])
        
        dead3Img = loadShape('images/dead3.svg')
        dead3Img.scale(0.5)
        shape(dead3Img, self.dead3Position[0], self.dead3Position[1])
        
        dead4Img = loadShape('images/dead4.svg')
        dead4Img.scale(0.5)
        shape(dead1Img, self.dead4Position[0], self.dead4Position[1])
        
        normal1Img = loadShape('images/normal1.svg')
        normal1Img.scale(0.1)
        shape(normal1Img, self.normal1Position[0], self.normal1Position[1])
        
        normal2Img = loadShape('images/normal2.svg')
        normal2Img.scale(0.1)
        shape(normal2Img, self.normal2Position[0], self.normal2Position[1])
        
    def drawMap(self):
        self.drawStaticObstacles()
        self.drawStaticKeys()
   
