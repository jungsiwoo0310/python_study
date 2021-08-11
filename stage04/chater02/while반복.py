"""
i = 0

while i<4:
    print("%d번쨰 안녕?" %i)

    i = i + 1
i = 5

while i>0:
    print("%d번쨰 안녕?" %i)

    i = i - 1


i, total = 0, 0

while i<10:
    i = i + 1
    total = total + i
print("1부터 10까지의 합은 %d입니다." %total)


a = int(input(("숫자를 맞혀주세요. :")))
while a != 3 :
    a = int(input("틀렸습니다. 다시 맞혀 주세요. :"))
print("정답입니다!")
"""
import time

while True:
    print("무한 반복입니다. 멈추려면 Ctrl + C를 눌러주세요~")
    time.sleep(2)