def recurse(n, s):
	"""
	Prints the value of 's' when 'n == 0'.

	Parameters:
		n: positive int
		s: int or float
	"""
	if n == 0:
		print(s)
	else:
		recurse(n-1, n+s)
recurse(3, 0)
#recurse(-1, 0)  #this is an infinite recursion that causes a runtime error
