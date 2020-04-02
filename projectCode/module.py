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

class Player():
    """
    Class to account location for the player
    """
    def __init__(self, start_location):
        """
        Function that initializes the class with
        given start location
        """
        self.last_location = None
        self.current_location = start_location

    def update_current_location(self, new_location):
        """
        Function that updates the new_location and also
        stores the previous one for reference
        """
        self.last_location = self.current_location
        self.current_location = new_location

    def draw_player(self):
        """
        Function that draws the player object at new location
        and removes the old player object from previous location
        """
        stroke(255)
        if self.last_location:
            fill(255)
            circle(self.last_location[0], self.last_location[1], 10)
        fill(0)
        circle(self.current_location[0], self.current_location[1], 10)

class Bot():
    """
    Class to account location for the all
    the bot locations
    """
    def __init__(self, start_location):
        """
        Function that initializes the class with
        given start locations
        """
        self.bot_count = None
        self.last_location = list()
        self.current_location = start_location

    def update_location(self, new_location):
        """
        Function that updates the new_location and also
        stores the previous one for reference for all
        the bots
        """
        for i in range(self.bot_count):
            self.last_location[i] = self.current_location[i]
            self.current_location[i] = new_location[i]

    def draw_bot(self):
        """
        Function that draws all the bot objects at new
        location and removes all the old bot objects from
        previous location
        """
        for i in range(len(self.bot_count)):
            stroke(255)
            if self.last_location:
                fill(255)
                circle(self.last_location[i][0], self.last_location[i][1], 10)
            fill(0)
            circle(self.current_location[i][0], self.current_location[i][1], 10)
