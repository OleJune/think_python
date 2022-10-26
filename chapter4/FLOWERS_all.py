import math
import turtle as draw

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def flo(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    for i in range(n):
        flo(t, r, angle)
        t.lt(360/n)

def next_flower(t):
    draw.pu()
    draw.fd(300)
    draw.pd()

draw.pu()
draw.bk(300)
draw.pd()
flower(draw, 7, 150, 60)
next_flower(draw)
flower(draw, 10, 100, 80)
next_flower(draw)
flower(draw, 20, 370, 20)
draw.hideturtle()
draw.mainloop()
