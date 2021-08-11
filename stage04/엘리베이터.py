import random

x = int(input('몇 층에 가실 건가요?'))
y = random.randint (1,12)
print('이 엘리베이터의 정원은 8명입니다.')
print('현재 인원은',y,'명 입니다.')

if y < 9:
    for i in range(1,x):
        print(i, '층')
    print(x ,'층에 도착했습니다. 문이 열립니다.')

else :
    print('8명을 초과했습니다.',y - 8,'명 내려주세요.')