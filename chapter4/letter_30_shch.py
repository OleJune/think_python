import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def letter_sh(t, length):
    a.fd(length+length/4)
    a.rt(90)
    a.fd(length/4)
    a.bk(length/4)
    a.lt(90)
    a.bk(length/4)
    vertical_line(t, length)
    a.pu()
    a.bk(length/2)
    a.pd()
    a.lt(180)
    vertical_line(t, length)
    a.fd(length/2)
    a.lt(180)
    vertical_line(t, length)

a.color('dark blue')
a.pensize(10)
    
letter_sh(a, 200)
a.ht()
a.done()