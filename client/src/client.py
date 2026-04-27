import asyncio

import requests
import websockets

from shared.model.requests.RegisterRequest import RegisterRequest


async def run():
    uri = "ws://127.0.0.1:8000/ws"

    async with websockets.connect(uri) as ws:
        await ws.send("hello server")

        msg = await ws.recv()
        print(msg)


asyncio.run(run())

BASE_URL = "http://127.0.0.1:8000"


def send_request(method, path="/", data=None, params=None, headers=None):
    url = BASE_URL + path

    method = method.upper()

    if method == "GET":
        response = requests.get(url, params=params, headers=headers)
    elif method == "POST":
        response = requests.post(url, json=data, headers=headers)
    elif method == "PUT":
        response = requests.put(url, json=data, headers=headers)
    elif method == "PATCH":
        response = requests.patch(url, json=data, headers=headers)
    elif method == "DELETE":
        response = requests.delete(url, headers=headers)
    else:
        raise ValueError(f"Unsupported method: {method}")

    print(response.json())


# Good Post Request"
req = RegisterRequest(username="jimmy", age=22, password="admin123")
send_request("POST", "/register/player", data=req.model_dump())

# Bad Post Request
data = {"username": 2344, "age": 22, "password": "admin123"}
send_request("POST", "/register/player", data=data)
