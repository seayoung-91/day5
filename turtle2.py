import turtle as t
import random as r
t.shape('turtle')
t.shapesize(2,2,0)
color=['red','blue','green','yellow','orange','purple']
t.speed(100)

for i in range(50):
    t.pensize(r.randint(1,5))
    t.pencolor(color[i%6])
    t.fd(200)
    t.lt(60)
    t.lt(10)
t.penup()
t.goto(-200,-200)
t.pendown()
t.fillcolor(color[2])
t.begin_fill()
t.circle(200)
t.end_fill()
