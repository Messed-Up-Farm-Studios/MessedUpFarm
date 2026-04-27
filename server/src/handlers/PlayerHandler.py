from server.src.services.PlayerService import PlayerService
from shared.model.requests.RegisterRequest import RegisterRequest
from shared.model.responses.RegisterResponse import RegisterResponse
from shared.model.result.RegisterResult import RegisterResult


class PlayerHandler:
    def __init__(self):
        self.playerService = PlayerService()

    def handle_registration(self, registerRequest: RegisterRequest):
        result: RegisterResult = self.playerService.register(registerRequest)
        return RegisterResponse(username=result.username, authToken=result.authToken)
