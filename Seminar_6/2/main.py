from sys import argv
from modul import play

options = list(map(int, argv[1:]))
min = 0
max = 10
count = 10
if len(options) != 0:
    if len(options) == 1:
        max = options[0]
    elif len(options) == 2:
        max, count = options
    else:
        min, max, count, *_ = options

print(play(min, max, count))
