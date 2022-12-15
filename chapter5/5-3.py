def is_triangle(a, b, c):
	if a<b+c and b<a+c and c<a+b:
		print('Yes')
	elif a==b+c or b==a+c or c==a+b:
		print('It\'s a "degenerate" triangle!')
	else:
		print('No')
#is_triangle(9, 11, 3)

side_a = int(input('Length of the first stick is: '))
side_b = int(input('Length of the second stick is: '))
side_c = int(input('Length of the third stick is: '))

is_triangle(side_a, side_b, side_c)