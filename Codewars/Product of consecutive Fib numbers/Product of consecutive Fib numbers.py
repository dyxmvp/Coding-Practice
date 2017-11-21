def productFib(prod):
    # your code
    F0, F1 = 0, 1
    while F0 * F1 < prod:
        F0, F1 = F1, F0 + F1
    return [F0, F1, F0 * F1 == prod]