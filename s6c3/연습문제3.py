def bimando(h, w):
    standard = h/100 * h/100 * 22 #표준 체중
    return (w-standard)/standard * 100

num1 = float(input("키를 입력 해주세요"))
num2 = float(input("몸무게를 입력 해주세요"))

bmi = bimando(num1, num2)
print('bmi : {}'.format(bmi))

if bmi < 10 :
    print("비만지수 결과 : 정상입니다.")
elif bmi >= 10 and bmi < 20 :
    print("비만지수 결과 : 과체중입니다.")
elif bmi >= 20 :
    print("비만지수 결과 : 비만입니다.")