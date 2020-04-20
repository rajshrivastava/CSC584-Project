import json
from module import *
from algorithm import *
from Map import *

world_object = None
player_object = None
bot_objects = None
botMovement_object = None
map_obj = None
oneTimeChangeOnTreasureStolen = True
game_over = False

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
    r,g,b = 255,150,0
    fill(r,g,b)
    stroke(r,g,b)
    background(255, 255, 255)
    global player_object
    global botMovement_object
    global map_obj
    global oneTimeChangeOnTreasureStolen
    global game_over
    
    map_obj.drawMap()
    
    if(game_over):
        return
    
    player_object.draw_player()
    
    # check if treasure stolen
    if(map_obj.checkTreasureStolen(player_object.current_location)):
        
        if(oneTimeChangeOnTreasureStolen):
            # do all the one time changes like changing speeds, power-ups etc.
            print("TREASURE STOLEN!")
            botMovement_object.treasureStolen = True
            player_object.img = loadShape('images/player_steal.svg')
            player_object.img.scale(0.07)
            oneTimeChangeOnTreasureStolen = False
        
        # do all the things when the game is in treasure stolen state
        # like powerups, decision-making etc.
        pass
    
    # check collision between player and obstacles
    if(map_obj.playerCollisionOccur(player_object.current_location, botMovement_object.bots)):
        print("PLAYER COLLIDED. GAME OVER!")
        # show something on screen as well
        game_over=True
        return
    
    # botMovement_object.move_bots(player_object.current_location)
    botMovement_object.move_bots(player_object.current_location, map_obj.treasurePosition, map_obj.safehousePosition)

    
    
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
