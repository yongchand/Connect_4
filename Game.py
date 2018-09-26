from Board import *
from player import *

def main():
    """ Human versus AI game.  No code to write here! """
    k = int(input("Enter ply (level from 0 to 5): "))
    px = "human"
    po = Player("O", "LEFT", k)
    b = Board(7, 6)
    playGame(b, px, po)
    
def playGame(b, px, po):
    """ plays a game of Connect Four
        p1 and p2 are objects of type Player OR
        the string 'human'.
    """
    # Game starts with "X" moving, but this will alternate and thus
    # the nextPieceToMove will alternate during game play, so the
    # nextPieceToMove at the end of the game will be the winner which
    # could be "X" or "O".
    nextPieceToMove = "X"  
    nextPlayerToMove = px

    # FILL IN CODE HERE
    while b.isFull()==False and b.winsFor("X")==False and b.winsFor("O")==False:
        print(b)

        if nextPlayerToMove=="human":
            while True:
                playerMove=int(input("Select your move: "))
                if b.allowsMove(playerMove)==True:
                    b.addMove(playerMove,nextPieceToMove)
                    break
        
        else:
            column=nextPlayerToMove.nextMove(b)
            b.addMove(column,nextPieceToMove)
    
        if nextPieceToMove=="X":
            nextPieceToMove="O"
            nextPlayerToMove=po
        
        else:
            nextPieceToMove="X"
            nextPlayerToMove=px

    if nextPieceToMove=="X":
        nextPieceToMove="O"
        nextPlayerToMove=po
        
    else:
        nextPieceToMove="X"
        nextPlayerToMove=px
    
    print(nextPieceToMove+" wins!")
    print(b)
    return(b.data, nextPieceToMove)
    
