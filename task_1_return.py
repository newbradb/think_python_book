def absolute_value(x):
    x = int(x)
    if x < 0:
        return -x
    if x > 0:
        return x
    else:
        return 0

print (absolute_value(input('Please enter number for absolute value:')))