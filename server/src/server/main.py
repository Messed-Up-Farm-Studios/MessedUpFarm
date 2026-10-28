import uuid

from fastapi import FastAPI

from server.daos.AuthDAO import AuthDAO
from server.daos.PlayerDAO import PlayerDAO
from server.handlers.PlayerHandler import PlayerHandler
from server.server import Server
from server.services.PlayerService import PlayerService
from server.websocket.ConnectionManager import ConnectionManager
from server.websocket.WebSocketHandler import WebSocketHandler


def create_server() -> Server:
    playerDAO = PlayerDAO()
    authDAO = AuthDAO()

    def authGenerator():
        return uuid.uuid4()

    playerService = PlayerService(playerDAO, authDAO, authGenerator)
    playerHandler = PlayerHandler(playerService)

    connectionManager = ConnectionManager()
    webSocketHandler = WebSocketHandler(connectionManager)

    return Server(webSocketHandler, playerHandler)


def create_app(server: Server) -> FastAPI:
    app = FastAPI()
    server.register_routes(app)
    return app


server = create_server()
app = create_app(server)
