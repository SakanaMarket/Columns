## Project 5
## Columns Game Logic
## Ha Tran 53409673
## Lab 5 Eletriby, M.

from collections import namedtuple
import sys
import random

GameState = namedtuple('GameState',['board', 'row', 'column'])

VALID = 'STVWYXZ'
NONE = '   '


def generate_faller()->list:
    return ['F',random.randrange(1,7),random.choice(VALID),random.choice(VALID),random.choice(VALID)]

class board:

    def __init__(self):
        '''
        assigns information from a list of info into content pieces for the game
        '''
        try:
            self.row = 13
            self.column = 6
            self.board_type = 'EMPTY'
            self.Game_Over = False
            self.GameState = self.create_board() ## GameState
        except ValueError:
            pass

    def create_board(self):
        '''
        Creates the board, an empty board if user input is EMPTY
        or a board with existing tiles if user input is CONTENTS
        '''
        try:
            if self.board_type == 'EMPTY':
                self.GameState = self.empty_board()
                return self.GameState
        except ValueError:
            return
            
    def empty_board(self):
        '''
        creates a new board based of dimension specifications
        '''
        board = []
        for col in range(self.row):
            board.append([])
            for row in range(self.column):
                board[-1].append('   ')
        return GameState(board=board, row=self.row, column=self.column)


    def auto_fall_existing_board(self):
        '''
        Generates a board where existing tiles that have been given have already fallen
        '''
        try:
            safe_ticker = 50
            while safe_ticker != 0:
                for i in range(self.row):
                    for x in range(self.column):
                        if self.GameState.board[i][x] == NONE:
                            if i == 0:
                                pass

                                
                            else:         
                                self.GameState.board[i][x] = self.GameState.board[i-1][x]
                                self.GameState.board[i-1][x] = NONE
                safe_ticker-=1


            return self.GameState
        
        except IndexError:
            pass

    def check_existing_board(self):
        '''
        Checks for invalid tiles in an existing board
        '''
        for i in range(self.row):
            for x in range(self.column):
                if self.GameState.board[i][x] != NONE:
                    block = self.GameState.board[i][x]
                    mid = int(len(block)/2)
                    letter = block[mid]
                    if letter not in VALID:
                        raise InvalidBlockType
                    else:
                        pass

    def fall(self, fall: 'fall class'):
        '''
        The main falling mechanic that makes both the falling and landing block tiles
        '''
        try:
            if fall.num_rows_moved == 0:
                if self.GameState.board[0][fall.col-1] == NONE:
                    if self.GameState.board[fall.num_rows_moved+1][fall.col-1] != NONE:
                        self.GameState.board[fall.num_rows_moved][fall.col-1] = '|' + fall.gem3 + '|'
                        fall.num_rows_moved += 1
                        fall.land()
                    if not self._check_under_plus_one(fall):
                
                        if self.GameState.board[0][fall.col-1] == NONE:
                            self.GameState.board[0][fall.col-1] = '[' + fall.gem3 + ']'
                            fall.num_rows_moved+=1
                        else:
                            pass
                    if self._check_under(fall):
                        self._force_land(fall)
                else:
                    self._game_over()
            elif fall.num_rows_moved == 1:
                if self._check_under_plus_one(fall):
                    if fall.num_rows_moved-2>=0:
                        self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|' + fall.gem1 + '|'
                        self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|' + fall.gem2 + '|'
                        self.GameState.board[fall.num_rows_moved][fall.col-1] = '|' + fall.gem3 + '|'
                        fall.num_rows_moved += 1
                        fall.land()
                    else:
                        self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|' + fall.gem2 + '|'
                        self.GameState.board[fall.num_rows_moved][fall.col-1] = '|' + fall.gem3 + '|'
                        fall.num_rows_moved += 1
                        fall.land()
                elif not self._check_under_plus_one(fall):
                    self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '[' + fall.gem2 + ']'
                    self.GameState.board[fall.num_rows_moved][fall.col-1] = '[' + fall.gem3 + ']'
                    fall.num_rows_moved += 1

                if self._check_under(fall):
                    self._force_land(fall)
            elif fall.num_rows_moved == 2:
                if self._check_under_plus_one(fall):
                    self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|' + fall.gem1 + '|'
                    self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|' + fall.gem2 + '|'
                    self.GameState.board[fall.num_rows_moved][fall.col-1] = '|' + fall.gem3 + '|'
                    fall.num_rows_moved += 1
                    fall.land()
                elif not self._check_under_plus_one(fall):
                    self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '[' + fall.gem1 + ']'
                    self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '[' + fall.gem2 + ']'
                    self.GameState.board[fall.num_rows_moved][fall.col-1] = '[' + fall.gem3 + ']'
                    fall.num_rows_moved += 1
                if self._check_under(fall):
                    self._force_land(fall)
            elif fall.num_rows_moved+1 == self.row:
                if self._check_under(fall):
                    self.GameState.board[fall.num_rows_moved-4][fall.col-1] = NONE
                    self.GameState.board[fall.num_rows_moved-3][fall.col-1] = '|' + fall.gem1 + '|'
                    self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|' + fall.gem2 + '|'
                    self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|' + fall.gem3 + '|'
                    fall.num_rows_moved += 1
                    fall.land()
                else:
                    self.GameState.board[fall.num_rows_moved-3][fall.col-1] = NONE
                    self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|' + fall.gem1 + '|'
                    self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|' + fall.gem2 + '|'
                    self.GameState.board[fall.num_rows_moved][fall.col-1] = '|' + fall.gem3 + '|'
                    fall.num_rows_moved += 1
                    fall.land()
            elif self.row>fall.num_rows_moved>=3:
                if self._check_under_plus_one(fall):
                    if fall.num_rows_moved-4>=0:
                        self.GameState.board[fall.num_rows_moved-4][fall.col-1] = NONE
                    else:
                        pass
                    self.GameState.board[fall.num_rows_moved-3][fall.col-1] = NONE
                    self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|' + fall.gem1 + '|'
                    self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|' + fall.gem2 + '|'
                    self.GameState.board[fall.num_rows_moved][fall.col-1] = '|' + fall.gem3 + '|'
                    fall.num_rows_moved += 1
                    fall.land()
                elif not self._check_under_plus_one(fall):
                    self.GameState.board[fall.num_rows_moved-3][fall.col-1] = NONE
                    self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '[' + fall.gem1 + ']'
                    self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '[' + fall.gem2 + ']'
                    self.GameState.board[fall.num_rows_moved][fall.col-1] = '[' + fall.gem3 + ']'
                    fall.num_rows_moved += 1
                if self._check_under(fall):
                    self._force_land(fall)
            elif fall.num_rows_moved == self.row:
                if fall.num_rows_moved-4>=0:
                    self.GameState.board[fall.num_rows_moved-4][fall.col-1] = NONE
                else:
                    pass
                self.GameState.board[fall.num_rows_moved-4][fall.col-1] = NONE
                self.GameState.board[fall.num_rows_moved-3][fall.col-1] = '|' + fall.gem1 + '|'
                self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|' + fall.gem2 + '|'
                self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|' + fall.gem3 + '|'
                fall.land()
            else:
                pass
            if fall.landed:
                fall.freeze()
        finally:
            pass

    def _force_land(self, fall):
        '''
        Forces a faller to land.
        '''
        for i in range(self.row):
            for x in range(self.column):
                if '[' in self.GameState.board[i][x]:
                    self.GameState.board[i][x] = self.GameState.board[i][x].replace('[','|')
                    self.GameState.board[i][x]= self.GameState.board[i][x].replace(']','|')
        fall.land()

    def _check_under(self, fall: 'fall class'):
        '''
        returns True if something is under the last block, False otherwise
        '''
        for x in range(self.column):
            if fall.num_rows_moved == self.row:
                
                return True
            elif '[' in self.GameState.board[fall.num_rows_moved-1][x]:
                if self.GameState.board[fall.num_rows_moved][x] == NONE:
                    return False
                else:
                    return True

    def _check_under_plus_one(self, fall: 'fall class'):
        '''
        returns True if something is under the last block 1 tile over, False otherwise
        '''
        for x in range(self.column):
            if fall.num_rows_moved == self.row:
                
                return True
            elif '[' in self.GameState.board[fall.num_rows_moved-1][x]:
                if self.GameState.board[fall.num_rows_moved+1][x] == NONE:
                    return False
                else:
                    return True
                        
    def _erase(self, fall: 'fall class'):
        '''
        Creates blank tiles at the position of the existing faller.
        '''
        if fall.num_rows_moved-3>=0:
            self.GameState.board[fall.num_rows_moved-3][fall.col-1] = NONE
            self.GameState.board[fall.num_rows_moved-2][fall.col-1] = NONE
            self.GameState.board[fall.num_rows_moved-1][fall.col-1] = NONE
        elif fall.num_rows_moved-2>=0:
            self.GameState.board[fall.num_rows_moved-2][fall.col-1] = NONE
            self.GameState.board[fall.num_rows_moved-1][fall.col-1] = NONE
        elif fall.num_rows_moved-1>=0:
            self.GameState.board[fall.num_rows_moved-1][fall.col-1] = NONE
        else:
            pass

    def move_right(self, fall: 'fall class'):
        '''
        Moves a faller to the right, keeping it at the same number of rows moved down, but 1 column right.
        '''
        if fall.col<self.column:
            if self._require_free_right(fall):
                self._erase(fall)
                fall.num_rows_moved -= 1
                fall.col+=1
            else:
                fall.num_rows_moved -= 1
                self.GameState.board[fall.num_rows_moved][fall.col-1] = NONE
        else:
            fall.num_rows_moved -= 1
            self.GameState.board[fall.num_rows_moved][fall.col-1] = NONE


    def move_left(self, fall: 'fall class'):
        '''
        Moves a faller to the left, keeping it at the same number of rows moved down, but 1 column left.
        '''
        if fall.col>1:
            if self._require_free_left(fall):
                self._erase(fall)
                fall.num_rows_moved -= 1
                fall.col -= 1
            else:
                fall.num_rows_moved -= 1
                self.GameState.board[fall.num_rows_moved][fall.col-1] = NONE
        elif fall.col == 1:
            fall.num_rows_moved -= 1
            self.GameState.board[fall.num_rows_moved][fall.col-1] = NONE

    def _require_free_left(self, fall: 'class'):
        '''
        Checks if the left tile of the bottom faller is a blank tile.
        '''
        if self.GameState.board[fall.num_rows_moved-1][fall.col-2] == NONE:
            return True
        else:
            return False

    def _require_free_right(self, fall: 'class'):
        '''
        Checks if the right tile of the bottom faller is a blank tile.
        '''
        if self.GameState.board[fall.num_rows_moved-1][fall.col] == NONE:
            return True
        else:
            return False
            
    def last_right(self, fall: 'fall class'):
        '''
        initiates a right movement if the faller has landed.
        '''
        self._final_right(fall)
        self.freeze(fall)
        self.auto_fall_existing_board()
        print_board(self.GameState)

    def last_left(self, fall: 'fall class'):
        '''
        initiates a left movement if the faller has landed.
        '''
        self._final_left(fall)
        self.freeze(fall)
        self.auto_fall_existing_board()
        print_board(self.GameState)

    def _final_right(self, fall: 'fall class'):
        '''
        Shifts a landed faller to the right.
        '''
        if fall.col<self.column:
            if self._require_free_right(fall):
                fall.col+=1
                for i in range(self.row):
                    for x in range(self.column):
                        if '|' in self.GameState.board[i][x]:
                            if fall.num_rows_moved < 3:
                                print('stop')
                                if fall.num_rows_moved == 1:
                                    self.GameState.board[fall.num_rows_moved-1][fall.col-2] = NONE
                                else:
                                    self.GameState.board[fall.num_rows_moved-2][fall.col-2] = NONE
                                    self.GameState.board[fall.num_rows_moved-1][fall.col-2] = NONE
                                for z in range(self.row):
                                    if self.GameState.board[z][fall.col-1] != NONE:
                                        if self.GameState.board[z-1][fall.col-1] == NONE:
                                            if z-3>1:
                                                fall.num_rows_moved = z
                                                self.GameState.board[fall.num_rows_moved-4][fall.col-1] = NONE
                                                self.GameState.board[fall.num_rows_moved-3][fall.col-1] = '|'+fall.gem1+'|'
                                                self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|'+fall.gem2+'|'
                                                self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|'+fall.gem3+'|'
                                                return fall.num_rows_moved
                                            if 1>=(z-3)>=0:
                                                fall.num_rows_moved = z
                                                self.GameState.board[fall.num_rows_moved-3][fall.col-1] = '|'+fall.gem1+'|'
                                                self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|'+fall.gem2+'|'
                                                self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|'+fall.gem3+'|'
                                                return fall.num_rows_moved
                                            elif z-3==-1:
                                                fall.num_rows_moved = z
                                                self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|'+fall.gem2+'|'
                                                self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|'+fall.gem3+'|'
                                                return fall.num_rows_moved
                                            elif z-3==-2:
                                                fall.num_rows_moved = z
                                                self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|'+fall.gem3+'|'
                                                return fall.num_rows_moved
                                            else:
                                                self.GameState.board[fall.num_rows_moved-1][fall.col-2] == NONE
                                        elif self.GameState.board[z-1][fall.col-1] != NONE:
                                            pass 
                            else:
                                self.GameState.board[fall.num_rows_moved-3][fall.col-1] = '|'+fall.gem1+'|'
                                self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|'+fall.gem2+'|'
                                self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|'+fall.gem3+'|'
                                self.GameState.board[fall.num_rows_moved-3][fall.col-2] = NONE
                                self.GameState.board[fall.num_rows_moved-2][fall.col-2] = NONE
                                self.GameState.board[fall.num_rows_moved-1][fall.col-2] = NONE
                                return


    def _final_left(self, fall: 'fall class'):
        '''
        Shifts a landed faller to the left.
        '''
        if fall.col>1:
            if self._require_free_left(fall):
                fall.col -= 1
                for i in range(self.row):
                    for x in range(self.column):
                        if '|' in self.GameState.board[i][x]:
                            if fall.num_rows_moved < 3:
                                if fall.num_rows_moved == 1:
                                    self.GameState.board[fall.num_rows_moved-1][fall.col] = NONE
                                else:
                                    self.GameState.board[fall.num_rows_moved-2][fall.col] = NONE
                                    self.GameState.board[fall.num_rows_moved-1][fall.col] = NONE
                                for z in range(self.row):
                                    if self.GameState.board[z][fall.col-1] != NONE:
                                        if self.GameState.board[z-1][fall.col-1] == NONE:
                                            if z-3>1:
                                                fall.num_rows_moved = z
                                                self.GameState.board[fall.num_rows_moved-4][fall.col-1] = NONE
                                                self.GameState.board[fall.num_rows_moved-3][fall.col-1] = '|'+fall.gem1+'|'
                                                self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|'+fall.gem2+'|'
                                                self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|'+fall.gem3+'|'
                                                return fall.num_rows_moved
                                            if 1>=(z-3)>=0:
                                                fall.num_rows_moved = z
                                                self.GameState.board[fall.num_rows_moved-3][fall.col-1] = '|'+fall.gem1+'|'
                                                self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|'+fall.gem2+'|'
                                                self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|'+fall.gem3+'|'
                                                return fall.num_rows_moved
                                            elif z-3==-1:
                                                fall.num_rows_moved = z
                                                self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|'+fall.gem2+'|'
                                                self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|'+fall.gem3+'|'
                                                return fall.num_rows_moved
                                            elif z-3==-2:
                                                fall.num_rows_moved = z
                                                
                                                self.GameState.board[fall.num_rows_moved-1][fall.col] = '|'+fall.gem3+'|'
                                                return fall.num_rows_moved
                                            else:
                                                self.GameState.board[fall.num_rows_moved-1][fall.col-1] == NONE
                                        elif self.GameState.board[z-1][fall.col-1] != NONE:
                                            pass 
                            else:
                                self.GameState.board[fall.num_rows_moved-3][fall.col-1] = '|'+fall.gem1+'|'
                                self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|'+fall.gem2+'|'
                                self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|'+fall.gem3+'|'
                                self.GameState.board[fall.num_rows_moved-3][fall.col] = NONE
                                self.GameState.board[fall.num_rows_moved-2][fall.col] = NONE
                                self.GameState.board[fall.num_rows_moved-1][fall.col] = NONE
                                return
                                
            

                
    def _check_spill(self, fall: 'fall class'):
        '''
        checks if the number of rows passed is less than the minimum required to fall into the board,
        initiating a Game Over
        '''
        if fall.num_rows_moved<3:
            self._game_over()
        else:
            pass

    def freeze(self, fall: 'fall class'):
        '''
        freezes a block in place
        '''
        if fall.landed:
            for i in range(self.row):
                for x in range(self.column):
                    if '|' in self.GameState.board[i][x]:
        
                        if fall.num_rows_moved-3>=0:
                            self.GameState.board[fall.num_rows_moved-3][fall.col-1] = ' ' + fall.gem1 + ' '
                            self.GameState.board[fall.num_rows_moved-2][fall.col-1] = ' ' + fall.gem2 + ' '        
                            self.GameState.board[fall.num_rows_moved-1][fall.col-1] = ' ' + fall.gem3 + ' '
                        elif fall.num_rows_moved-2>=0:
                            self.GameState.board[fall.num_rows_moved-2][fall.col-1] = ' ' + fall.gem2 + ' '        
                            self.GameState.board[fall.num_rows_moved-1][fall.col-1] = ' ' + fall.gem3 + ' '
                        elif fall.num_rows_moved-1>=0:
                            self.GameState.board[fall.num_rows_moved-1][fall.col-1] = ' ' + fall.gem3 + ' '
                        elif fall.num_rows_moved == 0:
                            self.GameState.board[fall.num_rows_moved][fall.col-1] == ' ' + fall.gem3 + ' '
            self._check_spill(fall)
                


    def frozen(self, fall: 'fall class'):
        self.freeze(fall)

    def rotate_landed(self, fall: 'fall class'):
        '''
        rotates a landed block
        '''
        for i in range(self.row):
            for x in range(self.column):
                if '|' in self.GameState.board[i][x]:
                    if fall.num_rows_moved>=3:
                        self.GameState.board[fall.num_rows_moved-3][fall.col-1] = '|' + fall.gem1 + '|'
                        self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|' + fall.gem2 + '|'
                        self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|' + fall.gem3 + '|'
                    elif fall.num_rows_moved==2:
                        self.GameState.board[fall.num_rows_moved-2][fall.col-1] = '|' + fall.gem2 + '|'
                        self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|' + fall.gem3 + '|'
                    elif fall.num_rows_moved==1:
                        self.GameState.board[fall.num_rows_moved-1][fall.col-1] = '|' + fall.gem3 + '|'

    def rotater(self, fall: 'fall class'):
        '''
        rotates a falling block mid-fall
        '''
        self.GameState.board[fall.num_rows_moved-1][fall.col-1] = NONE
        fall.num_rows_moved -= 1
        fall.rotate()

    def last_rotate(self, fall: 'fall class')->None:
        '''
        rotates a block that has landed and freezes the block in place
        '''
        fall.rotate()
        self.rotate_landed(fall)
        self.freeze(fall)
        print_board(self.GameState)
         
    def horizontal_match(self):
        '''
        Checks for horizontal matches in the board and creating asterisk spaces if so
        '''
        delta = []
        for i in range(self.row):
            for x in range(self.column):
                if self.GameState.board[i][x] != NONE:
                    y = int(len(self.GameState.board[i][x])/2)
                    match = self.GameState.board[i][x]
                    mark = match[y]
                    if x == 0:
                        if self.GameState.board[i][x+1]== match and self.GameState.board[i][x+2] == match:
                            delta.append((mark,i,x))
                            delta.append((mark,i,x+1))
                            delta.append((mark,i,x+2))
                    elif x == self.column-1:
                        if self.GameState.board[i][x-1] == match and self.GameState.board[i][x-2] == match:
                            delta.append((mark,i,x))
                            delta.append((mark,i,x-1))
                            delta.append((mark,i,x-2))
                    else:
                        if self.GameState.board[i][x-1] == match and self.GameState.board[i][x+1] == match:
                            delta.append((mark,i,x))
                            delta.append((mark,i,x-1))
                            delta.append((mark,i,x+1))
        return delta
        
    def vertical_match(self):
        '''
        Checks for vertical matches in the board and creates a list of the positions of the matches
        '''
        delta = []
        for i in range(self.row):
            for x in range(self.column):
                if self.GameState.board[i][x] != NONE:
                    y = int(len(self.GameState.board[i][x])/2)
                    match = self.GameState.board[i][x]
                    mark = match[y]
                    if i == 0:
                        if self.GameState.board[i+1][x] == match and self.GameState.board[i+2][x] == match:
                            delta.append((mark,i,x))
                            delta.append((mark,i+1,x))
                            delta.append((mark,i+2,x))
                    elif i == self.row-1:
                        if self.GameState.board[i-1][x] == match and self.GameState.board[i-2][x] == match:
                            delta.append((mark,i,x))
                            delta.append((mark,i-1,x))
                            delta.append((mark,i-2,x))
                    else:
                        if self.GameState.board[i+1][x] == match and self.GameState.board[i-1][x] == match:
                            delta.append((mark,i,x))
                            delta.append((mark,i+1,x))
                            delta.append((mark,i-1,x))
        return delta
                        
    def diagonal_match(self):
        '''
        Checks for diagonal matches in the board and creates a list of the positions of the matches
        '''
        delta = []
        for i in range(self.row):
            for x in range(self.column):
                if self.GameState.board[i][x] != NONE:
                    y = int(len(self.GameState.board[i][x])/2)
                    match = self.GameState.board[i][x]
                    mark = match[y]
                    if i == 0:
                        if x == 0:
                            if self.GameState.board[i+1][x+1] == match and self.GameState.board[i+2][x+2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i+1,x+1))
                                delta.append((mark,i+2,x+2))
                        elif x == self.column-1:
                            if self.GameState.board[i+1][x-1] == match and self.GameState.board[i+2][x-2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i+1,x-1))
                                delta.append((mark,i+2,x-2))

                        elif x == 1:
                            if self.GameState.board[i+1][x+1] == match and self.GameState.board[i+2][x+2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i+1,x+1))
                                delta.append((mark,i+2,x+2))
                        elif x == self.column-2:
                            if self.GameState.board[i+1][x-1] == match and self.GameState.board[i+2][x-2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i+1,x-1))
                                delta.append((mark,i+2,x-2))
                        elif self.column>4:
                            if self.GameState.board[i+1][x-1] == match and self.GameState.board[i+2][x-2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i+1,x-1))
                                delta.append((mark,i+2,x-2))
                            if self.GameState.board[i+1][x+1] == match and self.GameState.board[i+2][x+2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i+1,x+1))
                                delta.append((mark,i+2,x+2))

                    if i == self.row-1:
                        if x == 0:
                            if self.GameState.board[i-1][x+1] == match and self.GameState.board[i-2][x+2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i-1,x+1))
                                delta.append((mark,i-2,x+2))

                        if x == self.column-1:
                            if self.GameState.board[i-1][x-1] == match and self.GameState.board[i-2][x-2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i-1,x-1))
                                delta.append((mark,i-2,x-2))
                        if x == 1:
                            if self.GameState.board[i-1][x+1] == match and self.GameState.board[i-2][x+2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i-1,x+1))
                                delta.append((mark,i-2,x+2))
                        if x == self.column-2:
                            if self.GameState.board[i-1][x-1] == match and self.GameState.board[i-2][x-2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i-1,x-1))
                                delta.append((mark,i-2,x-2))
                        elif self.column>4 and 2<=x<=self.column-3:
                            if self.GameState.board[i-1][x-1] == match and self.GameState.board[i-2][x-2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i-1,x-1))
                                delta.append((mark,i-2,x-2))
                            if self.GameState.board[i-1][x+1] == match and self.GameState.board[i-2][x+2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i-1,x+1))
                                delta.append((mark,i-2,x+2))
                    if i == 1:
                        if x == 0:
                            if self.GameState.board[i+1][x+1] == match and self.GameState.board[i+2][x+2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i+1,x+1))
                                delta.append((mark,i+2,x+2))
                        if x == self.column-1:
                            if self.GameState.board[i+1][x-1] == match and self.GameState.board[i+2][x-2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i+1,x-1))
                                delta.append((mark,i+2,x-2))
                    if i == self.row-2:
                        if x == 0:
                            if self.GameState.board[i-1][x+1] == match and self.GameState.board[i-2][x+2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i-1,x+1))
                                delta.append((mark,i-2,x+2))
                        if x == self.column-1:
                            if self.GameState.board[i-1][x-1] == match and self.GameState.board[i-2][x-2] == match:
                                delta.append((mark,i,x))
                                delta.append((mark,i-1,x-1))
                                delta.append((mark,i-2,x-2))
                    if 1<i<self.row-2:
                            if x == 0:
                                if self.GameState.board[i-1][x+1] == match and self.GameState.board[i-2][x+2] == match:
                                    delta.append((mark,i,x))
                                    delta.append((mark,i-1,x+1))
                                    delta.append((mark,i-2,x+2))
                                if self.GameState.board[i+1][x+1] == match and self.GameState.board[i+2][x+2] == match:
                                    delta.append((mark,i,x))
                                    delta.append((mark,i+1,x+1))
                                    delta.append((mark,i+2,x+2))
                            if x == self.column-1:
                                if self.GameState.board[i-1][x-1] == match and self.GameState.board[i-2][x-2] == match:
                                    delta.append((mark,i,x))
                                    delta.append((mark,i-1,x-1))
                                    delta.append((mark,i-2,x-2))
                                if self.GameState.board[i+1][x-1] == match and self.GameState.board[i+2][x-2] == match:
                                    delta.append((mark,i,x))
                                    delta.append((mark,i+1,x-1))
                                    delta.append((mark,i+2,x-2))
                            else:
                                if self.GameState.board[i+1][x+1] == match and self.GameState.board[i-1][x-1] == match:
                                    delta.append((mark,i,x))
                                    delta.append((mark,i-1,x-1))
                                    delta.append((mark,i+1,x+1))
                                if self.GameState.board[i-1][x+1] == match and self.GameState.board[i+1][x-1] == match:
                                    delta.append((mark,i,x))
                                    delta.append((mark,i+1,x-1))
                                    delta.append((mark,i-1,x+1))
        return delta

    def beginning_check(self):
        '''
        Checks if there are matches in the CONTENTS board.
        '''
        print_board(self.GameState)
        self.check_matched()
        print_board(self.GameState)
                               
    def match(self):
        '''
        Returns true if matches exist. False otherwise.
        '''
        marked = self.horizontal_match()+self.vertical_match()+self.diagonal_match()
        if len(marked) != 0:
            return True
        else:
            return False
                
    def check_matched(self):
        '''
        Changes the matched tiles into asterisks tiles.
        '''
        marked = self.horizontal_match()+self.vertical_match()+self.diagonal_match()
        if len(marked) != 0:
            for index in marked:
                self.GameState.board[index[1]][index[2]] = '*'+index[0]+'*'
            for i in range(self.row):
                for x in range(self.column):
                    if '*' in self.GameState.board[i][x]:
                        self.GameState.board[i][x] = NONE
            self.auto_fall_existing_board()
            self.check_matched()
        else:
            pass

    def mark_matched(self):
        '''
        Changes the matched tiles into asterisks tiles.
        '''
        marked = self.horizontal_match()+self.vertical_match()+self.diagonal_match()
        for index in marked:
            self.GameState.board[index[1]][index[2]] = '*'+index[0]+'*'

    def empty_matched(self):
        '''
        Changes the asterisk tiles into empty slots and falls existing tiles.
        '''
        for i in range(self.row):
                for x in range(self.column):
                    if '*' in self.GameState.board[i][x]:
                        self.GameState.board[i][x] = NONE
        self.auto_fall_existing_board()
        self.check_matched()
                     
    def _game_over(self):
        '''
        Initiates a Game Over
        '''
        self.Game_Over = True

