a = [1, 2, 2, 3, 4, 4]

print(list(set([i for i in a if a.count(i) > 1])))