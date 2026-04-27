import uuid

from server.src.daos.AuthDAO import AuthDAO
from server.src.daos.PlayerDAO import PlayerDAO
from shared.model.requests.RegisterRequest import RegisterRequest
from shared.model.responses.RegisterResponse import RegisterResponse


class PlayerService:
    def __init__(self):
        self.playerDAO: PlayerDAO = PlayerDAO()
        self.authDAO: AuthDAO = AuthDAO()

    def register(self, registerRequest: RegisterRequest):
        username: str = registerRequest.username

        self.playerDAO.register(username)

        authToken = uuid.uuid4()

        self.authDAO.addAuthData(username, authToken)

        return RegisterResponse(username=username, authToken=authToken)
