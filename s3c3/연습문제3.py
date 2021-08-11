import random

print('☆구구단 테스트')

A = random.randint(1,9)
B = random.randint(1,9)

C = int(input('{} * {} ='.format(A,B)))

if A * B == C :
    print('맞습니다.')
else :
    print('틀렸습니다.')
