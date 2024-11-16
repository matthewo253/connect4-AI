#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, init_height, init_width):
        ''' creates a set of variables '''
        self.height = init_height
        self.width = init_width
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        s += '-' * (self.width * 2 + 1)
        s += '\n'
        for i in range(self.width):
            s += ' ' + str(i % 10)
        s += '\n'
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = self.height - 1
        for i in range(self.width * self.height):
            if(self.slots[row][col] == ' '):
                self.slots[row][col] = checker
                break
            else:
                row -= 1
            
        

    
    ### add your reset method here ###
    def reset(self):
        ''' resets the checker board and creates a blank board '''
        col = self.width - 1
        row = self.height - 1
        for i in range(self.width * self.height):
            if(self.slots[row][col] != ' '):
                self.slots[row][col] = ' '
            else:
                row -= 1
                if(row == 0):
                    self.slots[row][col] = ' '
                    col -= 1
                    row = self.height - 1
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        ''' determines if you can add a chip to the column the player inputs
        returns true if so
        '''
        row = self.height - 1
        for i in range(self.height * self.width):
            if(self.slots[row][col] == ' '):
                return True
            else:
                row -= 1
        return False
    
    def is_full(self):
        ''' determines if the board is full of pieces, returns true if so
        and false if not
        '''
        row = self.height - 1
        col = self.width - 1
        for i in range(self.height * self.width):
            if(self.slots[row][col] == ' '):
                return False
            else:
                row -= 1
                if(row == 0):
                    col -= 1
                    row = self.height - 1
        return True
    
    
    def remove_checker(self, col):
        ''' removes a checker off the board '''
        row = 0
        for i in range(self.height * self.width):
            if(self.slots[row][col] != ' '):
                self.slots[row][col] = ' '
                break
            else:
                if(row == self.height - 1):
                    break
                row += 1
                
    def is_win_for(self, checker):
        """ determines if you the checker you select has a win or not
        returning true if so and false if not
        """
        assert(checker == 'X' or checker == 'O')
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                        self.slots[row][col + 2] == checker and \
                            self.slots[row][col + 3] == checker:
                                return True
        for row in range(self.height - 3):
            for col in range(self.width):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                        self.slots[row + 2][col] == checker and \
                            self.slots[row + 3][col] == checker:
                                return True
        for row in range(self.height - 3):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                        self.slots[row + 2][col + 2] == checker and \
                            self.slots[row + 3][col + 3] == checker:
                                return True
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                        self.slots[row - 2][col + 2] == checker and \
                            self.slots[row - 3][col + 3] == checker:
                                return True
    # if we make it here, there were no horizontal wins
        return False
            