import numpy as np

# setting up the values for the gri
ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(value):
    return np.random.choice(vals, value*value, p=[0.2, 0.8]).reshape(value, value)

def get_new_board(size):
    grid = np.array([])
    grid = randomGrid(value=size)
    return grid

def get_new_board_1_D(size):
    grid = np.zeros((size * size))
    index = 0
    if size % 2 == 0:
        index = int(size / 2)
    else: 
        index = int(size / 2 + 1)

    grid[index] = 255
    return grid.reshape(size, size)