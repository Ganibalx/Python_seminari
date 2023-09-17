from random import randint


def play(a, b, c):
    x = randint(a, b)
    result = 'Вы не угадали'
    for i in range(c+1):
        user_input = int(input('Введите число: '))
        if user_input == x:
            return True
        elif user_input > x:
            print('меньше')
        elif user_input < x:
            print('Больше')
    return False

