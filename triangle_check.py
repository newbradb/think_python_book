
def is_triangle (a , b, c):
    if c > a + b:
        print('Not triangle')
    elif a > c + b:
        print('Not triangle')
    elif b > a + c:
        print('Not triangle')
    else:
        print('Yes, this is suitable for triangle')

is_triangle (5, 5, 15)