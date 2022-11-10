import turtle as a

def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def letter_p(t, length):
    vertical_line(t, length)
    a.fd(length/2)
    a.rt(180)
    vertical_line(t, length)

a.color('dark blue')
a.pensize(10)
       
letter_p(a, 200)
a.ht()
a.done()
