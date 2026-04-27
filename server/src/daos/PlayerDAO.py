class PlayerDAO:
    def __init__(self) -> None:
        self.players: list[str] = []

    def register(self, username: str) -> None:
        self.players.append(username)
