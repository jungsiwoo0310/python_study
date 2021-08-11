w , h =map(float, input('당시의 몸무게와 키를 순서대로 입력하세요:'). split(','))
result = w / (h**2)*10000
print('체질량지수:%.1f' %result)