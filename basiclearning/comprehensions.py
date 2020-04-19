# 列表推导式
# 求1-10 所有偶数的平方 放入列表
alist = []
for i in range(1, 11):
    if(i % 2 == 0):
        alist.append(i*i)
print(alist)
# 列表推导式
blist = [i*i for i in range(1, 11) if(i % 2 == 0)]
print(blist)

# 字典推导式
adict = {i: 0 for i in range(1, 11)}
print(adict)
