X = int(input("X 좌표를 입력해주세요.:"))
Y = int(input("Y 좌표를 입력해주세요.:"))

사분면 = 0

if X > 0 and Y > 0:
    사분면 = 1

elif X < 0 and Y > 0:
    사분면 = 2

elif X < 0 and Y < 0:
    사분면 = 3

elif X > 0 and Y < 0:
    사분면 = 4
else:
    print("잘못된 값을 입력 하셨습니다.")
    

print('({},{})는 {} 사분면에 위치해 있습니다.'.format(X,Y, 사분면))