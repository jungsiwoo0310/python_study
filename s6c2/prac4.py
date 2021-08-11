import random

a = [ ]
for i in range(0,10):
    b=random.randint(1, 6)
    a.append(b)
print(a)

#1은 몇번 나올까요?
count = 0
for i in range(0,10):
    if a[i] == 1:
        count = count + 1

print(count)