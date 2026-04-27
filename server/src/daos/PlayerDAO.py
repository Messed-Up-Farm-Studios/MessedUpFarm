class PlayerDAO:
    def __init__(self):
        self.players = []

    def register(self, username: str):
        self.players.append(username)
