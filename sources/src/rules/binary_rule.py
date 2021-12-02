ON = 255
OFF = 0

index = 1

def get_neighbour(grid, size, i, j):
    return {
        "left": grid[(i - 1) % size][(j - 1) % size], 
        "center": grid[(i - 1) % size][j],
        "right": grid[(i - 1) % size][(j + 1) % size]
    }

def convert_to_color(digit):
    if digit == '0':
        return OFF
    if digit == '1':
        return ON

def next_gen(neighbour, rule):
    if neighbour['left'] == OFF and neighbour['center'] == OFF and neighbour['right'] == OFF : # 000
        return convert_to_color(rule[7])
    if neighbour['left'] == OFF and neighbour['center'] == OFF and neighbour['right'] == ON : # 001
        return convert_to_color(rule[6])
    if neighbour['left'] == OFF and neighbour['center'] == ON and neighbour['right'] == OFF : # 010
        return convert_to_color(rule[5])
    if neighbour['left'] == OFF and neighbour['center'] == ON and neighbour['right'] == ON : # 011
        return convert_to_color(rule[4])
    if neighbour['left'] == ON and neighbour['center'] == OFF and neighbour['right'] == OFF : # 100
        return convert_to_color(rule[3])
    if neighbour['left'] == ON and neighbour['center'] == OFF and neighbour['right'] == ON : # 101
        return convert_to_color(rule[2])
    if neighbour['left'] == ON and neighbour['center'] == ON and neighbour['right'] == OFF : # 110
        return convert_to_color(rule[1])
    if neighbour['left'] == ON and neighbour['center'] == ON and neighbour['right'] == ON : # 111
        return convert_to_color(rule[0])


def play_binary_rule(frameNum, grid, size, img, rule):
    newGrid = grid.copy()
    global index
    for j in range(size):
        neighbour = get_neighbour(grid, size, index % size, j)
        newGrid[index % size][j] = next_gen(neighbour=neighbour, rule=str(rule))

    index += 1
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,