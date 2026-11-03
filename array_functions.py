def intersection (l1: list[int], l2: list[int]) -> list[int]:
    result = []
    for num1 in l1:
        if num1 in l2:
            result.append(num1)
    return result

def union (l1: list[int], l2: list[int]) -> list[int]:
    result = l1[:]
    for num in l2:
        if num not in result:
            result.append(num)
    return result

def difference (l1: list[int], l2: list[int]) -> list[int]:
    result = []
    for n in l1:
        if n not in l2:
            result.append(n)
    return result

def symmetric_difference (l1: list[int], l2: list[int]) -> list[int]:
    return difference(l1, l2) + difference(l2, l1)

def remove_positive_greater_or_negative_less(numbers:list[int],\
                         positive_lim: int, negative_lim: int) -> list[int]:
    result = []
    for num in numbers:
        if num in range(negative_lim, positive_lim+1):
            result.append(num)
    return result

def max_with_negative_duplicate (numbers:list[int]) -> int:
    result = -1
    size = len(numbers)
    for index, num in enumerate(numbers):
        if abs(num) > result:
            for j in range(index + 1, size):
                if numbers[j] == -num:
                    result = abs(num)
    return result
