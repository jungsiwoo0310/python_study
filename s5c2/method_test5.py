def 둘레(d, e) :
    f = 2 * (d + e) 
    return  f
def 넓이(a, b) :
    c = a * b
    return c

one = int(input("가로의 길이를 입력하세요."))
two = int(input("세로의 길이를 입력하세요."))
print("넓이는 %d, 둘레는 %d 입니다."%(넓이(one, two),둘레(one, two)))