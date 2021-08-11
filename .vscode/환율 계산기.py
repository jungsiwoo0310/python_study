print('★환율 계산기★')

won = int(input('우리나라 돈 얼마를 환전하고 싶나요?'))
usd = 1115.75
print('미국:약' , round(won / usd , 2), '달러')
yen = 10.62
print('일본:약' , round(won / yen , 2), '달러')
cny = 172.71
print('중국:약' , round(won / cny , 2), '달러')
thb = 37.15
print('태국:약' , round(won / thb , 2), '달러')
php = 23.23
print('필리핀:약' , round(won / php , 2), '달러')