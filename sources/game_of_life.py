from optparse import OptionParser

def start_game(size=50) :
    # generate_board = get_new_board()
    pass

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