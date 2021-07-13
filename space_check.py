'''
Функция принимает содержимое доски в виде списка и номер эл-та списка, после чего проверяет, что указанный эл-т не
является маркером одного из игроков
The function takes the contents of the board in the form of a list and the number of the list item,
and then checks that the specified item is not a marker of one of the players
'''


def space_check(board, position):
    return board[position] not in ["X", "O"]
