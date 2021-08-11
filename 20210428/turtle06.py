import turtle as t

def star(t):
    t.left(36)
    for i in range (5) :
        t.forward(200)
        t.right(144)

def drawStar(x ,y):
    #print('x좌표{},y좌표{}'.format(x ,y))
    t.penup()
    t.goto(x ,y)
    t.pendown()
    star(t)

import random as rand

def bgchange():
    colors = ['orange', 'sky blue', 'lime green', 'gray']
    num = rand.randint(0,3)
    bg = colors[num]
    scr.bgcolor(bg)

t.shape('turtle')

scr = t.Screen()
scr.bgcolor('orange')

#star(t)
scr.onclick(drawStar)
scr.onkey(bgchange, 'c')

scr.listen()

t.mainloop()