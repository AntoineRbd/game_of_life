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