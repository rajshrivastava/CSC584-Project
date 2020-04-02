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
bot_object = None
pathFinderObject = None
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
    global pathFinderObject
    global knightLocation
    global player_object
    size(640, 480)
    pathFinderObject = pathFinder(640, 480)
    fileData = readJson('map.json')
    worldJson = loadJson(fileData)
    world_object = World(worldJson)
    player_object = Player(worldJson["player_start"])
    bot_object = Bot(worldJson["bot_start"])
    gameSize = world_object.set_background_color()
    world_object.draw_all_obstacles()
    world_object.draw_bot()
    knightLocation = worldJson["bot_start"]

def draw():
    """
    draw function for the game
    """
    global knightLocation
    global counter
    global maxCount
    global player_object
    if finalPath and counter < maxCount:
        knightLocation = list(finalPath[counter])
        world_object.world_json["bot_start"] = knightLocation
        counter += 1
    world_object.draw_bot()
    player_object.draw_player()
    
def keyPressed():
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
    # global final_x
    # global final_y
    global knightLocation
    global finalPath
    global maxCount
    global counter
    print knightLocation
    finalPath = pathFindDijkstra(pathFinderObject, (knightLocation[0],knightLocation[1]), (mouseX, mouseY))
    if not finalPath:
        print("inaccessible")
        return
    counter = 0
    maxCount = len(finalPath)
    knightLocation[0] = mouseX
    knightLocation[1] = mouseY
