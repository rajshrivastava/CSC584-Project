import random
from algorithm import *

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
        last_location: list containing location
        current_location: list containing location
        """
        self.last_location = None
        self.current_location = start_location
        self.speed = 2
        self.img = loadShape('images/player.svg')
        self.img.scale(0.07)
    
    def update_current_location(self, new_location):
        """
        Function that updates the new_location and also
        stores the previous one for reference
        """
        self.last_location = self.current_location
        self.current_location = new_location

    def draw_player_old(self):
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
        
    def draw_player(self):
        shape(self.img, self.current_location[0], self.current_location[1])

class Bot():
    """
    Class to account location for the all
    the bot locations
    """
    def __init__(self, start_location):
        """
        Function that initializes the class with
        given start locations
        last_location : list containing locations
        current_location: list containing locations
        """
        self.last_location = None
        self.current_location = start_location
        self.path_traversing = None
        self.path_index = None
        self.is_moving = False
        self.destination = None
        self.speed = 2
        self.img = loadShape('images/guard1.svg')
        self.img.scale(0.07)
        
        
    def update_location(self, new_location):
        """
        Function that updates the new_location and also
        stores the previous one for reference for all
        the bots
        """
        self.last_location = self.current_location
        self.current_location = new_location

    def move_bot(self):
        if self.path_traversing and self.path_index < self.max_path_index:
            self.update_location(list(self.path_traversing[self.path_index]))
            self.path_index += self.speed
        else:
            self.is_moving = False

    def draw_bot_old(self):
        """
        Function that draws all the bot objects at new
        location and removes all the old bot objects from
        previous location
        """
        stroke(255)
        if self.last_location:
            fill(255)
            circle(self.last_location[0], self.last_location[1], 10)
        fill(100)
        circle(self.current_location[0], self.current_location[1], 10)
    
    def draw_bot(self):
        shape(self.img, self.current_location[0], self.current_location[1])
        
class BotMovement():
    """
    Class to make sure all the bots are in moving state
    """
    def __init__(self, bot_objects, count):
        """
        Initializes class with all the bot objects
        and bots count
        """
        self.bots = bot_objects
        self.bot_count = count
        self.current_state = 'random'
        self.available_state = ['random', 'guard', 'chase']
        self.pathFinderObject = pathFinder(width, height)
    
    def find_bot_path(self, bot_object):
        """
        Function to move the bot
        """
        start_location = tuple(bot_object.current_location)
        goal_location = tuple(bot_object.destination)
        #path = self.pathFinderObject.pathFindRecursiveBestFirstSearch(start_location, goal_location)
        path = self.pathFinderObject.pathFindAstar(start_location, goal_location)
        if not path:
            print("inaccessible")
            return
        bot_object.path_traversing = path
        bot_object.path_index = 0
        bot_object.max_path_index = len(path)
        bot_object.is_moving = True
            
    def move_bots(self):
        """
        Function that moves all the bots acroos
        the canvas
        """
        if self.current_state == 'random':
            for i in range(self.bot_count):
                if self.bots[i].is_moving:
                    self.bots[i].move_bot()
                    self.bots[i].draw_bot()
                else:
                    self.bots[i].destination = [random.randrange(0,640), random.randrange(0, 480)]
                    # print self.bots[i].destination
                    self.find_bot_path(self.bots[i])
        elif self.current_state == 'guard':
            """
            to make all the bots guard the treasure
            """
            pass
        elif self.current_state == 'chase':
            """
            to make all the bots chase the player bot
            once in the vicinity/range
            """
            pass
