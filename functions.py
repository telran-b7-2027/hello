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

def count(numbers, num) :
    result = 0
    for n in numbers:
        if n == num:
            result += 1
    return result

#Not optimal with what we have learned
#O(n^2) - time
#O(n) - space
def sum_of_two_exists(numbers, sum):
    seen = []
    for num in numbers:
        if num in seen:
            return True
        seen.append(sum - num)
    return False

#Optimal with set (not learned)
#O(n) - time
#O(n) - space
def optimal_sum_of_two_exists(numbers, sum):
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(sum - num)
    return False
