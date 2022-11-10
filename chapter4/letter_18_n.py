import turtle as a

def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def fd_lt(t, length):
    a.fd(length)
    a.lt(90)

def letter_n(t, length):
    vertical_line(t, length)
    a.rt(90)
    fd_lt(t, length/2)
    fd_lt(t, length/2)
    fd_lt(t, length/2)
    vertical_line(t, length)

a.color('dark blue')
a.pensize(10)

letter_n(a, 200)
a.ht()
a.done()