from matplotlib import pyplot as plt
import matplotlib.animation as animation

from src.board.create_board import get_new_board
from src.rules.basic_rules import basic_rule

def play_game_of_life(size):
    grid = get_new_board(size)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, basic_rule, fargs=(grid, size, img, ), frames=10, interval=50, save_count=50)
    plt.show()