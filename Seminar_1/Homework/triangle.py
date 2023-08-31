def input_data(text):
    while True:
        try:
            return int(input(f'Введите сторону: {text}\n'))
            break
        except:
            print('Что-то не вышло, попробуй всетаки цифры')

def check(a, b, c):
    result = list()
    result.append('True' if a + b > c and a + c > b and b + c > a else 'False')
    if result[0] == 'True':
        if a == b and b == c and c == a:
            result.append('Равносторонний')
        elif a == c or b == c or a == b:
            result.append('Равнобедренный')
        else:
            result.append('Разносторонний')
    return result

def print_result(result):
    if len(result) == 2:
        print(f'Треугольник существует, он "{result[1]}"')
    else:
        print('Такого треугольника не существует')


print_result(check(input_data('a'), input_data('b'), input_data('c')))
