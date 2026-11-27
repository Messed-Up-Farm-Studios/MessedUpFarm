from Direction import Direction
from Player import Player
from Biome import Biome


class Tile:
    def __init__(self, biome: Biome, col: int, row: int):
        self.biome = biome
        # this is to know for whom the tile should appear on the map
        # tiles will only appear once visited, except for the main fountain
        self.playersVisited: list[Player] = []
        # location of tile on the map
        self.col = col
        self.row = row
        # idk why the None = None part is here
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

