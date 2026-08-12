
def factorial(n):
    if n == 0 :
        return 1
    else:
        recurse = factorial(n - 1)
        return n * recurse

print (factorial (6))