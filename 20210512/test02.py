import turtle as t

t.shape('turtle')
t.left(90)
t.color('red')
t.speed(0)

size = 200
for k in range(2) :
    for i in range(36) :
        for j in range(5) :
            t.forward(size)
            t.left(144)
        t.left(10)
    size = size - 100

t.mainloop()