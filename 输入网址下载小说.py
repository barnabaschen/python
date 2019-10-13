
namelist = ['Sophia', 'Emma', 'Olivia', 'Ava','Mia','Isabella','Zoe','Lily','Emily','Madison','Jackson','Aiden','Liam','Lucas','Noah','Mason','Ethan','Caden','Logan','Jacob']
# # 点名册
for i in namelist:
    print(i)

for a in range(1, 11):
    print(a)
for i in range(1, 11):
    print('书珩走的第{}天，想他！'.format(i))

a = 1
while a <= 10:
    print(a)
    a = a+1


for i in range(10):
    if i == 5:
        break
    print(i)

a = 0
while a < 10:
    a += 1
    if a == 5:
        continue
    print(a)
# 逢7就跳


for a in range(100):
    if not a % 7 == 0:
     print(a)

