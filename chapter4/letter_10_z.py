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

def letter_z(t, length):
    arc(t, length+3)
    a.rt(180)
    arc(t, length-3)

a.pensize(10)
a.color('dark blue')

letter_z(a, 200)
a.ht()
a.done()