from array_functions import *

assert intersection([1, 2, 3], [4, 3, 1]) == [1, 3]
assert intersection([1, 2, 3], [4, 5, 6]) == []
assert intersection([], []) == []
assert intersection([1, 2, 3], []) == []
assert intersection([], [4, 3, 1]) == []

assert union([1, 2, 3], [4, 3, 1]) == [1, 2, 3, 4]
assert union([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert union([], []) == []
assert union([1, 2, 3], []) == [1, 2, 3]
assert union([], [4, 3, 1]) == [4, 3, 1]

assert difference([1, 2, 3], [4, 3, 1]) == [2]
assert difference([1, 2, 3], [4, 5, 6]) == [1, 2, 3]
assert difference([], []) == []
assert difference([1, 2, 3], []) == [1, 2, 3]
assert difference([], [4, 3, 1]) == []

assert symmetric_difference([1, 2, 3], [4, 3, 1]) == [2, 4]
assert symmetric_difference([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert symmetric_difference([], []) == []
assert symmetric_difference([1, 2, 3], [1, 2, 3]) == []

assert remove_positive_greater_or_negative_less([1, 2, 11, -3, 10, 15], 10, -3) == [1, 2, -3, 10]
assert remove_positive_greater_or_negative_less([], 10, -3) == []

assert max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]) == 100
assert max_with_negative_duplicate([10, 20, -15, -11, 20]) == -1
assert max_with_negative_duplicate([]) == -1