import turtle as a
    
def vertical_line(t, length):
    a.lt(90)
    a.fd(length)
    a.rt(90)
    
def letter_i(t, length):
    a.fd(length/10*2)
    #a.pu()
    a.bk(length/10)
    #a.pd()
    vertical_line(t, length)
    #a.rt(90)
    #a.pu()
    a.fd(length/10)
    a.lt(180)
    #a.pd()
    a.fd(length/10*2)

a.color('dark blue')
a.pensize(10)  

letter_i(a, 200)
a.ht()
a.done()
