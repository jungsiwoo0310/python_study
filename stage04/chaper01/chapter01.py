for i in range(0 , 4 , 1) :
    print("%d 번쨰 안녕?" %i)

for i in range(4 , 0 , -1) :
    print("%d 번쨰 안녕?" %i)

for i in range(0 , 5 , 1) :
    print("안녕?")

total = 0
for i in range(1 , 11 , 1) :
    total = total + i
print('1부터 10까지 합계는 : %d 입니다.' %total)

a = 0
for i in "동해물과 백두산이 마르고 닳도록 하느님이 보우하사" :
    a = a + 1
    if i  == '하' :
        print(a)