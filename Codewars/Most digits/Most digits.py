def find_longest(arr):
    #your code here
    return int(max([str(a) for a in arr], key = len))