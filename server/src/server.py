from fastapi import FastAPI, WebSocket, status

from server.src.handlers.PlayerHandler import PlayerHandler
from server.src.websocket.WebSocketHandler import WebSocketHandler
from shared.model.requests.RegisterRequest import RegisterRequest
from shared.model.responses.RegisterResponse import RegisterResponse


class Server:
    def __init__(self) -> None:
        self.webSocketHandler = WebSocketHandler()
        self.playerHandler = PlayerHandler()

    def register_routes(self, app: FastAPI):

        @app.websocket("/ws/{gameID}")
        async def websocket_endpoint(ws: WebSocket, gameID: str) -> None:
            await self.webSocketHandler.handle(ws, gameID)

        @app.get("/health ")
        def health_check() -> dict[str, str]:
            return {"status": "ok"}

        @app.post(
            "/register/player",
            status_code=status.HTTP_201_CREATED,
            tags=["Player", "Create"],
        )
        def register_player(registerRequest: RegisterRequest) -> RegisterResponse:
            return self.playerHandler.handle_registration(registerRequest)


app = FastAPI()

server = Server()
server.register_routes(app)
