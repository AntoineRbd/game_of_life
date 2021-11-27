from optparse import OptionParser

from src.game.game_of_life_game import play_game_of_life

def start_game(size=50, rule='game_of_life') :
    if rule == 'game_of_life' :
        play_game_of_life(size)

    else:
        print("Rule invalid")
        return -1


if __name__ == "__main__":
    parser = OptionParser()
    usage = "usage: %prog [options] arg1 arg2"

    parser.add_option("-s", "--size", type="int",
                    help="Numeric value of the board size",
                    dest="size")
    
    parser.add_option("-r", "--rule", type="int",
                      help="Numeric value of rule number, default is game of life",
                      dest="rule")

    options, arguments = parser.parse_args()

    if options.size and options.rule :
        print("start game with size " + str(options.size) + " and rule n°" + str(options.rule))
        start_game(size=options.size, rule=options.rule)

    elif options.size:
        print ("start game with size " + str(options.size))
        start_game(size=options.size)

    elif options.rule :
        print("Start game with rule n°" + str(options.rule))
        start_game(rule=options.rule)
        
    else :
        print ("start game without option")
        start_game()