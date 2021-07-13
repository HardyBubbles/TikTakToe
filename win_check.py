'''
Простая функция, принимающая содержимое доски и маркер игрока, после чего проверяет наличие выигрышных комбинаций.
A simple function that takes the contents of the board and the player's marker and then checks for winning combinations.
'''


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or     # across the bottom
    (board[4] == mark and board[5] == mark and board[6] == mark) or             # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or             # across the top
    (board[7] == mark and board[4] == mark and board[1] == mark) or             # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or             # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or             # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or             # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))               # diagonal
