print("이 영화는 12세 이상 관람가 입니다.")

age = int(input("당신은 몇 살인가요?:"))
standard = 12

if age < standard:
    print("영화 관람이 불가능합니다.")

else :
    print("영화 관람이 가능합니다.")