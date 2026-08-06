import sys

#function to draw triangle
def triangle (symbol, n) :
    n = int(n)
    for i in range (1, n + 1):
        print(symbol * i)

#function to draw rectangle
def rectangle(symbol, n, s):
    n = int(n)
    s = int(s)
    for i in range ( n ):
        print(symbol * s ) 


#function to read input
def read_user_input (): 
    number = input('Chose 1 for triangle, 2 for rec:')
    number = int(number)
    if number == 1:
        symbol, count = validate_args_triangle () 
        triangle(symbol, count)
    elif number == 2:
        symb, cou1, cou2 = validate_args_rectangle () 
        rectangle(symb, cou1, cou2 )
    else:
        sys.exit()


def validate_args_triangle():
    symbol = input('Please specify the Symbol(upper letter:)')
    count = input('Please specify the number(integer only:)')

    if symbol.isupper() != 1:
        print('First argument only uppercase letter')
        sys.exit()
    elif count.isdigit() != 1 :
        print('Second argument only digit')
        sys.exit()
    return symbol, count

def validate_args_rectangle():
    
    symb = input('Please specify symbol(Upper letter):')
    co1 = input('Please specify number of colunms(int only):')
    co2 = input('Please specify number of rows(int only):')

    
    if symb.isupper() != 1:
            print('First argument only uppercase letter')
            sys.exit()
    elif co1.isdigit() != 1 :
            print('Second argument only digit')
            sys.exit()
    elif co2.isdigit() != 1:
         print('Third argument only digit')
         sys.exit()
    return symb, co1, co2
    
read_user_input ()

#symbol_user, count_user = validate_args()
#triangle(symbol_user , count_user)