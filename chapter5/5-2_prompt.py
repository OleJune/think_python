def check_fermat(a, b, c, n):
	if n > 2 and a**n + b**n == c**n:
		print('Holy smokes, Fermat was wrong!')
	else:
		print('No, that doesn\'t work')
#check_fermat(4, 3, 5, 3)


number = int(input('Enter any positive integer: '))
number1 = int(input('Enter any positive integer: '))
number2 = int(input('Enter any positive integer: '))
power = int(input('Enter number greater than 2: '))

check_fermat(number, number1, number2, power)
