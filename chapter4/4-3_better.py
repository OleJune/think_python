import turtle as draw
import math

def triangle(t, angle, length):
    half_base_length = length * math.sin(math.radians(angle/2))

    t.fd(length)
    t.lt(90+angle/2)
    t.fd(2*half_base_length)
    t.lt(90+angle/2)
    t.fd(length)
    t.lt(180)

def pie(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        triangle(t, angle, length)

def next_pie(t):
    draw.pu()
    draw.fd(250)
    draw.pd()

#triangle(draw, 40, 150)

draw.pu()
draw.bk(300)
draw.pd()
pie(draw, 5, 100)
next_pie(draw)
pie(draw, 6, 100)
next_pie(draw)
pie(draw, 7, 100)
draw.hideturtle()
draw.mainloop()