import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def half_step_fd(t, length):
    a.pu()
    a.fd(length/4)
    a.pd()
    
def letter_ye(t, length):
    half_step_fd(t, length*2)
    r = length/2
    a.fd(length/10)
    a.pu()
    a.circle(r, 180)
    a.pd()
    a.fd(length/10)
    a.circle(r, 180)
    a.pu()
    vertical_line(t, length/2)
    a.pd()
    a.bk(length/2)

a.color('dark blue')
a.pensize(10)

letter_ye(a, 200)
a.ht()
a.done()