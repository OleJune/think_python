import turtle as a
import math

def diagonal(t, length):
    x = length*length + length/2*length/2
    x1 = math.sqrt(x)
    a.fd(x1)

def letter_l(t, length):
    a.lt(70)
    diagonal(t, length)
    a.rt(140)
    diagonal(t, length)

a.color('dark blue')
a.pensize(10)

letter_l(a, 200)
a.ht()
a.done()