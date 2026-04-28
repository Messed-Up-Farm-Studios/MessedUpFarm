import uuid

from server.src.daos.AuthDAO import AuthDAO
from server.src.daos.PlayerDAO import PlayerDAO
from shared.model.requests.RegisterRequest import RegisterRequest
from shared.model.result.RegisterResult import RegisterResult


class PlayerService:
    def __init__(self) -> None:
        self.playerDAO: PlayerDAO = PlayerDAO()
        self.authDAO: AuthDAO = AuthDAO()

    def register(self, registerRequest: RegisterRequest) -> RegisterResult:
        username: str = registerRequest.username

        self.playerDAO.register(username)

        authToken = uuid.uuid4()

        self.authDAO.add_auth_data(username, authToken)

        return RegisterResult(username=username, authToken=authToken)
