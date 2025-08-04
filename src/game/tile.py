from enum import Enum

class Player(Enum):
    COW = "Cow"
    PIG = "Pig"

class Biome(Enum):
    S = "Swamp"
    O = "Orchard"
    G = "Garden"
    D = "Dirt"
    T = "Trees"

class Direction(Enum):
    N = "North"
    E = "East"
    S = "South"
    W = "West"

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

    def linkTile(self, direction: Direction, tileToConnect: Tile):
        if direction == Direction.N:
            self.n = tileToConnect
        elif direction == Direction.E:
            self.e = tileToConnect
        elif direction == Direction.S:
            self.s = tileToConnect
        elif direction == Direction.W:
            self.w = tileToConnect
