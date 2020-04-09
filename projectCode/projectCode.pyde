import json
from module import *
from algorithm import *
from Map import *

world_object = None
player_object = None
bot_objects = None
botMovement_object = None
map_obj = None

def readJson(filename):
    """
    Reads the file and returns file content
    filename: name of the file to be read
    return: file content in string
    """
    with open(filename) as fp:
        data = fp.read()
    return data

def loadJson(data):
    """
    Loads the file content in to json object
    data: data to be loaded into json object
    return: json object of data
    """
    try:
        data = json.loads(data)
        return data
    except Exception as e:
        print "Error loading json: {}".format(str(e))

def setup():
    """
    setup function for the game
    """
    global world_object
    global player_object
    global bot_objects
    global botMovement_object
    global map_obj
    size(641, 481)
    
    fileData = readJson('map.json')
    worldJson = loadJson(fileData)
    # world_object = World(worldJson)
    player_object = Player(worldJson["player_start"])
    bot_count = len(worldJson["bot_start"])
    bot_objects = list()
    for i in range(bot_count):
        bot_objects.append(Bot(worldJson["bot_start"][i]))
    botMovement_object = BotMovement(bot_objects, bot_count)
    # world_object.set_background_color()
    #world_object.draw_all_obstacles()
    map_obj = Map(worldJson)
    

def draw():
    """
    draw function for the game
    """
    fill(0)
    background(255, 255, 255)
    map_obj.drawMap()   
    global player_object
    global botMovement_object
    player_object.draw_player()
    botMovement_object.move_bots()
    
    
def keyPressed():
    global player_object
    if keyPressed and key == CODED:
        new_location = player_object.current_location
        x=player_object.speed
        if keyCode == UP:
            player_object.update_current_location([new_location[0], new_location[1]-x])
        elif keyCode == DOWN:
            player_object.update_current_location([new_location[0], new_location[1]+x])
        elif keyCode == LEFT:
            player_object.update_current_location([new_location[0]-x, new_location[1]])
        elif keyCode == RIGHT:
            player_object.update_current_location([new_location[0]+x, new_location[1]])
