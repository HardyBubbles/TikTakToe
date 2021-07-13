'''
Функция спрашивает у 1го игрока, каким маркером он хочет отмечать свои квадратики на доске
The function asks the 1st player with which marker he wants to mark his squares on the board
'''


def player_input():
    p1_m = ""   # стартовое знач-е для запуска цикла while

    while not (p1_m == "X" or p1_m == "O"):
        p1_m = input("Player 1 please choose X or O: ").upper()

        if p1_m == "X":     # присвоение маркеров игрокам, исходя из выбора первого игрока
            p2_m = "O"
        elif p1_m == "O":
            p2_m = "X"
        else:
            print("Wrong input\n")

    return (p1_m, p2_m)     # возвращаем маркеры, присвоенные игрокам
