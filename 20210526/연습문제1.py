#1-1
a = int(input('숫자를 입력해 주세요:'))

if a % 2 == 0 :
    print('짝수 입니다.')
else :
    print('홀수 입니다.')

#1-2
for i in range(1,101):
    if i % 2 == 0 :
        print('{}은/는 짝수 입니다.'.format(i))
    else :
        print('{}은/는 홀수 입니다.'.format(i))

#1-3
num = int(input('숫자를 입력해 주세요:'))
if num % 2 == 0 and num % 3 == 0 :
    print('{} 은(는) 2와 3의 공배수입니다.'.format(num))
else :
    print('{} 은(는) 2와 3의 공배수가 아닙니다.'.format(num))

#1-4
for i in range(1,101,1):
    if i % 2 == 0 and i % 3 == 0 :
        print(i)
        












