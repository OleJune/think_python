import turtle as a

def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def letter_ch(t, length):
    a.pu()
    a.lt(90)
    a.fd(length)
    a.pd()
    a.bk(length/2)
    a.rt(90)
    a.fd(length/2)
    a.lt(90)
    a.fd(length/2)
    a.lt(180)
    a.fd(length)

# variant 2

def letter_ch1(t, length):
    a.pu()
    vertical_line(t, length)
    a.pd()
    a.rt(90)
    a.fd(length/2)
    vertical_line(t, length/2)
    a.lt(180)
    a.fd(length/2)
    a.lt(90)
    vertical_line(t, length)

a.color('dark blue')
a.pensize(10)

letter_ch(a, 200)
#letter_ch1(a, 200)
a.ht()
a.done()