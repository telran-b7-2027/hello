def binary_search(numbers: list[int], num:int)->int:
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return left if left < len(numbers) and numbers[left] == num else -(left + 1)

def insert_sorted(numbers: list[int], num: int) -> None:
    insert_index = binary_search(numbers, num)
    normalized_insert_index = - insert_index - 1 if insert_index < 0 else insert_index
    numbers.insert(normalized_insert_index, num)