import turtle as a
    
def horizontal_line(t, length):
    a.fd(length)
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)
    
def letter_yi(t, length):
    size = length/12
    horizontal_line(t, length/10*2)
    a.bk(length/10)
    vertical_line(t, length)
    a.fd(length/10)
    a.lt(180)
    horizontal_line(t, length/10*2)
    a.pu()
    a.lt(180)
    vertical_line(t, length/10)
    a.pd()
    a.dot(size)
    a.pu()
    a.fd(length/10*2)
    a.pd()
    a.dot(size)
    
a.color('dark blue')
a.pensize(10)

letter_yi(a, 200)
a.ht()
a.done()
