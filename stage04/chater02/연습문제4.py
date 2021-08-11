import time

x = int(input('몇 도까지 끓이실 건가요?'))

water = 0

while water < x :
    print('현재 온도는 %d도 입니다.'%water)
    water = water + 10
    time.sleep(1)
print('%d도 입니다. 다 끓었습니다!!'%x)