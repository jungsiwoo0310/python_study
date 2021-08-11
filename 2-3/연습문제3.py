print('★더치페이 계산기')
total = int(input('내야할 금액은 얼마인가요?'))
people = int(input('사람은 몇 명인가요?'))

result = total//people
print('1인당 낼 돈 : %d' %result)

mod = total % result
print('부족한 돈: %d' %mod)