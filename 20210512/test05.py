import turtle as t

scr =  t.Screen()
scr.setup(width=1.0, height=1.0)
t.shape('turtle')
t.speed(0)
t.color('red',"yellow")
t.begin_fill()

while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1 :
        break

t.end_fill()

t.mainloop()