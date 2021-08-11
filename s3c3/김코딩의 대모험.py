import random
import time

print('아틀란티스 왕국의 공주, 세델리아 는 사악한 해적 ‘포론’에게 납치되어 미우타우로스 동굴에 갇히게 되었습니다. 공주를 구하기 위해서는 미우타우로스 동굴을 지키고 있는 다섯 괴물을 차례대로 물리쳐야 합니다. 김코딩은 공주를 구하기 위해 미우타우로스 동굴로 갔어요.')

input('진행하려면 엔터 키를 누르세요.')

time.sleep(1)

# 첫 번쨰 괴물

print('첫 번쨰 괴물은 날개 달린 사자 페세한!!')

time.sleep(1)

print('페세한을 이기기 위해서는 주사위를 굴려 페세한보다 더 높은 숫자가 나와야 합니다.')

페세한 = random.randint(1,5)

time.sleep(1.5)

input('주사위를 굴리려면 엔터 키를 누르세요.')

dice = random.randint(2,6)

time.sleep(1.5)

print('페세한의 주사위 : {}, 당신의 주사위 : {}'.format(페세한,dice))

if dice > 페세한 :
    print('페세한을 물리쳤습니다.')

    time.sleep(1.5)

    # 두 번쨰 괴물
    print('두 번쨰 괴물은 철갑 독수리 휴그바!!')

    time.sleep(1.5)

    print('휴그바를 이기기 위해서는 휴그바가 내는 수학 문제를 맞혀야 합니다. 문제는 3 + 8 / 2 - 9 * 3 입니다.')

    time.sleep(1.5)

    answer = int(input('답을 입력 해 주세요:'))

    if answer == (3 + 8 / 2 - 9 * 3) :
        print('휴그바를 물리쳤습니다.')

        # 세 번쨰 괴믈

        time.sleep(1.5)

        print('세 번째 괴물은 뿔 뿜는 용 ‘드래곤’!!')

        time.sleep(1.5)

        print('드래곤을 이기기 위해서는 1,2,3이라는 3개의 숫자 중에 드래곤이 랜덤으로 뽑은 숫자가 무엇인지 맞추어야 합니다.')

        드래곤 = random.randint(1,3)

        time.sleep(1.5)

        X = int(input('1,2,3 중 드래곤이 뽑을것 같은 숫자를 고르세요 :'))

        time.sleep(1.5)

        print('드래곤이 낸 수 : {}, 당신이 낸 수 : {}'.format(드래곤,X))

        if X == 드래곤 :
            print('드래곤을 물리쳤습니다.')

            # 네 번쨰 괴물

            print('네 번째 괴물은 피리 부는 뱀 ‘스말라’!!')

            time.sleep(1.5)

            print('스말라를 이기기 위해서는 스말라가 가지고 있는 동전의 개수가 짝수인지 홀수인지 맞추어야 합니다. 스말라는 동전을 1부터 100개 중 랜덤으로 선택합니다.')

            time.sleep(1.5)

            스말라 = random.randint(1,100)

            if 스말라 % 2 == 0:
                스말라 = '짝수'
            
            else :
                스말라 = '홀수'

            Y = str(input('스말라가 가지고 있는 동전의 수는 짝수일까요? 혹은 홀수 일까요?(짝수/홀수) :'))

            time.sleep(1.5)

            print('스말라 : {}, 나 : {}'.format(스말라,Y))

            time.sleep(1.5)

            if Y == 스말라 :
                print('드래곤을 물리쳤습니다.')

                time.sleep(1.5)

                #다섯 번째 괴물

                print('다섯 번째 괴물은 뿔 달린 원숭이 ‘아마톤’!!')

                time.sleep(1.5)

                print('아마톤을 이기기 위해서는 아마톤과의 가위바위보 게임에서 승리해야 합니다.')

                아마톤 = random.randint(1,3)

                if 아마톤 == 1 :
                    아마톤 = '가위'

                elif 아마톤 == 2 :
                    아마톤 = '바위'

                elif 아마톤 == 3 :
                    아마톤 = '보'

                time.sleep(1.5)
                
                Z = str(input('가위, 바위, 보 중 하나를 선택해 주세요 :'))

                time.sleep(1.5)

                print('아마톤 : {}, 나 : {}'.format(아마톤,Z))

                time.sleep(1.5)

                if Z == 아마톤 :
                    print('아마톤을 물리쳤습니다.')

                else :
                    print('게임에서 패배했습니다.')

                
            else :
                print('게임에서 패배했습니다.')

        else :
            print('게임에서 패배했습니다.')


    else :
        print('게임에서 패배했습니다.')

else :
    print('게임에서 패배했습니다.')