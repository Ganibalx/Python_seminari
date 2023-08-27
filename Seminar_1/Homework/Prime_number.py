def input_data():
    while True:
        try:
            result = int(input('Введите число в диапозоне от 0 до 100 000:\n'))
            if result > 0 and result <= 100000:
                return result
        except:
            print('Введи число')

result = input_data()
flag = 0
if result == 0 or result == 1:
    print("Число никакое")
else:
    for i in range(2, int(result**0.5)):
        if result % i == 0:
            flag += 1
            break
    if flag:
        print('Число составное')
    else:
        print('Число простое')
