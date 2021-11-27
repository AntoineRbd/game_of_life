from src.rules.basic_rules import basic_rule_test, get_neighbour_bot, get_neighbour_center, get_neighbour_top
from src.board.create_board import get_new_board

size = 50

grid = get_new_board(size=size)

ON = 255
OFF = 0

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
        neighbours = 0

        for k in neighbours_state:
            if k == ON:
                neighbours += 1
                
        if cell == ON and (neighbours < 2) or (neighbours > 3):
            cell_should_die = (i, j)
            
        if cell == ON and (neighbours == 2 or neighbours == 3):
            cell_should_survive = (i, j)
            
        if cell == OFF and neighbours == 3:
            cell_should_born = (i, j)

def test_rule_game_of_life_die():
    new_grid = basic_rule_test(grid, size)
    assert new_grid[cell_should_die[0]][cell_should_die[1]] == OFF

def test_rule_game_of_life_survive():
    new_grid = basic_rule_test(grid, size)
    assert new_grid[cell_should_survive[0]][cell_should_survive[1]] == ON

def test_rule_game_of_life_die_born():
    new_grid = basic_rule_test(grid, size)
    assert new_grid[cell_should_born[0]][cell_should_born[1]] == ON