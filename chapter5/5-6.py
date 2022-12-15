import turtle as t
def curve_koch(t, length):
	if length < 15:
		t.fd(length)
		return
	curve_koch(t, length/3)
	t.lt(60)
	curve_koch(t, length/3)
	t.rt(120)
	curve_koch(t, length/3)
	t.lt(60)
	curve_koch(t, length/3)

"""Write a function called snowflake that draws 
three Koch curves to make the outline of a snowflake."""
def snowflake(t, length):
	for i in range(3):
		curve_koch(t, length)
		t.rt(120)

"""The Koch curve can be generalized in several ways. See http://en.wikipedia.org/
wiki/Koch_snowflake for examples and implement your favorite."""
def cesaro_antisnowflake(t, length):
	for i in range(4):
		curve_koch(t, length)
		t.lt(90)

#snowflake(t, 200)
#curve_koch(t, 270)
cesaro_antisnowflake(t, 150)
t.ht()
t.done()