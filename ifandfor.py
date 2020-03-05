# ######if条件
# x=input('请输入一个数字：')
# x=int(x)
# if x>100:
#     print('x>100')
# elif x>50:
#     print('x>50')
# elif x>20:
#     print('x>20')
# elif  x>10:
#     print('x>10')
# else:
#     print('x<20')

# ######for循环
# chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
# for cz in chinese_zodiac:
#     # print(cz)
#     pass

# for i in range(2000, 2012):
#     print("%s 年是 %s 年" % (i, chinese_zodiac[i % 12]))

# while循环

import time
num = 5
while True:
    num = num+1
    if num == 10:
        continue
    print(num)
    time.sleep(1)
    if num>19:
        break
