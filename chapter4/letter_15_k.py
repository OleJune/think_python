import turtle as a
import math

def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def right_diagonal(t, length):
    c = length*length + length*length  # triangle with equal sides
    c1 = math.sqrt(c)
    a.fd(c1)    

def letter_k(t, length):
    vertical_line(t, length)
    a.pu()
    a.fd(length/2)
    a.rt(135)
    a.pd()
    right_diagonal(t, length/2)
    a.lt(90)
    right_diagonal(t, length/2)

a.color('dark blue')
a.pensize(10)

letter_k(a, 200)
a.ht()
a.done()