import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def fd_lt(t, length):
    a.fd(length)
    a.lt(90)

def arc(t, length):
    r = length/4
    a.fd(length/4)
    a.circle(r, 180)
    a.fd(length/4)
    
def letter_znak(t, length):
    vertical_line(t, length)
    a.rt(90)
    fd_lt(t, length)
    arc(t, length)

a.color('dark blue')
a.pensize(10)

letter_znak(a, 200)
a.ht()
a.done()