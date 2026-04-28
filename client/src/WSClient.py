import json

import websockets
from websockets.asyncio.client import ClientConnection


class WSClient:
    def __init__(self, loop) -> None:
        self.ws: ClientConnection | None = None
        self.loop = loop

    async def connect(self) -> None:
        from client.src.WSManager import wsManager
        gameID = 34543  # TEMP gameID
        uri = f"ws://127.0.0.1:8000/ws/{gameID}"

        async with websockets.connect(uri) as ws:
            self.ws = ws
            wsManager.client = self

            while True:
                msg = await ws.recv()

                try:
                    data = json.loads(msg)
                except json.JSONDecodeError:
                    data = msg

                wsManager.queue.put(data)

    async def send(self, data: dict) -> None:
        if self.ws:
            await self.ws.send(json.dumps(data))
