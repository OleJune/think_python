import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def arc(t, length):
    r = float(length/4)
    a.fd(float(length/4))
    a.circle(r, 180)
    a.fd(float(length/4))

def letter_v(t, length):
    arc(t, float(length+5))
    a.rt(180)
    arc(t, float(length-5))
    vertical_line(t, length)

a.color('dark blue')
a.pensize(10)

letter_v(a, 200)
a.ht()
a.done()