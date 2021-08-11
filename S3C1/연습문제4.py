print("★ 계산기")
num1 = int(input("첫 번쨰 수를 입력하세요.:"))
num2 = int(input("두 번쨰 수를 입력하세요.:"))
yeon = input("어떤 연산을 하실 건가요?")


if yeon == '+' :
    print("답은" , num1 + num2 , "입니다.")

if yeon == '-' :
    print("답은" , num1 - num2 , "입니다.")

if yeon == '*' :
    print("답은" , num1 * num2 , "입니다.")

if yeon == '/' :
    print("답은" , round(num1 / num2,1) , "입니다.")