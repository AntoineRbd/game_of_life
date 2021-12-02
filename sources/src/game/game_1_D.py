from matplotlib import pyplot as plt
import matplotlib.animation as animation

from src.board.create_board import get_new_board_1_D
from src.rules.binary_rule import play_binary_rule

def play_1_D(rule, size):
    grid = get_new_board_1_D(size)
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    anim = animation.FuncAnimation(fig, play_binary_rule, fargs=(grid, size, img, rule, ), frames=10, interval=50, save_count=50)
    anim = anim
    plt.show()