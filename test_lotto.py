from lotto import exists
from lotto import distinct_random_numbers

assert exists([1,2,3], 3)==True
assert exists([1,2,3], 0)==False
assert exists([], 3)==False

assert len(distinct_random_numbers(1,49,7))==7
assert len(distinct_random_numbers(50,40,3))==3
assert len(distinct_random_numbers(-10,-5,2))==2
assert len(distinct_random_numbers(1,2,7))==0
assert len(distinct_random_numbers(-1,-2,7))==0
assert len(distinct_random_numbers(1,49,-7))==0
assert distinct_random_numbers(1, 49, 0) == []