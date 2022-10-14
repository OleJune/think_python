def print_plus_minus():
    print('+', '- '*4 + '+', '- '*4 + '+', '- '*4 + '+', '- '*4 + '+')
def print_vertical_bar():
    print('|', ' '*7, '|', ' '*7, '|', ' '*7, '|', ' '*7, '|')

def four_bars():
    print_vertical_bar()
    print_vertical_bar()
    print_vertical_bar()
    print_vertical_bar()

def draw_grid():
    print_plus_minus()
    four_bars()
    print_plus_minus()
    four_bars()
    
def draw_4x4(func_object):
    draw_grid()
    print_plus_minus()

draw_4x4(draw_grid()) 
