import json
from module import World

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
def setup():
    """
    setup function for the game
    """
    global world
    size(640, 480)
    fileData = readJson('map.json')
    worldJson = loadJson(fileData)
    world = World(worldJson)
    gameSize = world.set_background_color()
    world.draw_all_obstacles()
    world.draw_bot()
    
def draw():
    world.draw_bot()
