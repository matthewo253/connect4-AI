#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    
    def __init__(self, checker, tiebreak, lookahead):
        """ inherits from variable and initalizes a set of variables
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        self.num_moves = 0
        
    def __repr__(self):
        ''' prints the turn of the player and the tiebreak and lookahead 
        for the player
        '''
        return 'Player ' + str(self.checker) + ' ('+ str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        ''' gives the index of the max score the player has depending
        on the tiebreak
        '''
        maxScores = max(scores)
        newList = []
        for i in range(len(scores)):
            if(scores[i] == maxScores):
                newList += [i] 
        if(self.tiebreak == 'LEFT'):
            return newList[0]
        elif(self.tiebreak == 'RIGHT'):
            return newList[-1]
        else:
            return random.choice(newList)
        
        
    def scores_for(self, b):
        ''' determines in which columns that player x or player o has a win,
        loss, or tie in 
        '''
        scores = [50] * b.width
        for c in range(b.width):
                if(b.can_add_to(c) == False):
                    scores[c] = -1
                elif(b.is_win_for(self.checker) == True):
                    scores[c] = 100
                elif(b.is_win_for(self.opponent_checker()) == True):
                    scores[c] = 0
                else:
                    if(self.lookahead > 0):
                        b.add_checker(self.checker, c)
                        op = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                        if(max(op.scores_for(b)) == 0):
                            scores[c] = 100
                        elif(max(op.scores_for(b)) == 100):
                            scores[c] = 0
                        b.remove_checker(c)
        return scores
    
    def next_move(self, b):
        ''' determines the best move for the player '''
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))
        
                
                    
                
        