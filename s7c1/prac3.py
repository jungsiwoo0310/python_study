name1 = "뽀로로,크롱,포비,루피"
arr = name1.split(",")
print(arr)

score = [91, 86, 77, 96]
for i in range(len(arr)):
    print('이름:{} / 점수:{}'.format(arr[i], score[i]))