from sys import exit

def is_triangle (a , b, c):
    if c > a + b:
        print('Not triangle')
    elif a > c + b:
        print('Not triangle')
    elif b > a + c:
        print('Not triangle')
    else:
        print('Yes, this is suitable for triangle')

def validate_args():
    one = input('Please specify the first line:')
    two = input('Please specify the second line:')
    three = input('Please specify the third line:')

    if one.isdigit() != 1:
        print('Only integers allowed!')
        exit()
    elif two.isdigit() != 1: 
        print('Only integers allowed!')
        exit()
    elif three.isdigit() !=1:
        print('Only integers allowed')
        exit ()
    return one, two, three


a, b, c = validate_args ()

is_triangle(a, b, c)