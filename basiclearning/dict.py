dict1 = {'a': 1, 3: '123'}
dict1['c'] = {'aa': 11, 'bb': 22}
print(dict1)
print(dict1.get(3))
for dict1key in dict1.keys():
    print(dict1.get(dict1key))
