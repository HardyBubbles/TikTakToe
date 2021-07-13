'''
Функция перезапуска игры
Game restart function
'''


def replay():
    return input('Do you want to play again? Enter Yes or No: ').upper().startswith('Y')
