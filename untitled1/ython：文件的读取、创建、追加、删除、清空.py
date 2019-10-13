# 1.用Python创建一个新文件，内容是从0到9的整数, 每个数字占一行：
f = open('f.txt', 'w')    # r只读，w可写，a追加
for i in range(0, 10):
    f.write(str(i)+'\n')
f.close()

# 2.文件内容追加，从0到9的10个随机整数：

import random
f = open('f.txt', 'a')
for i in range(0, 10):
    f.write(str(random.randint(0, 9)))
f.write('\n')
f.close()

# 3.文件内容追加，从0到9的随机整数, 10个数字一行，共10行：
