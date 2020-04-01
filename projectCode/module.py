class World():
    """
    Class for handling the map 
    functions and variables
    """
    def __init__(self, worldJson):
        """
        Initializes all the variables
        that are part of the class Map
        """
        self.world_json = worldJson
        
    def get_canvas_size(self):
        """
        Function that returns the size of canvas from Json
        return: array having width and height
        """
        return world_json["canvas_size"]
    
    def set_background_color(self):
        """
        Sets the background color
        """
        background(self.world_json["canvas_color"])
        
    def draw_all_obstacles(self):
        """
        Function that creates all the obstacles on
        the map
        """
        obstaclesJson = self.world_json["obstacles"]
        for obstacle in obstaclesJson.keys():
            tempObstacleJson = obstaclesJson[obstacle]
            self.draw_obstacle_utility(tempObstacleJson, obstacle)
        
    def draw_obstacle_utility(self, locationList, obstacle):
        """
        Function that creates the obstacle on
        the map
        loationList: dictionary of all the locations
                     where the obstacles are to be drawn
        obstacle: name of the obstacle that is being drawn
        """
        totalVertices = len(locationList)
        fill(0)
        stroke(0)
        strokeWeight(2)
        beginShape()
        for i in range(0,totalVertices):
            location = locationList[i]
            vertex(location[0],location[1])
        endShape(CLOSE)
        
    def draw_bot(self):
        """
        Function draws the bot on the map
        """
        circle(self.world_json["bot_start"][0], self.world_json["bot_start"][1], 10)
        
    def draw_player(self):
        """
        Function draws the bot on the map
        """
        circle(self.world_json["player_start"][0], self.world_json["player_start"][1], 10)
