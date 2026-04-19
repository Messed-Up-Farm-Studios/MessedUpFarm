from server.src.daos.PlayerDAO import PlayerDAO


class PlayerHandler:
    def __init__(self):
        self.playerDAO: PlayerDAO = PlayerDAO()

    def create_player(self, player):
        #
        self.playerDAO.add_player(player)
        response = {"msg": "player created"}
        return response
    
    def list_players():
        pass