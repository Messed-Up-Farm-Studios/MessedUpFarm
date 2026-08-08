from collections import defaultdict

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self) -> None:
        self.games: dict[str, set[WebSocket]] = defaultdict(set)
        self.player_game: dict[WebSocket, str] = {}

    async def connect(self, gameID: str, ws: WebSocket):
        await ws.accept()
        self.games[gameID].add(ws)
        self.player_game[ws] = gameID

    def disconnect(self, ws: WebSocket):
        gameID = self.player_game.get(ws)

        if gameID:
            self.games[gameID].discard(ws)

            if len(self.games[gameID]) == 0:
                del self.games[gameID]

            del self.player_game[ws]

    async def broadcast_all(self, gameID: str, message: dict) -> None:
        for ws in self.games.get(gameID, []):
            await ws.send_json(message)

    async def broadcast_to_game(
        self, gameID: str, message: dict, exclude: WebSocket | None = None
    ) -> None:
        for ws in self.games.get(gameID, set()):
            if ws == exclude:
                continue
            await ws.send_json(message)
