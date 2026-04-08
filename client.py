import asyncio
import websockets

async def run():
    uri = "ws://127.0.0.1:8000/ws"

    async with websockets.connect(uri) as ws:
        await ws.send("hello server")

        msg = await ws.recv()
        print(msg)

asyncio.run(run())