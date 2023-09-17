from random import choice

_results = {}

def zagadka(count):
    global _results
    for i in get_puzzle():
        kol = 1
        zagadka, otvet = i
        print(zagadka)
        otvet = list(map(lambda x: x.lower(), otvet))
        while kol <= count:
            user_input = input('Введите ответ: ').lower()
            if user_input in otvet:
                _results[zagadka] = kol
                break
            kol += 1
        else:
            _results[zagadka] = 0


def get_puzzle():
    zagadka_dict = {'зимой и летом одним цветом': ['елка', 'ель', 'машина', 'небо', 'майонез'],
                    'Ни лает, ни кусает, в дом не пускает': ['замок', 'сторож'],
                    'сто одежек и все без застежек': ['стриптизерша', 'капуста', 'лук']}
    while zagadka_dict.keys():
        i = choice(list(zagadka_dict))
        yield i, zagadka_dict.pop(i)


def get_result():
    global _results
    result = ['Результаты:']
    max_len = len(max(list(_results), key=len))
    for puzzle, count in _results.items():
        result.append(f'{puzzle:<{max_len}}: Отгадана с {count} попытки')
    return '\n'.join(result)
