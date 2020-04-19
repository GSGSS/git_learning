import random
# print(random.randint(1, 2))

# print(random.choice(['aa', 'bb', 'cc', 'dd']))
mydic = {'aa': 0, 'bb': 0, 'cc': 0, 'dd': 0}
for i in range(0, 120):
    ran = random.choice(['aa', 'bb', 'cc', 'dd'])
    mydic[ran] += 1
print(mydic)
