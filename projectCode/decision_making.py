class decisions():
    def __init__(self):
        self.game_states = ["defend_q1", "defend_q2", "defend_q3", "defend_q4", "attack_q1", "attack_q2", "attack_q3", "attack_q4"]
        self.player_position = None
        self.game_state_index = None
        self.current_game_state = None
        self.treasure_intact = True
    
    def determine_state(self):
        if self.treasure_intact:
            #we are in one of the defend states
            if self.player_position[0] > 0 and self.player_position[1] < width/2 and self.player_position[1] > 0 and self.player_postion[1] < height/2:
                self.current_game_state = "defend_q2"
            if self.player_position[0] > width/2 and self.player_position[1] < width and self.player_position[1] > 0 and self.player_postion[1] < height/2:
                self.current_game_state = "defend_q1"
            if self.player_position[0] > 0 and self.player_position[1] < width/2 and self.player_position[1] > height/2 and self.player_postion[1] < height:
                self.current_game_state = "defend_q3"
            if self.player_position[0] > width/2 and self.player_position[1] < width and self.player_position[1] > height/2 and self.player_postion[1] < height:
                self.current_game_state = "defend_q4"
        else:
            #we are in one of the attack states
            if self.player_position[0] > 0 and self.player_position[1] < width/2 and self.player_position[1] > 0 and self.player_postion[1] < height/2:
                self.current_game_state = "attack_q2"
            if self.player_position[0] > width/2 and self.player_position[1] < width and self.player_position[1] > 0 and self.player_postion[1] < height/2:
                self.current_game_state = "attack_q1"
            if self.player_position[0] > 0 and self.player_position[1] < width/2 and self.player_position[1] > height/2 and self.player_postion[1] < height:
                self.current_game_state = "attack_q3"
            if self.player_position[0] > width/2 and self.player_position[1] < width and self.player_position[1] > height/2 and self.player_postion[1] < height:
                self.current_game_state = "attack_q4"
