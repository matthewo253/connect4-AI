#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)

    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p, b):
        ''' processes a move that the player made and checks if the player
        wins, ties, or has no win which returns false
        '''
        print(str(p) + 's turn')
    #    print('yeet')
     #   print('naw')
        b.add_checker(p.checker, p.next_move(b))
        print()
        print(b)
        if(b.is_win_for(p.checker) == True):
            print(str(p.checker) + ' wins in ' + str(p.num_moves) + ' moves \n Congratulations')
            return True
        elif(b.is_full() == True):
            print('It''s a Tie!')
            return True
        else:
            return False

class RandomPlayer(Player):      
    ''' creates a new class that inherits from player and changes the
    next_move that is inherited form the player into making a random move
    with the slots that are not full
    '''
    def next_move(self, b):
        openNum = []
        for i in range(b.width):
            if(b.slots[0][i] == ' '):
                openNum += [i]
        randNum = random.choice(openNum)
        return randNum
                