def sum_num(n, m):
    total = 0

    for i in range(n, m+1) :
        total = total + i

    return total

answer = sum_num(1, 10)
print(answer)

answer = sum_num(5, 10)
print(answer)