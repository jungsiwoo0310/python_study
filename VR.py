gender = str(input("성별이 무엇인가요? (남/여)"))
h = int(input("키가 몇 cm입니까?"))
e = float(input("시력은 몇입니까?"))

if gender == "남" :
    if h >= 160 and e >= 1.2 : 
        print("VR 사격 대회에 참가할 수 있습니다.")
    else :
        print("아쉽네요. 참가할 수 없습니다.")
if gender == "여" : 
    if h >= 150 and e >= 1.2 :
        print("VR 사격 대회에 참가할 수 있습니다.")
    else :
        print("아쉽네요. 참가할 수 있습니다.")