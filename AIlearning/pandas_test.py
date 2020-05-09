# from pandas import Series,DataFrame
import pandas as pd

obj = pd.Series([3, 4, 6, -1])

# print(obj)
# print(obj.values)
# print({'a': 1, 'b': 2})

# obj2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])  # 索引可以重复
# print(obj2)

# DataFram操作高维数组
data = {'city': ['shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2018, 2017, 2018, 2017],
        'pop': [1.5, 1.6, 2.2, 2.3]
        }
frame = pd.DataFrame(data)
print(frame)

# 按年份，城市，人口排序
frame2 = pd.DataFrame(data, columns=['year', 'city', 'pop'],)

# print(frame2)
# print(frame2['city'])
# print(frame2.year)

frame2['new'] = 100
frame2['cap'] = frame2.city == 'beijing'

frame2['new'] = 100
print(frame2)
