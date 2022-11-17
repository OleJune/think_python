import turtle as a
import math

def diagonal(t, length):
    x = length*length + length/2*length/2
    x1 = math.sqrt(x)
    a.fd(x1)

def letter_kh(t, length):
    a.lt(63.5)
    diagonal(t, length)
    a.pu()
    a.lt(116.5)
    a.fd(length/2)
    a.lt(116.5)
    a.pd()
    diagonal(t, length)

a.color('dark blue')
a.pensize(10)
letter_kh(a, 200)
a.ht()
a.done()