
def factorial(n):
    if not isinstance(n, int):
        raise TypeError('Factorial is for integers only')
    if n < 0:
        raise TypeError('Factorial is for positive values only')
    if n == 0:
        return 1
    else: 
        return n * factorial (n -1)


try:
    result_float = factorial(1.5)
    print(result_float)
except TypeError as e:
    print('Error:', e)
except ValueError as e:
    print('Error:', e)

try:
    result_integer = factorial(6)
    print(result_integer)
except TypeError as e:
    print('Error:', e)
except ValueError as e :
    print('Error:', e)

try: 
    result_minus = factorial(-1)
    print(result_minus)
except TypeError as e:
    print('Error:', e)
except ValueError as e :
    print ('Error', e)