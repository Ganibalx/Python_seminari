from random import randint


def check(positions):
    result = True
    for i in range(0, len(positions)-1):
        for j in range(i+1, len(positions)):
            if positions[i][0] == positions[j][0] \
            or positions[i][1] == positions[j][1] \
            or positions[i][0] - positions[j][0] == positions[i][1] - positions[j][1] \
            or positions[i][0] + positions[i][1] == positions[j][0] + positions[j][1]:
                result = False
    return result


def search_positions():
    result = []
    while len(result) != 4:
        attempt = []
        while len(attempt) != 8:
            item = (randint(1, 9), randint(1, 9))
            attempt.append(item)
        if check(attempt):
            result.append(attempt)
    return result
