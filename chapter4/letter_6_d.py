import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def letter_d(t, length):
    vertical_line(t, length/3)
    a.fd(length/4)
    vertical_line(t, length/3*2)
    a.fd(length/2)
    a.rt(180)
    vertical_line(t, length/3*2)
    a.fd(length/2)
    a.bk(length/4*3)
    vertical_line(t, length/3)

a.color('dark blue')
a.pensize(10)
    
letter_d(a, 200)
a.ht()
a.done()