def 겉넓이(g, s, n) :
    leng = g*s*2 + g*n*2 + s*n*2
    return leng
def 넓이(g, s, n) :
    leng = g*s*n
    return leng

g = int(input('가로:'))
s = int(input('세로:'))
n = int(input('높이:'))

print('겉넓이: {}'.format(겉넓이(g, s, n)))
print('넓이: {}'.format(넓이(g, s, n)))