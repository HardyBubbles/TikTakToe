'''
Функция проверяет, чтобы указанная игроком позиция была от 1 до 9, а также была без маркера
The function checks that the position indicated by the player is from 1 to 9 and without a marker
'''

from space_check import space_check


def player_choice(board):
    position = 0
    exist_pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while position not in exist_pos or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position
