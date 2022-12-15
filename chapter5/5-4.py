def recurse(n, s):
	"""
	The function calls itself until argument1 (n) equals 0 and then 
	returns the value of argument2 (s). 
	And in this case, the value of 's' will be equal to 
	the sum of the sequence from 'n' to 0, which adds up to the initial value of 's'.

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
