import uuid
from collections.abc import Callable

from server.daos.AuthDAO import AuthDAO
from server.daos.PlayerDAO import PlayerDAO
from shared.model.requests.RegisterRequest import RegisterRequest
from shared.model.result.RegisterResult import RegisterResult


class PlayerService:
    def __init__(self, playerDAO: PlayerDAO, authDAO: AuthDAO, authGenerator: Callable[[], uuid.UUID]) -> None:
        self.playerDAO = playerDAO
        self.authDAO = authDAO
        self.authGenerator = authGenerator

    def register(self, registerRequest: RegisterRequest) -> RegisterResult:
        username: str = registerRequest.username

        self.playerDAO.register(username)

        authToken = self.authGenerator()

        self.authDAO.add_auth_data(username, authToken)

        return RegisterResult(username=username, authToken=authToken)
