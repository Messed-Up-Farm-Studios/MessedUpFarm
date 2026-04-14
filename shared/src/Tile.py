from shared.src.Direction import Direction
from shared.src.Player import Player
from shared.src.Biome import Biome

class Tile:
    def __init__(self, biome: Biome, col: int, row: int):
        self.biome = biome
        self.playersVisited: list[Player] = []
        self.col = col
        self.row = row
        self.n: Tile | None = None
        self.e: Tile | None = None
        self.s: Tile | None = None
        self.w: Tile | None = None

    def playerVisits(self, player: Player):
        if Player not in self.playersVisited:
            self.playersVisited.append(player)

    def linkTile(self, direction: Direction, tileToConnect: str):
        if direction == Direction.N:
            self.n = tileToConnect
        elif direction == Direction.E:
            self.e = tileToConnect
        elif direction == Direction.S:
            self.s = tileToConnect
        elif direction == Direction.W:
            self.w = tileToConnect
