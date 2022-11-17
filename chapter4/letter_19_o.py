import turtle as a
    
def letter_o(t, length):
    r = length/3
    a.circle(r, 90)
    a.fd(length/3)
    a.circle(r, 180)
    a.fd(length/3)
    a.circle(r, 90)

a.color('dark blue')
a.pensize(10) 

letter_o(a, 200)
a.ht()
a.done()