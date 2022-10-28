import turtle as tur
def spiral(t):
	for i in range(150):
	    tur.circle(15 + i, 10)
tur.color('dark green')
tur.pensize(5)
spiral(tur)
tur.mainloop()