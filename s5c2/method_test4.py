def 수의_합(frist, second):
    res = 0
    for i in range(frist, second+1) :
        res = res + i
    return res 

print(수의_합(1, 10))
print(수의_합(1, 100))
print(수의_합(1, 1000))

