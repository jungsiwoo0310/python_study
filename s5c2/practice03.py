def type01(a, b, c) :
    res =  a * b - c
    return res

def type02(a, b, c) :
    res =  a + b * c
    return res

def type03(a, b, c) :
    res =  a / b + c
    return res

typeInput = int(input("유형을 선택해 주세요(1,2,3): "))
result = 0

num1 = int(input(" 첫번쨰 숫자를 입력 해주세요: "))
num2 = int(input(" 두번쨰 숫자를 입력 해주세요: "))
num3 = int(input(" 세번쨰 숫자를 입력 해주세요: "))

if typeInput == 1 :
    result = type01(num1, num2 ,num3)

elif typeInput == 2 :
    result = type02(num1, num2 ,num3)

elif typeInput == 3 :
    result = type03(num1, num2 ,num3)

print('계산결과는 {}입니다.'.format(result))

