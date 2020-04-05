import json
from module import *
from algorithm import *

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

world_object = None
player_object = None
bot_objects = None
botMovement_object = None


finalPath = []
final_x = 25
final_y = 290
knightLocation = []
counter = 0
maxCount = 0

def setup():
    """
    setup function for the game
    """
    global world_object
    # global pathFinderObject
    global knightLocation
    global player_object
    global bot_objects
    global botMovement_object
    size(640, 480)
    fileData = readJson('map.json')
    worldJson = loadJson(fileData)
    world_object = World(worldJson)
    player_object = Player(worldJson["player_start"])
    bot_count = len(worldJson["bot_start"])
    bot_objects = list()
    for i in range(bot_count):
        bot_objects.append(Bot(worldJson["bot_start"][i]))
    botMovement_object = BotMovement(bot_objects, bot_count)
    gameSize = world_object.set_background_color()
    world_object.draw_all_obstacles()
    # world_object.draw_bot()
    knightLocation = worldJson["bot_start"]

def draw():
    """
    draw function for the game
    """
    global knightLocation
    global counter
    global maxCount
    global player_object
    global bot_objects
    global botMovement_object
    if finalPath and counter < maxCount:
        knightLocation = list(finalPath[counter])
        world_object.world_json["bot_start"] = knightLocation
        counter += 1
    player_object.draw_player()
    botMovement_object.move_bots()
    
def keyPressed():
    global player_object
    if keyPressed and key == CODED:
        new_location = player_object.current_location
        if keyCode == UP:
            player_object.update_current_location([new_location[0], new_location[1]-1])
        elif keyCode == DOWN:
            player_object.update_current_location([new_location[0], new_location[1]+1])
        elif keyCode == LEFT:
            player_object.update_current_location([new_location[0]-1, new_location[1]])
        elif keyCode == RIGHT:
            player_object.update_current_location([new_location[0]+1, new_location[1]])

def mousePressed():
    """
    Function that gets triggered on mouse press
    """
    global pathFinderObject
    start_location = tuple(bot_objects[0].current_location)
    goal_location = (mouseX, mouseY)
    path = pathFindDijkstra(pathFinderObject, start_location, goal_location)
    if not path:
        print("inaccessible")
        return
    bot_objects[0].path_traversing = path
    bot_objects[0].path_index = 0
    bot_objects[0].max_path_index = len(path)
