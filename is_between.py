
def is_between(x, y, z):
    if x > y > z :
        return True
    elif x < y < z:
        return True
    else:
        return False

def akerman (m, n):
    if m == 0:
        A = n + 1
    if m > 0 and n == 0 :
        A = m - 1  