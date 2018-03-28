import turtle as t
import random as r

c=r.randint(1,100)
t.pensize(c)



t.shape('turtle')
t.color('yellow')
t.speed(0)




for x in range(1000):
    a=r.randint(1,360)
    t.setheading(a)
    b=r.randint(1,20)
    t.forward(b)
    
    
