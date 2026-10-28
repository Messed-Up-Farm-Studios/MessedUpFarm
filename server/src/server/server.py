from fastapi import FastAPI, WebSocket, status

from model.requests.RegisterRequest import RegisterRequest
from model.responses.RegisterResponse import RegisterResponse
from server.handlers.PlayerHandler import PlayerHandler
from server.websocket.WebSocketHandler import WebSocketHandler


class Server:
    def __init__(
        self, webSocketHandler: WebSocketHandler, playerHandler: PlayerHandler
    ) -> None:
        self.webSocketHandler = webSocketHandler
        self.playerHandler = playerHandler

    def register_routes(self, app: FastAPI):

        @app.websocket("/ws/{gameID}")
        async def websocket_endpoint(ws: WebSocket, gameID: str) -> None:
            await self.webSocketHandler.handle(ws, gameID)

        @app.get("/health")
        def health_check() -> dict[str, str]:
            return {"status": "ok"}

        @app.post(
            "/register/player",
            status_code=status.HTTP_201_CREATED,
            tags=["Player", "Create"],
        )
        def register_player(registerRequest: RegisterRequest) -> RegisterResponse:
            return self.playerHandler.handle_registration(registerRequest)
