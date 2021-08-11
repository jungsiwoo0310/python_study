li = []
num = 1
while len(li) < 500:
    count = 0
    num = num + 1
    for i in range(1,num+1):
        if num % i == 0:
            count = count + 1
            print(i, end=' ')
    print()
    print('{}의 약수의 개수는 {}개 입니다.'.format(num, count))
    if count == 2:
        print('{}는 소수입니다.'.format(num))
        li.append(num)
    else:
        print('{}는 소수가 아닙니다.'.format(num))

print(li)