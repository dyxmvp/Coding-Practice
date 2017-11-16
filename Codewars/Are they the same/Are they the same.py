def comp(array1, array2):
    # your code
	return None not in (array1, array2) and list(map(lambda x: x ** 2, sorted(array1))) == sorted(array2)