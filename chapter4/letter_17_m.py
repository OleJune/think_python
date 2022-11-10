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

def letter_m(t, length):
    vertical_line(t, length)
    a.rt(60)
    diagonal(t, length/2)
    a.lt(120)
    diagonal(t, length/2)
    a.rt(150)
    a.fd(length)

a.color('dark blue')    
a.pensize(10)
letter_m(a, 200)
a.ht()
a.done()