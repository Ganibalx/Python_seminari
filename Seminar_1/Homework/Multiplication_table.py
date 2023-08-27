def creat_table(n, result):
    for i in range(2, 11):
        result.append(f'{n} x {i:^2} = {n*i:>2}\t\t'
                      f'{n+1} x {i:^2} = {(n+1)*i:>2}\t\t'
                      f'{n+2} x {i:^2} = {(n+2)*i:>2}\t\t'
                      f'{n+3} x {i:^2} = {(n+3)*i:>2}')
    result.append('')
    return result

result = list()
creat_table(2, result)
creat_table(6, result)
print(*result, sep='\n')
