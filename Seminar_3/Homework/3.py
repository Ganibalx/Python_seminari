data = ' fdg dss Тут будет любая строка , . - '

new_data = data.strip(' ,.-! ').lower()
my_dict = dict()
for i in new_data:
    my_dict[i] = my_dict.get(i, 0) + 1

print(dict(sorted(my_dict.items(), key=lambda i:i[1], reverse = True)[:10:]))

