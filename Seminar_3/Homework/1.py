
dict_friends = dict()
dict_friends['Коля'] = ('холодильник', 'спички', 'сосиски', 'пиво', 'водка')
dict_friends['Сергей'] = ('мясо', 'водка', 'мангал')
dict_friends['Саня'] = ('жена', 'спички', 'мясо', 'топор', 'уголь')

all = set()
[all.update(dict_friends.get(i)) for i in dict_friends.keys()]
print(f'все взятые предметы: \n{all}')

are_unique = set()
[are_unique.symmetric_difference_update(dict_friends.get(i)) for i in dict_friends.keys()]
print(f'уникальные предметы: \n{are_unique}')

for i in dict_friends.keys():
    things = set()
    for j in dict_friends.keys():
        if j != i:
            if len(things) == 0:
                things.update(dict_friends.get(j))
            else:
                things = things.intersection(dict_friends.get(j))
    print(f'у {i} нет: {things.difference(dict_friends.get(i))}')
