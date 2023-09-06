
def trans(m):
    for i in range(len(m)):
        for j in range(i, len(m[i])):
            if i != j:
                m[i][j], m[j][i] = m[j][i], m[i][j]


m = [[1, 2, 3],
     [6, 7, 8],
     [4, 5, 9]]
trans(m)
print(m)