'''
Функция выводит содержимое доски, представленное в виде списка, в наглядном крафическом виде
The function displays the contents of the board, presented in the form of a list, in a visual craft form
'''

from IPython.display import clear_output


def display_board(board):
    clear_output()      # очищает поле вывода, при многократном вызове фун-и
    # доска будет проиндексирована сверху вниз, поэтому:
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("---|---|---")    # межсторчный разделитель
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("---|---|---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
