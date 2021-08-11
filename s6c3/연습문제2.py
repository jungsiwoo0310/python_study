def exec(counts):
    # 1. 가장 큰 숫자 찾기
    m = max(counts)
    # 2. 가장 작은 숫자 찾기
    n = min(counts)
    # 3. 가장 큰 수와 가장 작은  수의 차를 계산하여 return 해준다. 
    return m - n

class1 = [55,36,47,44,64,50]
class2 = [58,39,63,50,46]
class3 = [73,38,44,49,52,60]
class4 = [46,34,49,52,55,38]

chai = exec(class1)
print("6-1반 차이:{}".format(chai))

chai = exec(class2)
print("6-2반 차이:{}".format(chai))

chai = exec(class3)
print("6-3반 차이:{}".format(chai))

chai = exec(class4)
print("6-4반 차이:{}".format(chai))