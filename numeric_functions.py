def min_max_average(numbers: list[int]) -> tuple[int, int, float] | None:
   if not numbers:
       return None

   minimal: int = numbers[0]
   maximal: int = numbers[0]
   total: int = numbers[0]

   for i in range(1, len(numbers)):
       num = numbers[i]
       minimal = min(num, minimal)
       maximal = max(num, maximal)
       total+=num
   return minimal,maximal, total / len(numbers)

def min_max_average_nums(n1: int, n2: int) -> tuple[int, int, float]:
   return min(n1,n2), max(n1,n2), (n1+n2)/2

def move_max_to_end(numbers: list[int]):
    if len(numbers) < 2:
        return

    maximal: int = numbers[0]
    index_of_max = 0

    for i in range(1, len(numbers)):
        num = numbers[i]
        if num > maximal:
            maximal = num
            index_of_max = i

    value = numbers.pop(index_of_max)
    numbers.append(value)