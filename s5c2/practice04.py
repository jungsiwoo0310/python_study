import time
def add(x, y):
    res = x + y
    return res    

def minus(x, y):
    res = x - y
    return res    

def multi(x, y):
    res = x * y
    return res    

def div(x, y):
    res = x / y
    return res    

def triangle(x, y):
    res = x * y / 2
    return res    

def square(x, y):
    res = 2 * (x + y)
    return res    

result = 0
while True:
    print('어떤 계산을 하고싶은지 골라주세요.')
    n = int(input('1:더하기\n 2:뺴기 \n 3:곱하기 \n 4:나누기 \n 5:삼각형의 넓이 \n 6:직사각형의 둘레 \n 종료:0 \n 입력: '))
    if n == 0:
        break
    a = int(input('첫 번쨰 숫자를 입력하세요: '))
    b = int(input('두 번쨰 숫자를 입력하세요: '))
    if n == 1:
        result = add(a,b)
    if n == 2:
        result = minus(a,b)
    if n == 3:
        result = multi(a,b)
    if n == 4:
        result = div(a,b)
    if n == 5:
        result = triangle(a,b)
    if n == 6:
        result = square(a,b)

    print('게산결과는 {}입니다.'.format(result))
    time.sleep(1)
    print('________________________')