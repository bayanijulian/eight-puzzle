import random

class Puzzle():
    def __init__(self):
        self.grid_size = 3
        self.grid = []
        self._init_grid()

    def _init_grid(self):
        tiles = list(range(self.grid_size**2))
        random.shuffle(tiles)
        for i in range(self.grid_size):
            row = []
            for i in range(self.grid_size):
                tile = tiles.pop()
                row.append(tile)
            self.grid.append(row)
    
    def print_grid(self):
        print("  " + "-"*((self.grid_size**2)+self.grid_size-1))
        for row in self.grid:
            row_str = ""
            for col in row:
                col_str = " | " + str(col)
                if col == 0:
                    col_str = " | " + " "
                row_str += col_str

            row_str += " | "
            print(row_str)
            print("  " + "-"*((self.grid_size**2)+self.grid_size-1))


puzzle = Puzzle()
puzzle.print_grid()