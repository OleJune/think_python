def recurse(n, s):
	"""
	Calculates and prints the value of argument2 (s) after calling itself 
	until it reaches the base case where argument1 (n) equals 0.

	# or: The function calls itself until argument1 (n) equals 0
	#		and then returns the value of argument2 (s).

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
