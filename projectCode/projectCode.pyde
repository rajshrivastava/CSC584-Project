import json
from module import World
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

world = None
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
    global world
    global pathFinderObject
    global knightLocation
    size(640, 480)
    pathFinderObject = pathFinder(640, 480)
    fileData = readJson('map.json')
    worldJson = loadJson(fileData)
    world = World(worldJson)
    gameSize = world.set_background_color()
    world.draw_all_obstacles()
    world.draw_bot()
    knightLocation = worldJson["bot_start"]
    
def keyPressed():
    if keyPressed and key == CODED:
        if keyCode == UP:
            world.world_json["player_start"][1] -= 1
        elif keyCode == DOWN:
            world.world_json["player_start"][1] += 1
        elif keyCode == LEFT:
            world.world_json["player_start"][0] -= 1
        elif keyCode == RIGHT:
            world.world_json["player_start"][0] += 1

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

def draw():
    """
    draw function for the game
    """
    global knightLocation
    global counter
    global maxCount
    if finalPath and counter < maxCount:
        knightLocation = list(finalPath[counter])
        world.world_json["bot_start"] = knightLocation
        counter += 1
    world.draw_bot()
    world.draw_player()
