from search_functions import *


mock_numbers = [10, 10, 10, 20, 20, 20, 30, 30, 40]

assert binary_search(mock_numbers, 20) == 3
assert binary_search(mock_numbers, 15) == -4
assert binary_search(mock_numbers, 45) == -10

assert binary_search(mock_numbers, 5) == -1

assert binary_search(mock_numbers, 10) == 0
assert binary_search(mock_numbers, 40) == 8

assert binary_search([], 20) == -1

initial = mock_numbers.copy()

test_numbers = initial.copy()
insert_sorted(test_numbers, 19)
assert test_numbers == [10, 10, 10, 19, 20, 20, 20, 30, 30, 40]

test_numbers = initial.copy()
insert_sorted(test_numbers, 20)
assert test_numbers == [10, 10, 10, 20, 20, 20, 20, 30, 30, 40]

test_numbers = initial.copy()
insert_sorted(test_numbers, 5)
assert test_numbers == [5, 10, 10, 10, 20, 20, 20, 30, 30, 40]

test_numbers = initial.copy()
insert_sorted(test_numbers, 45)
assert test_numbers == [10, 10, 10, 20, 20, 20, 30, 30, 40, 45]

test_numbers = []
insert_sorted(test_numbers, 20)
assert test_numbers == [20]