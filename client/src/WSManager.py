import asyncio
from queue import Queue


class WSManager:
    def __init__(self):
        self.client = None
        self.queue = Queue()

    def send_ws(self, data: dict):

        if self.client is None:
            return

        asyncio.run_coroutine_threadsafe(self.client.send(data), self.client.loop)


wsManager = WSManager()
