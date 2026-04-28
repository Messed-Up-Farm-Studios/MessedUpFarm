import asyncio
from queue import Queue

from client.src.WSClient import WSClient


class WSManager:
    def __init__(self) -> None:
        self.client: WSClient | None = None
        self.queue: Queue = Queue()

    def send_ws(self, data: dict) -> None:

        if self.client is None:
            return

        asyncio.run_coroutine_threadsafe(self.client.send(data), self.client.loop)


wsManager = WSManager()
