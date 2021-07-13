'''
Функция проверяет заполненность всего пространства доски: если функция space_check вернёт True (есть свободное место),
то функция full_board_check вернёт False. И наоборот.
The function checks the fullness of the entire space of the board: if the space_check function returns True (there is
free space), then the full_board_check function will return False. And vice versa.
'''

from space_check import space_check


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True
