
def factorial(n):
    if not isinstance(n, int):
        print ('Factorial is only for  integers')
        return None
    elif n < 0 :
        print ('Factorial is itended only for positive numbers')
        return None
    if n == 0 :
        return 1
    else:
        recurse = factorial(n - 1)
        return n * recurse

print (factorial (6))
print (factorial(1.5))
print(factorial(-1))

