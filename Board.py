# Connect 4 Game Board

class Board:

    def __init__( self, width=7, height=6 ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        self.data = [[' ']*width for r in range(height)]

    def getWidth():
        return self.width

    def getHeight():
        return self.height

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--'*self.width    # add the bottom of the board
        s += '-\n'
        for col in range( self.width ):
            s += ' ' + str(col%10)
        s += '\n'
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """ Add the game piece ox (either 'X' or 'O') to column col. """
        for rows in range(self.height):
            if self.data[rows][col]==" ":
                continue
            else:
                self.data[rows-1][col]=ox
                return
        self.data[self.height-1][col]=ox


    def clear(self):
        """ Clear the game board of all game pieces. """
        self.data=[[' ']*self.width for r in range(self.height)]

    def setBoard(self, moves):
        """ Set the board using an input string representation. """
        ox="X"
        xo="O"
        for number in range(len(moves)):
            if number%2==0:
                self.addMove(int(moves[number]),ox)
            else:
                self.addMove(int(moves[number]),xo)
            

    def allowsMove(self, col):
        """ Return True if adding a game piece in the given column is 
            permitted and return False otherwise. """
        if col<0:
            return False
        elif col>self.width:
            return False
        else:
            if self.data[0][col]==" ":
                return True
            else:
                return False               

    def isFull(self):
        """ Return True if the game board is full and False otherwise. """
        for rows in range(self.height):
            for cols in range(self.width):
                if self.data[rows][cols]!=' ':
                    continue
                else:
                    return False
        return True

    def delMove(self, col):
        """ Delete the topmost game piece from the given column. """
        add=0
        for rows in range(self.height):
            if self.data[rows][col]!=" ":
                add+=1
            else:
                continue
        if add==0:
            return
        else:
            self.data[self.height-add][col]=" "

    def winsFor(self, ox):
        """ Return True if the game has been won by player ox where ox
            is either 'X' or 'O'. """
        H=self.height
        W=self.width
        
        for rows in range(H):
            for cols in range(W-3):
                if self.data[rows][cols]==ox and self.data[rows][cols+1]==ox and \
                    self.data[rows][cols+2]==ox and self.data[rows][cols+3]==ox:
                    return True
        
        for rows in range(H-3):
            for cols in range(W):
                if self.data[rows][cols]==ox and self.data[rows+1][cols]==ox and \
                    self.data[rows+2][cols]==ox and self.data[rows+3][cols]==ox:
                    return True

        #Leave this for a while
        for rows in range(0,H-3):
            for cols in range(0,W-3):
                if self.data[rows][cols]==ox and self.data[rows+1][cols+1]==ox and \
                    self.data[rows+2][cols+2]==ox and self.data[rows+3][cols+3]==ox:
                    return True
        
        for rows in range(4,H):
            for cols in range(0,W-3):
                if self.data[rows][cols]==ox and self.data[rows-1][cols+1]==ox and \
                    self.data[rows-2][cols+2]==ox and self.data[rows-3][cols+3]==ox:
                    return True
        return False