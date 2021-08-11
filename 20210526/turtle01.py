import turtle as t

t.shape('turtle')
def rect(길이):
    for i in range(4) :
        t.forward(길이)
        t.right(90)
def move_draw(x, y):
    t.penup()
    t.goto(x ,y)
    t.pendown()
    length = t.textinput('입력','길이를 입력 해줘요.')
    rect(int(length))

rect(150)

scr = t.Screen()
scr.onclick(move_draw)
scr.listen()

t.mainloop()