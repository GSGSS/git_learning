import time  #获取当前时间
print(time.time())
print(time.localtime())
print(time.strftime('%y-%m-%d %H:%M:%S'))

import datetime  #时间操作常用
print('_________________')
print(datetime.datetime.now())
newtime=datetime.timedelta(minutes=10)
print(datetime.datetime.now()+newtime)

one_day=datetime.datetime(2008,8,8)
new_day=datetime.timedelta(days=20)
print(one_day+new_day)

