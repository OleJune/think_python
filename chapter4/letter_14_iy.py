import turtle as a
import math

def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90) 

def diagonal(t, length):
    x = length*length + length/2*length/2
    x1 = math.sqrt(x)
    a.fd(x1)

def letter_iy(t, length):
    vertical_line(t, length)
    a.pu()
    a.fd(length/2)
    a.pd()
    a.lt(180)
    vertical_line(t, length)
    a.pu()
    a.fd(length/2)
    a.pd()
    a.rt(116.5)  
    diagonal(t, length)
# drawing symbol above
    a.lt(116.5)
    a.pu()
    a.fd(length/2/4*3)
    a.rt(90)
    a.fd(length/5)
    a.lt(180)
    a.pd()
    r = length/10
    a.circle(r, 180)

a.color('dark blue')
a.pensize(10)

letter_iy(a, 200)
a.ht()
a.done()