def my_function(path):
    a, b = path.split('.')
    c = a[0: a.rfind('/')+1]
    d = a[a.rfind('/')+1::]
    return (c, d, b)


print(my_function('C://a/c/v.txt'))