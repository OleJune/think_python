import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def half_step_fd(t, length):
    a.pu()
    a.fd(length/4)
    a.pd()
    
def letter_T(t, length):
    half_step_fd(t, length)
    vertical_line(t, length)
    a.fd(length/2.5)
    a.rt(180)
    a.fd(length/2.5*2)

a.color('dark blue')
a.pensize(10)

letter_T(a, 200)
a.ht()
a.done()
