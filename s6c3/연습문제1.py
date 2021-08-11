def hot(a):
    print('%s 분말을 종이컵에 넣습니다.'%a)
    print('뜨거운 물을 넣습니다.')
    print('섞어 줍니다.')

def cool(a):
    print('%s 시럽을 종이컵에 넣습니다.'%a)
    print('시원한 물을 넣습니다.')
    print('섞어 줍니다.')

drink = input('원하는 차를 선택하세요. (코코아/유자차/아이스티/콜라)')

if drink == "코코아" or drink == "유자차":
    hot(drink)

if drink == "아이스티" or drink == "콜라":
    cool(drink)
print("%s가 나왔습니다. 맛잇게 드세요." %drink)