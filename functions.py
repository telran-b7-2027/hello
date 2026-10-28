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

def min_even (numbers):
    result: None | int = None
    for num in numbers:
        if num % 2 == 0 and (result is None or num < result):
            result = num
    return result

