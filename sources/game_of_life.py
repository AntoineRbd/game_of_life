from optparse import OptionParser

from matplotlib import pyplot as plt

from src.board.create_board import get_new_board

def start_game(size=50) :
    new_board = get_new_board(size)
    
    fig, ax = plt.subplots()
    img = ax.imshow(new_board, interpolation='nearest')
    plt.show()


if __name__ == "__main__":
    parser = OptionParser()
    usage = "usage: %prog [options] arg1 arg2"

    parser.add_option("-s", "--size", type="int",
                    help="Numeric value of the board size",
                    dest="board_size")

    options, arguments = parser.parse_args()

    if options.board_size:
        print ("start game with size " + str(options.board_size))
        start_game(size=options.board_size)
        
    else :
        print ("start game without option")
        start_game()