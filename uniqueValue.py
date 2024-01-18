a = [1, 2, 2, 3]
b = [4, 5, 4, 6]


def uniqueVal(a, b):

    # Usijng set to get unique elements, and then converting it back to a list
    c = list(set(a + b))
    return c


result = uniqueVal(a, b)
print(result)
