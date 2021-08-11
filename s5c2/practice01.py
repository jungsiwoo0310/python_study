def 넓이(leng) :
    leng = leng * leng
    return leng

def 둘레(leng):
    leng = leng * 4
    return leng

length = int(input('정사각형의 한 변의 길이를 입력해주세요: '))
print('넓이: {}'.format(넓이(length)))
print('둘레: {}'.format(둘레(length)))