class fall:

    def __init__(self, faller):
        try:
            self.frozen = False
            self.landed = False
            self.num_rows_moved = 0
            
            if len(faller)==5:
                self.move_type = faller[0]
                self.col = int(faller[1])
                self.gem1 = faller[2]
                self.gem2 = faller[3]
                self.gem3 = faller[4]
                self.block = self.create_gem_block()
            else:
                self.move_type = faller[0]
        except AttributeError:
            pass

    def rotate(self):
        '''
        Rotates the Gem order and creates a new gem block according the rotation
        '''
        self.gem1 = self.block[2]
        self.gem2 = self.block[0]
        self.gem3 = self.block[1]
        self.block = self.create_gem_block()

    def create_gem_block(self):
        '''
        Creates a gem block list
        '''
        self.block = [self.gem1, self.gem2, self.gem3]
        return self.block
    def freeze(self):
        '''
        Returns self.frozen as True
        '''
        self.frozen = True
        return self.frozen
    def land(self):
        '''
        Returns self.landed as True
        '''
        self.landed = True
        return self.landed

def print_board(GameState):
    '''
    prints the current state of the board
    '''
    for row in GameState.board:
        tile = []
        for jewel in row:
            tile.append(jewel)
        print('|' + ''.join(tile) + '|')
    print(' ' + '-'*3*GameState.column + ' ')




    
