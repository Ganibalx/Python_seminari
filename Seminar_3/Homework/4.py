list_of_things = {'холодильник': 20, 'спички': 1, 'палатка': 15, 'сосиски': 2, 'пиво': 0, 'вода': 2, 'мясо': 3,
                  'мангал': 5, 'топор': 2, 'уголь': 5}

result = list()
list_of_things = dict(sorted(list_of_things.items(), reverse=True, key=lambda i: i[1]))
flag = True

while flag:
    capacity = 20
    backpack = list()
    for i in list_of_things.keys():
        if list_of_things.get(i) <= capacity:
            backpack.append(i)
            capacity -= list_of_things.get(i)
    if len(backpack) == 0:
        flag = False
    else:
        result.append(backpack)
        list_of_things.pop(backpack[0])


print(result)