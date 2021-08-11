import random

def dice():
    return random.randint(1,6)

def dance(idol1,idol2):
    print(idol1 + "와 " + idol2 + "가 춤을 춥니다.")

def parrot():
    print("코딩은 재밌어!")
    print("박수 부탁드립니다.")

def cal(*nums):
    total = 0
    for n in nums:
        total = total + n
    return total

def 한타(word):
    a = input(word+":")
    if a == word:
        print('정답입니다.')
    else:
        print('다시 입력하세요.')
        한타(word)

def jijun():
    #global a
    a = 10
    return a 

print("내가 굴린 주사위의 눈: %d" %dice())
print("컴퓨터가 굴린 주사위의 눈: %d" %dice())

dance("엑소","트와이스")
dance("모모랜드","비투비")

parrot()
parrot()

print(cal(4,3))

print('한글 타자 연습입니다. 다음에 제시된 단어를 입력하세요.')
한타("파이썬")
한타("트리케랍토스")

a = 1
print(jijun())
print(a)