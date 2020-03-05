# coding:utf-8
# 文件内容覆盖的写入
file1 = open('name.txt', mode='w')
file1.write(u'诸葛亮')
file1.close()

file2 = open('name.txt', mode='r')
content = file2.read()
file2.close()
print(content)
# 文件内容增加的写入
file1 = open('name.txt', mode='a')
file1.write('刘备')
file1.close()

file2 = open('name.txt', mode='r')
content = file2.read()
file2.close()
print(content)
