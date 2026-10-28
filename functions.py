def indexOf(numbers, num):
    for index, n in enumerate(numbers):
        if n == num:
            return index
    return -1

def lastIndexOf(numbers, num):
    result = -1
    for index, n in enumerate(numbers):
        if n == num:
            result=index
    return result