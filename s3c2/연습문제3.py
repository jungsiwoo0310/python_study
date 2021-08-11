js = input("장수의 이름을 입력해주세요.:")
mr = int(input("무력을 입력해주세요."))
jcr = int(input("장치력을 입력해주세요."))
jr = int(input("지력을 입력해주세요."))
tsr = int(input("통솔력을 입력해주세요."))

if mr >= 80 or tsr >= 80:
    print(jr,'은(는) 장군이 될 수 있습니다.')

if jr >= 70 and jcr >= 70:
    print(jr,'은(는) 군사가 될 수 있습니다.')

else:
    print(jr,'은(는) 아무것도 될 수 없습니다.')
