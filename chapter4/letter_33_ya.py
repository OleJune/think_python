import turtle as a
import math
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def arc(t, length):
    r = length/4
    a.fd(length/4)
    a.circle(r, 180)
    a.fd(length/4)

def right_diagonal(t, length):
    c = length*length + length*length  # triangle with equal sides
    c1 = math.sqrt(c)
    a.fd(c1)   

def half_step_fd(t, length):
    a.pu()
    a.fd(length/4)
    a.pd()    

def letter_ya(t, length):
    half_step_fd(t, length*2)
    vertical_line(t, length)
    a.lt(180)
    arc(t, length)
    a.rt(135)
    right_diagonal(t, length/2)

a.color('dark blue')
a.pensize(10)

letter_ya(a, 200)
a.ht()
a.done()