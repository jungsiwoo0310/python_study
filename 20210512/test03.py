import turtle as t
import random as rand



t.shape('turtle')

for i in range(10) :
    cir = rand.randint(60,190)
    x = rand.randint(-300,300)
    y = rand.randint(-300,300)

    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(cir)



t.mainloop()