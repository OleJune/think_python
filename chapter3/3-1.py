#перший варіант
print('variant 1:')

def right_justify(s):
    leading_space = 70 - len(s)
    print(leading_space * ' ' + s)
right_justify("It's such a beautiful day!")


#другий варіант

print(' ')
print('variant 2:')

def right_justify(s):
    print(' ' * (70 - len(s)) + s)
right_justify("It's such a beautiful day!")
