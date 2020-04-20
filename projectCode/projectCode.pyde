import json
from module import *
from algorithm import *
from Map import *
from decision_making import *
from power_up import *

world_object = None
player_object = None
bot_objects = None
botMovement_object = None
map_obj = None
oneTimeChangeOnTreasureStolen = True
game_over = False
decision_obj = None
power_object = None

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
    global decision_obj
    
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
    
    fileData = readJson('action.json')
    actionJson = loadJson(fileData)
    decision_obj = decisions(map_obj, botMovement_object, player_object, actionJson)
    
    #powerUp
    power_obj = Power(worldJson)
    
    
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
    global decision_obj
    
    map_obj.drawMap()
    
    player_object.draw_player()
    if not game_over:      
        # check if treasure stolen
        if(map_obj.checkTreasureStolen(player_object.current_location)):
            
            if(oneTimeChangeOnTreasureStolen):
                # do all the one time changes like changing speeds, power-ups etc.
                print("TREASURE STOLEN!")
                botMovement_object.treasureStolen = True
                decision_obj.treasure_intact = False
                player_object.img = map_obj.player_stealImg
                oneTimeChangeOnTreasureStolen = False
                for bot_obj in bot_objects:
                    bot_obj.speed += 1
            
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
        #botMovement_object.move_bots(player_object.current_location, map_obj.treasurePosition, map_obj.safehousePosition)
        # bot movementt added to decision control class
        decision_obj.game_control()
        
    else:     #game over
        gameOverImg = loadImage('images/gameOver.png')
        #gameOverImg.scale(0.07)
        image(gameOverImg, 100,100)
        
def keyPressed():
    if game_over:
        return
    global player_object
    if keyPressed and key == CODED:
        new_location = player_object.current_location
        x=player_object.speed
        #if keyCode == UP and get(new_location[0], new_location[1]-x) == -1:
        if keyCode == UP:
            player_object.update_current_location([new_location[0], new_location[1]-x])
            
        #elif keyCode == DOWN and get(new_location[0], new_location[1]+x) == -1:
        elif keyCode == DOWN:
            player_object.update_current_location([new_location[0], new_location[1]+x])
            
        #elif keyCode == LEFT and get(new_location[0]-x, new_location[1]) == -1:
        elif keyCode == LEFT:
            player_object.update_current_location([new_location[0]-x, new_location[1]])
            
        #elif keyCode == RIGHT and get(new_location[0] + x, new_location[1]) == -1:
        elif keyCode == RIGHT:
            player_object.update_current_location([new_location[0]+x, new_location[1]])
