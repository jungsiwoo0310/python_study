li = list()
num1 = int(input('첫 번째 숫자를 입력해줘:'))
num2 = int(input('두 번째 숫자를 입력해줘:'))

temp = 1
while not (temp > num1 or temp > num2) :
    if num1 % temp == 0 and num2 % temp == 0 :
        li.append(temp)
        print('공약수:' ,temp)
    temp += 1

print(li)