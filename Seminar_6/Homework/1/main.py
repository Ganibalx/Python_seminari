from check_data import check
from sys import argv


options = list(argv[1:])
if len(options) == 0:
    date = '29.02.2004'
else:
    date = options[0]
print(check(date))
