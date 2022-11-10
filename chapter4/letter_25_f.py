import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def half_step_fd(t, length):
    a.pu()
    a.fd(length/4)
    a.pd()

def letter_f(t, length):
    half_step_fd(t, length)
    vertical_line(t, length)
    a.lt(90)
    a.bk(length/4*3)
    a.rt(90)
    r = length/3
    a.fd(length/3/2)
    a.circle(r, 180)
    a.fd(length/3)
    a.circle(r, 180)
    a.fd(length/3/2)

a.color('dark blue')
a.pensize(10)

letter_f(a, 200)
a.ht()
a.done()