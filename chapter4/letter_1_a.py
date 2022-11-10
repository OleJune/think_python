import turtle as a
import math

def diagonal(t, length):
    x = length*length + length/2*length/2 # square of the length of hypotenuse
    x1 = math.sqrt(x)   # the length of hypotenuse (side of the letter A)
    a.fd(x1)

def middle_line(t, length):
    x = length*length + length/2*length/2 
    x1 = math.sqrt(x) 
    x2 = x1/2         
    x3 = 2 * x2 * math.cos(math.radians(70)) #base of the triangle with side x2
    a.fd(x3)

def letter_a(t, length):
    a.lt(70)
    diagonal(t, length)
    a.rt(140)
    diagonal(t, length)
    a.lt(180)
    a.pu()
    diagonal(t, length/2)
    a.lt(70)
    a.pd()
    middle_line(t, length)

a.color('dark blue')
a.pensize(10)

letter_a(a, 200)
a.ht()
a.done()