username = input("아이디를 입력하세요.:")
password = int(input("비밀번호 네 자리를 입력하요.:"))

if (username == "soen") :
    if (password == 1234) :
        print("본인 확인이 되었습니다. 환영합니다.")
    else :
        print("비밀번호가 틀렸습니다. 다시 확인해 보세요.")
else :
    print("아이디가 틀렸습니다. 다시 확인해 보세요.")
