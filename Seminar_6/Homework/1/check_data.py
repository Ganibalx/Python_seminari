def check(date):
    d, m, y = map(int, date.split('.'))
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    result = False
    if 0 < y <= 9999:
        if 0 < m <= 12:
            if 0 < d <= (29 if m == 2 and _bissextile(y) else days[m]):
                result = True
    return result


def _bissextile(year):
    return True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False
