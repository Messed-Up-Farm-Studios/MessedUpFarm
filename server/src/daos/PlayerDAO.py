players = []


class PlayerDAO:
    def __init__(self):
        pass

    def add_player(self, player):
        players.append(player.name)
        return
    
    def list_players(self):
        return players