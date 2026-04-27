import json

import websockets

from client.src.WSManager import wsManager


class WSClient:
    def __init__(self, loop):
        self.ws = None
        self.loop = loop

    async def connect(self):
        uri = "ws://127.0.0.1:8000/ws"

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

    async def send(self, data: dict):
        if self.ws:
            await self.ws.send(json.dumps(data))
