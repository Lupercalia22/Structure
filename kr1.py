def funk1(x):
    if(x <= 0):
        return 0
    if(x%2!=0):
        return x - 2
    else:
        return x - 1

def prover(x, y):
    return x + y == 3

def sum(a, b):
    return 1 / (a + b)

def funk2(func, funk1, a, b, cond ):
    if cond(a, b):
        return func(a, b)
    elif (a + b <= 0):
        return 0
    else:
        return func(a, b) + funk2(func, funk1, funk1(funk1(a)), funk1(a), cond)

def funk4(a, b):
    a, b = min(a, b), max(a, b)
    return funk2(sum, funk1, a, b, prover)

print(funk4(23, 27))