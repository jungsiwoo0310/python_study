N = int(input('입력하세요.'))

total = 0.0
for i in range(1,N + 1):
    total = total + (float(i + 1)/float(i))
print(total)