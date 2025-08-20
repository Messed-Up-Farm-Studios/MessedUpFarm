import random

class MapOutline:
    def __init__(self, outline_boundary: int = 18):
        # Constants
        self.OUTLINE_BOUNDARY = outline_boundary
        self.FOUNTAIN_ROOM_SIZE = random.randint(3, 7)
        self.CENTER = self.OUTLINE_BOUNDARY // 2

        self.map = [[" " for _ in range(self.OUTLINE_BOUNDARY)] for _ in range(self.OUTLINE_BOUNDARY)]
        self.map[self.CENTER][self.CENTER] = "F"

    def draw_map(self):
        self.draw_fountain()
        biomes = ["S", "D", "T", "C"]
        self.draw_biome()

        self.print_map()

    def draw_fountain(self):
        """Draw the fountain room and print the map."""

        def extend_vertically(row_index):
            for col_index in range((self.FOUNTAIN_ROOM_SIZE // 2) + 1):
                self.map[self.CENTER + col_index][row_index] = "F"
                self.map[self.CENTER - col_index][row_index] = "F"

        def extend_horizontally():
            for row_index in range((self.FOUNTAIN_ROOM_SIZE // 2) + 1):
                self.map[self.CENTER][self.CENTER + row_index] = "F"
                self.map[self.CENTER][self.CENTER - row_index] = "F"
                extend_vertically(self.CENTER + row_index)
                extend_vertically(self.CENTER - row_index)

        extend_horizontally()   

    def print_map(self):
        # Print map
        for row in self.map:
            print("".join(row))


        


    



outline = MapOutline()
outline.draw_map()
