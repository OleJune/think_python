print('Exercise 1:')
def do_twice(func_obj):
    func_obj()
    func_obj()
def print_day():
    print('Thursday')
do_twice(print_day)

print(' ')

print('Exercise 2(str):')
def do_twice(func_obj, value1):
    func_obj(value1)
    func_obj(value1)
def print_day(weekday):
    print(weekday)
do_twice(print_day, 'monday')

print(' ')

print('Exercise 2(int):')
def do_twice(func_obj, int):
    func_obj(int)
    func_obj(int)
def print_number(int):
    print(int)
do_twice(print_number, 6)

print(' ')

print('Exercise 3-4:')
def print_twice(value1):
    print(value1)
    print(value1)
def do_twice(func_obj, value1):
    func_obj(value1)
    func_obj(value1)
do_twice(print_twice, 'spam')

print(' ')

print('Exercise 5:')
def print_smth(words):
    print(words)
def do_twice(func_obj, words):
    print_smth(words)
    print_smth(words)
def do_four(func_obj, words):
    do_twice(print_smth, words)
    do_twice(print_smth, words)
do_four(do_twice, '4 for four')
