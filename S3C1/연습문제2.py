num1 = int(input("첫 번쨰 수의 분자를 입력하세요.:"))
num2 = int(input("첫 번쨰 수의 분모를 입력하세요.:"))
num3 = int(input("두 번쨰 수의 분자를 입력하세요.:"))
num4 = int(input("두 번쨰 수의 분모를 입력하세요.:"))


if num1/num2 > num3/num4 :
    print("첫 번째 수가 두 번째 수보다 더 큽니다.")

if num3/num4 > num1/num2 :
    print("두 번째 수가 첫 번째 수보다 더 큽니다.")

if num1/num2 == num3/num4 :
    print("두 수의 크기는 같습니다.")