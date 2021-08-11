import random

rsp = input("무엇을 내실 건가요? (가위/바위/보):")
rspc = random.choice(['가위' , '바위' , '보'])

print("컴퓨터는 {} 를 냈습니다.".format(rspc))

if rsp == '가위' and rspc == '바위' :
    print("컴퓨터가 이겼습니다.")

elif rsp == '가위' and rspc == '보' :
    print("컴퓨터가 졌습니다.")

elif rsp == '주먹' and rspc == '가위' :
    print("컴퓨터가 졌습니다.")

elif rsp == '주먹' and rspc == '보' :
    print("컴퓨터가 이겼습니다.")

elif rsp == '보' and rspc == '바위' :
    print("컴퓨터가 졌습니다.")

elif rsp == '보' and rspc == '가위' :
    print("컴퓨터가 이겼습니다.")

else :
    print("비겼습니다.")