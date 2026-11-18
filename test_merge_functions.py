from merge_functions import merge_in_place

numbers = [-11, 3, 5, 7, -20, -10, 0, 4, 100, -80, -4, 8]
merge_in_place(numbers, 0, 4, 8)
assert numbers == [-20, -11, -10, 0, 3, 4, 5, 7, 100, -80, -4, 8]

numbers = [3, 5, 7, -11, 0, 4, -10, -20, 100, -80, -4, 8]
merge_in_place(numbers, 0, 4, 8, abs)
assert numbers == [0, 3, 4, 5, 7, -10, -11, -20, 100, -80, -4, 8]

numbers = [2, 5, 10, 3, 4, 18]
merge_in_place(numbers, 0, 3, 6)
assert numbers == [2, 3, 4, 5, 10, 18]

numbers = [100, 2, 5, 10, 3, 4, -100]
merge_in_place(numbers, 1, 3, 5)
assert numbers == [100, 2, 3, 4, 5, 10, -100]

numbers = [2, 2, 4, 1, 2, 4]
merge_in_place(numbers, 0, 3, 6)
assert numbers == [1, 2, 2, 2, 4, 4]

numbers = [1, 2, 3]
merge_in_place(numbers, 0, 0, 3)
assert numbers == [1, 2, 3]

merge_in_place(numbers, 0, 3, 3)
assert numbers == [1, 2, 3]
