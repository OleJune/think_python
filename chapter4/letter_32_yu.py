import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def letter_yu(t, length):
    vertical_line(t, length)
    a.rt(90)
    a.fd(length/2)
    vertical_line(t, length/3)
    r = length/3
    a.fd(length/3/2)
    a.circle(r, 180)
    a.fd(length/3)
    a.circle(r, 180)
    a.fd(length/3/2)

a.color('dark blue')
a.pensize(10)

letter_yu(a, 200)
a.ht()
a.done()