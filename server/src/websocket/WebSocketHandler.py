import json

from fastapi import WebSocket, WebSocketDisconnect

from server.src.websocket.ConnectionManager import ConnectionManager


class WebSocketHandler:
    def __init__(self) -> None:
        self.manager = ConnectionManager()

    async def handle(self, ws: WebSocket, gameID: str) -> None:
        await self.manager.connect(gameID, ws)

        try:
            while True:
                data = await ws.receive_text()

                await self.on_message(gameID, data, ws)
        except WebSocketDisconnect:
            pass
        finally:
            self.manager.disconnect(ws)

    async def on_message(self, gameID: str, data: str, ws: WebSocket) -> None:
        try:
            msg = json.loads(data)
        except json.JSONDecodeError:
            await ws.close()
            return

        if not isinstance(msg, dict):
            await ws.close()
            return

        msg_type = msg.get("type")

        if msg_type == "move":
            pass
        elif msg_type == "chat":
            await self.manager.broadcast_to_game(gameID, msg, ws)
        else:
            await ws.close()
