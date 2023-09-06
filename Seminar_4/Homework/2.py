def my_dict(**kwargs):
    result = dict()
    for i in kwargs.keys():
        if type(kwargs.get(i)) == list or type(kwargs.get(i)) == set or type(kwargs.get(i)) == dict:
            result[str(' '.join([str(j) for j in kwargs.get(i)]))] = i
        else:
            result[kwargs.get(i)] = i
    return result



print(my_dict(text='Коля', int=45, list=[1, 2, 3, 4], set={1, 2, 'ntd', 4}, dict={'a':1, 'b':2, 'c':3} ))
