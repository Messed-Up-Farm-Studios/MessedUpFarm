from model.requests.RegisterRequest import RegisterRequest
from model.responses.RegisterResponse import RegisterResponse
from model.result.RegisterResult import RegisterResult
from server.services.PlayerService import PlayerService


class PlayerHandler:
    def __init__(self, playerService: PlayerService) -> None:
        self.playerService = playerService

    def handle_registration(self, registerRequest: RegisterRequest) -> RegisterResponse:
        result: RegisterResult = self.playerService.register(registerRequest)
        response: RegisterResponse = RegisterResponse(**result.model_dump())
        return response
