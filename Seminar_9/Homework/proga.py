import csv
import json
import random as rnd

CSV_PATH = 'file.csv'

def read_file(func):
    def wrapper():
        res = []
        with open(CSV_PATH, 'r', encoding='utf-8', newline='')as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                arg_dic = {'a': line[0],
                           'b': line[1],
                           'c': line[2],
                           'root': func(int(line[0]), int(line[1]), int(line[2]))}
                res.append(arg_dic)
            return res
    return wrapper


def writ_json(func):
    def wrapper():
        res = func()
        with open('my.json', 'w', encoding='utf-8')as f:
            json.dump(res, f, indent=4, ensure_ascii=False)
        return res
    return wrapper


@writ_json
@read_file
def get_root(a, b, c):
    result = []
    d = (b**2) - 4 * a * c
    if a == 0:
        a = rnd.randint(1, 99)
    if d > 0:
        result.append(round(((-b + d ** 0.5) / (2 * a)), 2))
        result.append(round(((-b - d ** 0.5) / (2 * a)), 2))
    elif d == 0:
        result.append(round(((-b) / (2 * a)), 2))
    return result


def csv_generator():
    roots = [[rnd.randint(-99, 99) for _ in range(3)] for _ in range(rnd.randint(100, 1000))]
    with open(CSV_PATH, 'w', encoding='utf-8')as f:
        csv_writ = csv.writer(f, dialect='excel')
        csv_writ.writerows(roots)


print(get_root())