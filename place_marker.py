'''
Функция принимает содержимое доски в виде списка, маркер игрока и номер эл-та в списке.
После чего заменяет эл-т списка, соотвествующий номеру, на маркер игрока.
The function takes the contents of the board as a list, the player's marker, and the number of the item in the list.
Then it replaces the list item corresponding to the number with the player's marker.
'''


def place_marker(board, marker, position):
    board[position] = marker    # позицию указывает пользователь 1-9, в списке мы также используем 9 эл-ов,
                                # значит эл-т списка, соответствующий указанной позиции, заменяется на маркер
