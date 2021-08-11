import random

a = [ ]
for i in range(0,10):
    b=random.randint(1, 6)
    a.append(b)
print(a)

#1을 7로 바꾸기

for i in range(0,10):
    if a[i] == 1:
        a[i] = 7

print(a)