a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = 5
slict = filter(lambda x: x < b, a)
print(type(slict))
print(list(slict))
