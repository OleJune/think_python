import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)

def letter_h(t, length):
    vertical_line(t, length)
    a.fd(length/2)

a.color('dark blue')
a.pensize(10)
    
letter_h(a, 200)
a.ht()
a.done()
