ON = 255
OFF = 0

def get_neighbour_top(grid, size, i, j):
    return {
            "neighbour_top_left" : grid[(i - 1) % size][(j - 1) % size],
            "neighbour_top_center" : grid[(i - 1) % size][j],
            "neighbour_top_right" : grid[(i - 1)  % size][(j + 1) % size]
            }

def get_neighbour_center(grid, size, i, j):
    return {
            "neighbour_center_left" : grid[i][(j - 1) % size],
            "neighbour_center_right" : grid[i][(j + 1) % size]
            }

def get_neighbour_bot(grid, size, i, j):
    return {
            "neighbour_bot_left" : grid[(i + 1) % size][(j - 1) % size],
            "neighbour_bot_center" : grid[(i + 1) % size][j],
            "neighbour_bot_right" : grid[(i + 1) % size][(j + 1) % size]
            }

def next_gen(neighbours_state, cell):
    neighbours = 0

    for k in neighbours_state:
        if k == ON:
            neighbours += 1

    if cell == ON:
        if (neighbours < 2) or (neighbours > 3) :
            return OFF #cell die

        if neighbours == 2 or neighbours == 3:
            return ON

    if cell == OFF and neighbours == 3:
        return ON

    return OFF


def basic_rule(frameNum, grid, size, img):
    newGrid = grid.copy()

    for i in range(size):
        for j in range(size):
            neighbour_top = get_neighbour_top(grid, size, i, j)
            neighbour_center = get_neighbour_center(grid, size, i, j)
            neighbour_bot = get_neighbour_bot(grid, size, i, j)

            cell = grid[i][j]

            neighbours_state = [
                neighbour_top["neighbour_top_left"],
                neighbour_top["neighbour_top_center"],
                neighbour_top["neighbour_top_right"],
                neighbour_center["neighbour_center_left"],
                neighbour_center["neighbour_center_right"],
                neighbour_bot["neighbour_bot_left"],
                neighbour_bot["neighbour_bot_center"],
                neighbour_bot["neighbour_bot_right"],
            ]

            newGrid[i][j] = next_gen(neighbours_state=neighbours_state, cell=cell)

    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def basic_rule_test(grid, size):
    newGrid = grid.copy()
    
    for i in range(size):
        for j in range(size):
            neighbour_top = get_neighbour_top(grid, size, i, j)
            neighbour_center = get_neighbour_center(grid, size, i, j)
            neighbour_bot = get_neighbour_bot(grid, size, i, j)

            cell = grid[i][j]

            neighbours_state = [
                neighbour_top["neighbour_top_left"],
                neighbour_top["neighbour_top_center"],
                neighbour_top["neighbour_top_right"],
                neighbour_center["neighbour_center_left"],
                neighbour_center["neighbour_center_right"],
                neighbour_bot["neighbour_bot_left"],
                neighbour_bot["neighbour_bot_center"],
                neighbour_bot["neighbour_bot_right"],
            ]

            newGrid[i][j] = nex_gen(neighbours_state=neighbours_state, cell=cell)

    return newGrid