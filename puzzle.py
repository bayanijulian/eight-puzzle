import random

class Puzzle():
    def __init__(self):
        self.grid_size = 3
        self.grid = []
        self.empty_space_loc = (0,0)
        self._init_grid()

    def _init_grid(self):
        tiles = list(range(self.grid_size**2))
        random.shuffle(tiles)
        for y in range(self.grid_size):
            row = []
            for x in range(self.grid_size):
                tile = tiles.pop()
                if tile == 0:
                    self.empty_space_loc = (x, y)
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
        print(f'Empty space is at {self.empty_space_loc}')

puzzle = Puzzle()
puzzle.print_grid()