class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players 
        self.coach = coach 
        self.points = 0 

    def add_player(self,new_player):
        self.players.append(new_player)

    def team_players(self):
        return len(self.players)

    def has_player(self, name):
        for player in self.players:
            if player == name:
                return True
        return False 

    def play_game(self, game_won):
        if game_won == True:
            self.points +=  3

    
            
   

Team.coach = "John Candy"



