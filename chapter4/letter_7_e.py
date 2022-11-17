import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

# VARIANT 1

def letter_e(t, length):
    vertical_line(t, length)
    a.fd(length/2)
    a.bk(length/2)
    a.rt(90)
    a.fd(length/2)
    a.lt(90)
    a.fd(length/2)
    a.bk(length/2)
    a.rt(90)
    a.fd(length/2)
    a.lt(90)
    a.fd(length/2)


# VARIANT 2    turned repeating code into function

def half_horiz_line(t, length):
    a.fd(length/2)
    a.bk(length/2)
    a.rt(90)
    a.fd(length/2)
    a.lt(90)

def new_letter_e(t, length):
    vertical_line(t, length)
    half_horiz_line(t, length)
    half_horiz_line(t, length)
    a.fd(length/2)

a.color('dark blue')
a.pensize(10)
#letter_e(a, 200)
new_letter_e(a, 200)
a.ht()
a.done()