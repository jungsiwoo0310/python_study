arr = []

def isSosu(i):
    n = 2
    count = 0
    while n != i:
        if i % n == 0:
            count = count + 1
        n = n + 1
    if count == 0:
        arr.append(i)

for i in range(2, 101):
    isSosu(i)

print(arr)