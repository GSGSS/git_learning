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
file1.write('刘备\n')
file1.write('第二行\n')
file1.write('第三行')
file1.close()

file2 = open('name.txt', mode='r')
content = file2.read()
file2.close()
print(content)
# 按行循环读取文件内容
# file3 = open("name.txt")
# for line in file3.readlines():
#     print(line)
#     print('==============')
# file3.close()

# 操作文件的指针（当前位置） tell seek
file4 = open("name.txt")
print(file4.tell())
print(file4.read(1))
print(file4.tell())
print(file4.read(1))
print(file4.tell())
# 参数一表示偏移量，参数二, 0表示从文件开头偏移，1表示从当前位置偏移，2表示从文件尾
file4.seek(2, 0)
print(file4.tell())

