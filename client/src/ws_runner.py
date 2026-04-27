import asyncio
import threading

from client.src.WSClient import WSClient


def start_ws():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    client = WSClient(loop)
    loop.run_until_complete(client.connect())


def start_ws_thread():
    thread = threading.Thread(target=start_ws, daemon=True)
    thread.start()
