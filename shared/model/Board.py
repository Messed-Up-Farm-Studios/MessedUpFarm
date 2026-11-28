from Biome import Biome
import random as r
from Direction import Direction

# right now:
# this makes a board, odd width and odd height
# the board is split along a center, with each biome in a quadrant
# check biomes for understanding the print from running this file
# each spot in the array is really a 2x2 of that biome tile

# eventually:
# each biome has a set of 2x2 of tiles that live inside it
# these 4 tiles make a 'room' and rooms have their own layout
# rooms assemble tiles to make different open / closed areas with walls
# we can randomly make one of the tiles in a room empty, so that there is just a thick wall where it was
# call me to explain this better

class Board:
    def __init__(self, w_range_min, w_range_max, h_range_min, h_range_max):
        biomes = ([Biome.T, Biome.G, Biome.O, Biome.D, Biome.S])
        r.shuffle(biomes)
        biomes.remove(r.choice(biomes))
        self.biomes = biomes

        # this is how far in we want the fountain, should not be larger than midpoint of small side
        f_tol = min([h_range_min//2, w_range_min//2]) 

        self.width = r.randint(w_range_min, w_range_max)
        self.height = r.randint(h_range_min, h_range_max)

        # fill with none, will be given biomes as we make the board
        self.array = [[None for x in range(self.width)] for y in range(self.height)]

        # x, y cord of where fountain will go
        self.fountain_point = (r.randint(f_tol, self.width - f_tol), r.randint(f_tol, self.height - f_tol))

        # get on with it
        self.make_board()

    def make_board(self):
        dirs = [Direction.N, Direction.E, Direction.S, Direction.W]
        biomes = self.biomes[:]

        for dir in dirs:
            biome = biomes.pop()
            self.make_biome(dir, biome)

        self.install_fountain()
        self.add_walls()


    def add_walls(self):
        # north
        for x in range(self.width):
            self.set(x, 0, Biome.W)
        # east
        for y in range(self.height):
            self.set(self.width - 1, y, Biome.W)
        # south
        for x in range(self.width):
            self.set(x, self.height-1, Biome.W)
        # west
        for y in range(self.height):
            self.set(0, y, Biome.W)
        

    def install_fountain(self):
        fpx, fpy = self.fountain_point

        # left side
        self.set(fpx - 1, fpy - 1, Biome.F)
        self.set(fpx - 1, fpy, Biome.F)
        self.set(fpx - 1, fpy + 1, Biome.F)
        # middle
        self.set(fpx, fpy - 1, Biome.F)
        self.set(fpx, fpy, Biome.C)
        self.set(fpx, fpy + 1, Biome.F)
        # right
        self.set(fpx + 1, fpy - 1, Biome.F)
        self.set(fpx + 1, fpy, Biome.F)
        self.set(fpx + 1, fpy + 1, Biome.F)
        

    def make_biome(self, dir: Direction, biome: Biome):
        fpx, fpy = self.fountain_point
        if dir == Direction.N:
            bpx, bpy = fpx + 0, fpy - 1
            self.make_biome_line(Direction.E, Direction.N, biome, bpx, bpy)
        elif dir == Direction.E:
            bpx, bpy = fpx + 1, fpy + 0
            self.make_biome_line(Direction.S, Direction.E, biome, bpx, bpy)
        elif dir == Direction.S:
            bpx, bpy = fpx + 0, fpy + 1
            self.make_biome_line(Direction.W, Direction.S, biome, bpx, bpy)
        elif dir == Direction.W:
            bpx, bpy = fpx - 1, fpy + 0
            self.make_biome_line(Direction.N, Direction.W, biome, bpx, bpy)
    

    def make_biome_line(self, pdir: Direction, sdir: Direction, biome: Biome, px, py):
        # find out changes that happen along pdir and sdir
        pxchange, pychange = Direction.get_changes(pdir)
        sxchange, sychange = Direction.get_changes(sdir)

        # loop along primary direction, px and py are primary references
        while self.in_bounds(px, py):
            self.set(px, py, biome)

            # loop along secondary direction using sx and sy
            sx, sy = px + sxchange, py + sychange
            while self.in_bounds(sx, sy):
                self.set(sx, sy, biome)
                sy += sychange
                sx += sxchange
    
            px += pxchange
            py += pychange


    def print_board(self):
        board_str = ''
        for row in self.array:
            row_str = ''
            for item in row:
                if item != None:
                    row_str += f'{item.name}'
                else:
                    row_str += '-'
            board_str += row_str
            board_str += '\n'
        print(board_str)


    def in_bounds(self, x, y):
        if 0 <= x <= self.width - 1 and 0 <= y <= self.height - 1:
            return True
        return False


    def set(self, x, y, val):
        if not self.in_bounds(x, y):
            raise IndexError
        self.array[y][x] = val


    def get(self, x, y):
        if not self.in_bounds(x, y):
            raise IndexError
        return self.array[y][x]
        

if __name__ == "__main__":
    buddy_board = Board(9, 21, 9, 21)
    buddy_board.print_board()
