"""Conways' game of life.

Also see https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""

from open_files import open_file


class Game:
    """The class for Conway's game of life."""

    def __init__(self):
        """Ititialize the game of life."""
        self.old_grid = self.generate_grid()
        self.new_grid = self.old_grid.copy()
        

    def generate_grid(self, cols = 30, rows = 60):
        """Generate a grid."""
        return [["-" for _ in range(cols)] for _ in range(rows)]

    def print_grid(self, grid):
        """Print out the grid."""
        for row in grid:
            for elem in row:
                print(elem, end=" ")
            print()

    def play(self):
        """Play the game."""
        while True:
            self.new = self.play_current_state(self.new) # Applies the rules of the game on the new board.
            self.old = self.new.copy()
            self.print_grid(self.new)
            input()

    def play_current_state(self, grid):
        """Run though the game and apply the rules.
            
        The rules:
            1) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            2) Any live cell with two or three live neighbours lives on to the next generation.
            3) Any live cell with more than three live neighbours dies, as if by overpopulation.
            4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        for row in grid:
            for elem in row:
                neighbors = self.calculate_neighbors(grid, x = grid.index(row), y = row.index(elem))
                sum = 0 # used to calculate if we have MORE than 3 neighbors or LESS than 2...
                
                for neighbor in neighbors:
                    if neighbor == '-': # if it is dead
                        sum += 0
                    else:
                        sum += 1
                
                if sum < 2 or sum > 3: # It dies of 'under-population' OR 'over-population'
                    elem = '-'

    def calculate_neighbors(self, grid, x, y):
        """Calculate the neighbors."""
        neighbors = []
        try:
            # Work in progress...
            # if self.isedge(grid, x, y):
            #     return neighbors    

            for i in range(-1, 2): # From the top to bottem
                for j in range(-1, 2): # From the left to right
                    neighbors.append(grid[i][j])
        except IndexError:
            return neighbors

        return neighbors

    def apply_spots(self, grid, *coords):
        """Apply easch spot in a grid to a coord."""
        for arg in coords:
            grid[arg[1]][arg[0]] = 'O' # For an "x/y" system
        return grid


game = Game()
game.apply_spots(open_file('starts/design.in'))
game.print_grid(game.old_grid)