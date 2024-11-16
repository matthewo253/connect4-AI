#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    def  __init__(self, checker):
        ''' creates a set of variables'''
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        ''' returns the piece that the player is playing as '''
        if(self.checker == 'X'):
            return 'Player X'
        else:
            return 'Player O'
    
    def opponent_checker(self):
        ''' returns what the opponent checker piece is '''
        if(self.checker == 'X'):
            return 'O'
        else:
            return 'X'
    def next_move(self, b):
        ''' returns if you can put a piece in the column that the player inputs
        if so it adds to the number of moves that the player has committed
        '''
        move = eval(input('Enter a column: '))
        while True:
            if(b.can_add_to(move) == True):
                self.num_moves += 1
                return move
                break
            else:
                print('Try again!')
                move = eval(input('Enter a column: '))