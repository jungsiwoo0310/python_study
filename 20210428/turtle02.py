import turtle as t 

t.shape('turtle')

n = int(input('숫자를 입력 해주세요.:'))

t.color('#ADF7BE')
t.begin_fill()

for i in range(n) :
    t.forward(1) 
    t.right(360/n)

t.end_fill()
t.mainloop()