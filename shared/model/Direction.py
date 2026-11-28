from enum import Enum

class Direction(Enum):
    N = "North"
    E = "East"
    S = "South"
    W = "West"

    @staticmethod
    def get_changes(dir: "Direction"):
        # returns changes to x and y for a given direction
        if dir == Direction.N:
            xchange = 0
            ychange = -1
        if dir == Direction.S:
            xchange = 0
            ychange = 1
        if dir == Direction.E:
            xchange = 1
            ychange = 0
        if dir == Direction.W:
            xchange = -1
            ychange = 0
        return xchange, ychange

if __name__ == "__main__":
    d = Direction.N
    if d == Direction.N:
        print('equal')