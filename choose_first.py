'''
Функция генерирует число 0 или 1, что позволяет определить очердность ходов
The function generates a number 0 or 1, which allows to determine the order of the moves
'''

import random


def choose_first():
    if random.randint(0, 1) == 0:   # фун-я вернёт значения 0 или 1
        return "Player 1"
    else:
        return "Player 2"
