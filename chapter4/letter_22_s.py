import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)
 
def half_step_fd(t, length):
    a.pu()
    a.fd(length/4)
    a.pd()

def letter_s(t, length):
    half_step_fd(t, length)
    r = length/3
    a.circle(r, 60)
    a.pu()
    a.circle(r, 30)
    a.fd(length/3)
    a.circle(r, 30)
    a.pd()
    a.circle(r, 150)
    a.fd(length/3)
    a.circle(r, 90)

a.color('dark blue')
a.pensize(10)

letter_s(a, 200)
a.ht()
a.done()