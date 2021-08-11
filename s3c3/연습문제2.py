score = int(input('점수를 입력하세요:'))

print('{} 점 입니다.'.format(score))

grade = 5
if score >= 90 :
    grade = 1
elif score >= 80 :
    grade = 2
elif score >= 70 :
    grade = 3
elif score >= 60 :
    grade = 4
else :
    grade = 5

print('{}등급 이군요.^^'.format(grade))