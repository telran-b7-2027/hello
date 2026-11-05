from numeric_functions import *

#min_max_average
assert min_max_average([10, 20, 60]) == (10, 60, 30.0)
assert min_max_average([1, 2]) == (1, 2, 1.5)
assert min_max_average([10, -20, -38]) == (-38, 10, -16.0)
assert min_max_average([5]) == (5, 5, 5.0)
assert min_max_average([]) is None

result = min_max_average([10, 20, 30])
assert result is not None
minimum, maximum, average = result
assert type(minimum) is int
assert type(maximum) is int
assert type(average) is float

assert min_max_average_nums(10, 20) == (10, 20, 15.0)
assert min_max_average_nums(-10, -20) == (-20, -10, -15.0)
assert min_max_average_nums(0, 0) == (0, 0, 0.0)

minimum, maximum, average = min_max_average_nums(10, 20)
assert type(minimum) is int
assert type(maximum) is int
assert type(average) is float

#move_max_to_end
#case 1
numbers = [100, 20, 30, 40, 50]
move_max_to_end(numbers)
assert numbers == [20, 30, 40, 50, 100]

#case 2
numbers = [-30, -10, -20]
move_max_to_end(numbers)
assert numbers == [-30, -20, -10]

#case 3
numbers = [30, 10, 30, 20]
move_max_to_end(numbers)
assert numbers == [10, 30, 20, 30]

#case 4
numbers = []
move_max_to_end(numbers)
assert numbers == []

#case 5
numbers = [100]
move_max_to_end(numbers)
assert numbers == [100]