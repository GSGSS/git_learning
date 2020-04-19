import re
p = re.compile('ca')
print(p.match('dcabdfcaaab'))

# 元字符 可上网搜索正则表达式元字符


# ()分组的用法
p = re.compile(r'(\d+)-(\d+)-(\d+)')
r = p.match('2019-03-05')
print(r)
print(r.group(1))
print(r.group(2))
print(r.group(3))
print(r.groups())
year,month,day=r.groups()

print(year+month+day)

#match是匹配功能，search是搜索功能，会找到匹配的部分
p = re.compile('ca')
print(p.search('dcabdfcaaab'))


#sub 替换函数
phone='136-2342-3256 #我想被替换'
repaclestr='替换成我'
p2=re.sub(r'#.*$',repaclestr,phone)
print(p2)
#只保留数字
p3=re.sub(r'\D','',p2)
print(p3)