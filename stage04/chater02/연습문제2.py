x = int(input('시작 숫자를 입력해 주세요.'))
y = int(input('끝 숫자를 입력해 주세요.'))
total = 0

while x <= y :
    total = total + x
    x = x + 1
print(total)