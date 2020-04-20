from heapq import *

class decisions():
    def __init__(self, map_obj, bot_movement_obj, player_obj, actionJson):
        self.game_states = ["defend_q1", "defend_q2", "defend_q3", "defend_q4", "attack_q1", "attack_q2", "attack_q3", "attack_q4"]
        self.player_position = None
        self.game_state_index = None
        self.current_game_state = None
        self.state_change_flag = False
        self.treasure_intact = True
        self.map_obj = map_obj
        self.game_over = False
        self.bot_movement_obj = bot_movement_obj
        self.player_obj = player_obj
        self.actionJson = actionJson
    
    def determine_state(self):
        new_state = None
        if self.treasure_intact:
            #we are in one of the defend states
            if self.player_position[0] > 0 and self.player_position[1] < width/2 and self.player_position[1] > 0 and self.player_position[1] < height/2:
                new_state = "defend_q2"
            if self.player_position[0] > width/2 and self.player_position[1] < width and self.player_position[1] > 0 and self.player_position[1] < height/2:
                new_state = "defend_q1"
            if self.player_position[0] > 0 and self.player_position[1] < width/2 and self.player_position[1] > height/2 and self.player_position[1] < height:
                new_state = "defend_q3"
            if self.player_position[0] > width/2 and self.player_position[1] < width and self.player_position[1] > height/2 and self.player_position[1] < height:
                new_state = "defend_q4"
        else:
            #we are in one of the attack states
            if self.player_position[0] > 0 and self.player_position[1] < width/2 and self.player_position[1] > 0 and self.player_position[1] < height/2:
                new_state = "attack_q2"
            if self.player_position[0] > width/2 and self.player_position[1] < width and self.player_position[1] > 0 and self.player_position[1] < height/2:
                new_state = "attack_q1"
            if self.player_position[0] > 0 and self.player_position[1] < width/2 and self.player_position[1] > height/2 and self.player_position[1] < height:
                new_state = "attack_q3"
            if self.player_position[0] > width/2 and self.player_position[1] < width and self.player_position[1] > height/2 and self.player_position[1] < height:
                new_state = "attack_q4"

        if new_state != self.current_game_state and new_state != None:
            self.current_game_state = new_state
            self.state_change_flag = True
            
    def simple_select_actions(self, action_dict):
        # print self.current_game_state
        actions_heap = []
        for temp_key in action_dict.keys():
            # print temp_key, action_dict[temp_key]
            heappush(actions_heap, (-1 * int(action_dict[temp_key]), temp_key))
            
        result_actions = list()
        for i in range(0,2):
            temp = heappop(actions_heap)
            # print temp[1].split(" ")[0]
            result_actions.append(temp[1].split(" ")[0])
        print result_actions

    def game_control(self):
        self.player_position = self.player_obj.current_location
        self.determine_state()
        if self.state_change_flag:
            #state has been changed perform new decision making
            new_actions = self.actionJson[self.current_game_state]
            # add logic here for finding order of actions
            
            #currently adding a hack here
            if self.current_game_state == "defend_q2":
                self.bot_movement_obj.bot_actions_decisions = self.simple_select_actions(self.actionJson[self.current_game_state])
                self.bot_movement_obj.bot_actions_locations = [self.map_obj.data["key_locations"]["treasure"], [0,0]]
            elif self.current_game_state == "defend_q1":
                self.bot_movement_obj.bot_actions_decisions = self.simple_select_actions(self.actionJson[self.current_game_state])
                self.bot_movement_obj.bot_actions_locations = [self.map_obj.data["key_locations"]["treasure"], [0,0]]
            elif self.current_game_state == "defend_q3":
                self.bot_movement_obj.bot_actions_decisions = self.simple_select_actions(self.actionJson[self.current_game_state])
                self.bot_movement_obj.bot_actions_locations = [self.map_obj.data["key_locations"]["treasure"], [0,0]]
            elif self.current_game_state == "defend_q4":
                self.bot_movement_obj.bot_actions_decisions = self.simple_select_actions(self.actionJson[self.current_game_state])
                self.bot_movement_obj.bot_actions_locations = [self.map_obj.data["key_locations"]["treasure"], self.map_obj.data["key_locations"]["treasure"]]
            elif self.current_game_state == "attack_q4":
                self.bot_movement_obj.bot_actions_decisions = self.simple_select_actions(self.actionJson[self.current_game_state])
                self.bot_movement_obj.bot_actions_locations = [[0,0], [0,0]]
            elif self.current_game_state == "attack_q3":
                self.bot_movement_obj.bot_actions_decisions = self.simple_select_actions(self.actionJson[self.current_game_state])
                self.bot_movement_obj.bot_actions_locations = [self.map_obj.data["key_locations"]["safe_house"], [0,0]]
            elif self.current_game_state == "attack_q1":
                self.bot_movement_obj.bot_actions_decisions = self.simple_select_actions(self.actionJson[self.current_game_state])
                self.bot_movement_obj.bot_actions_locations = [self.map_obj.data["key_locations"]["safe_house"], [0,0]]
            elif self.current_game_state == "attack_q2":
                self.bot_movement_obj.bot_actions_decisions = self.simple_select_actions(self.actionJson[self.current_game_state])
                self.bot_movement_obj.bot_actions_locations = [self.map_obj.data["key_locations"]["safe_house"], self.map_obj.data["key_locations"]["safe_house"]]
            self.state_change_flag = False
        else:
            #no need to perform new decision making
            self.bot_movement_obj.move_bots_decisions(self.player_obj.current_location, self.map_obj.treasurePosition, self.map_obj.safehousePosition)
