'''
Основной файл игры. Здесь буде описана главная логика, и отсюда будут выполняться запросы к функциям.
The main game file. This is where the main logic will be described, and function requests will be executed from here.
'''

from player_input import player_input
from choose_first import choose_first
from display_board import display_board
from player_choice import player_choice
from place_marker import place_marker
from win_check import win_check
from full_board_check import full_board_check
from replay import replay


print('Welcome to Tic Tac Toe!')

while True:
    # Стартовая настройка игры (доска, кто ходит первым, каким маркером будет пользоваться)
    # происходит задние доски
    the_board = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # Функция player_input() вернутся знач-я маркеров, присвоенные игрокам
    player1_marker, player2_marker = player_input()

    # Функция choose_first() укажет на игрока, который начинает игру
    turn = choose_first()
    print(turn + " will go first.")

    # Уточняем, готов ли выбранный игрок начать игру
    play_game = input("Ready to play? Y or N: ").upper()

    if play_game == "Y":
        game_on = True
    else:
        game_on = False

    # Игра запускается в цикле
    while game_on:
        # Player 1 Turn
        if turn == "Player 1":

            # выводит на экран доску
            display_board(the_board)

            # игрок выбирает позицию на доске
            position = player_choice(the_board)

            # происходит размещение маркера игрока в выбранной позиции
            place_marker(the_board, player1_marker, position)

            # проверяется, сложилась ли выиграшная комбинация из маркеров игрока
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON!!!")
                # игрок выиграл, можно прерывать цикл
                game_on = False
            else:
                # проверяется, может быть ничья
                if full_board_check(the_board):
                    display_board(the_board)
                    # ничья, можно прерывать цикл
                    print("DRAW GAME!")
                    break
                # нет ни победы, ни ничьей, то ход переходит ко второму игроку
                else:
                    turn = "Player 2"

        # Player2's turn.
        else:

            # выводит на экран доску
            display_board(the_board)  # Выводит на экран доску

            # игрок выбирает позицию на доске
            position = player_choice(the_board)

            # происходит размещение маркера игрока в выбранной позиции
            place_marker(the_board, player2_marker, position)

            # проверяется, сложилась ли выиграшная комбинация из маркеров игрока
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON!!!")
                # игрок выиграл, можно прерывать цикл
                game_on = False
            else:
                # проверяется, может быть ничья
                if full_board_check(the_board):
                    display_board(the_board)
                    # ничья, можно прерывать цикл
                    print("DRAW GAME!")
                    break
                # нет ни победы, ни ничьей, то ход переходит ко второму игроку
                else:
                    turn = "Player 1"

    if not replay():
        break
