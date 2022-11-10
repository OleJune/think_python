import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def arc(t, length):
    r = length/4
    a.fd(length/4)
    a.circle(r, 180)
    a.fd(length/4)
    
def letter_b(t, length):
    vertical_line(t, length)
    a.fd(length/2)
    a.bk(length/2)
    a.rt(90)
    a.fd(length)
    a.lt(90)
    arc(t, length)

a.color('dark blue')
a.pensize(10)

letter_b(a, 200)
a.ht()
a.done()