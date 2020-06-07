"""The redo."""
import open_files
import time
import random
import os

COLS = 100
ROWS = 100

def makeGrid(cols: int, rows: int) -> list:
    """Make an empty grid."""
    return [[0 for _ in range(cols)] for _ in range(rows)]

def pprint(grid: list) -> None:
    """Pretty print the grid."""
    for row in grid:
        for elem in row:
            if elem == 1:
                print('o', end=' ')
            else:
                print('-', end=' ')
        print()

def play() -> None:
    """Play the game!."""
    grid = makeGrid(COLS, ROWS)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = random.randint(1, 10)

    new = grid.copy()

    # The main loop.
    while True:
        for i in range(len(new)):
            for j in range(len(new[i])):
                new[i][j] = calcSpot(new, i, j)

        grid = new.copy()
        # pprint(new)
        time.sleep(1)


def calcSpot(grid, x, y):
    """Calculate the current spot's 'life'."""
    end = grid.copy()
    currentState = end[x][y]

    neighbors = countNeighbors(end, x, y)

    if currentState == 0 and neighbors == 3:
        end[x][y] = 1

    elif currentState == 1 and (neighbors < 2 or neighbors > 3):
        end[x][y] = 0
    
    else:
        pass # We don't need to do anything

    return end[x][y]


def countNeighbors(grid: list, x: int, y: int) -> int:
     """Count the current neighbors."""
     sum = 0
     for i in range(-1, 2):
          for j in range(-1, 2):
                col = (x + i + COLS) % COLS
                row = (y + j + ROWS) % ROWS
                if grid[col][row] == 0:
                    sum -= 1
                else:
                    sum += grid[col][row]

     sum -= grid[x][y] # Disinclude ourselves...
     return sum

def apply_spots(grid, *coords):
    """Apply easch spot in a grid to a coord."""
    for arg in coords:
        grid[arg[0]][arg[1]] = 0 # For an "x/y" system
    return grid

play()