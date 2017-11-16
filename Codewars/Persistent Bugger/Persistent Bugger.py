def persistence(n):
    # your code
    i = 0
    while n >= 10:
        n = reduce((lambda x, y: x * y), [int(x) for x in str(n)])
        i += 1
    return i