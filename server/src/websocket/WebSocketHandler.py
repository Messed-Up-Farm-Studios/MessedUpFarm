import json

from fastapi import WebSocket, WebSocketDisconnect

from server.src.websocket.ConnectionManager import ConnectionManager


class WebSocketHandler:
    def __init__(self):
        self.manager = ConnectionManager()

    async def handle(self, ws: WebSocket, gameID: str):
        await self.manager.connect(gameID, ws)

        try:
            while True:
                data = await ws.receive_text()

                await self.on_message(gameID, data, ws)
        except WebSocketDisconnect:
            self.manager.disconnect(ws)

    async def on_message(self, gameID: str, data: str, ws: WebSocket):
        msg = json.loads(data)

        if msg["type"] == "move":
            pass
        elif msg["type"] == "chat":
            await self.manager.broadcast_to_game(gameID, msg, ws)
