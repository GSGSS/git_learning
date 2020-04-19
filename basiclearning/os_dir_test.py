from pathlib import Path  # 可以建立目录
import os
print(os.path.abspath('.'))  # 当前目录（参数相对路径）的绝对路径
print(os.path.abspath('/'))
print(os.path.exists('./name.txt'))  # 判断是否存在文件或目录
print(os.path.isfile('./name.txt'))  # 判断是否存在文件
print(os.path.isdir('./name.txt'))  # 判断是否存在目录


p = Path('.')
print(p.resolve())
print(p.is_dir())
q = Path('/a/b/c')
Path.mkdir(q, parents=True)  # 创建目录，如果父目录不存在自动创建
