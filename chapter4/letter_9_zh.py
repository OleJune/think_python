import turtle as a
import math

def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def right_diagonal(t, length):
    x2 = length*length + length*length  # triangle with equal sides
    x3 = math.sqrt(x2)
    a.fd(x3) 

def half_step_fd(t, length):
    a.pu()
    a.fd(length/4)
    a.pd()

def letter_zh(t, length):
    half_step_fd(t, length)
    vertical_line(t, length)
    a.pu()
    a.fd(length/2)
    a.rt(135)
    a.pd()
    right_diagonal(t, length)
    a.rt(135)
    a.pu()
    a.fd(length)
    a.rt(135)
    a.pd()
    right_diagonal(t, length)

a.pensize(10)
a.color('dark blue')

letter_zh(a, 200)
a.ht()
a.done()