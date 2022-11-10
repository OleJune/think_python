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

def letter_y(t, length):
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

# VARIANT 2

def letter_y1(t, length):
    vertical_line(t, length)
    a.rt(90)
    a.fd(length)
    a.lt(153.5)
    diagonal(t, length)
    a.rt(153.5) 
    a.fd(length)

a.pensize(10)
a.color('dark blue')

#letter_y(a, 200)

letter_y1(a, 200)
a.ht()
a.done()