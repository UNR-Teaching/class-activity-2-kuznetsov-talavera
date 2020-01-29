import numpy as np
""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""

class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = np.chararray((3,3), unicode=True)
        self.board[:] = '_'
        print(self.board)
        

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """
        if column < 3 and row < 3 and self.board[row][column] == '_':
            legal = True
        else:
            legal = False
        if legal:
            self.board[row][column] = player
        

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """

        pass

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        self.mark_square(0,1,'X')
        print(self.board)
        self.mark_square(0,1,'O')
        print(self.board)
        self.mark_square(0,2,'O')
        print(self.board)
        
        
        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))
