from functions import *

mock_array=[10, 20, 30, 20, -1]
mock_array1=[-10001, 10, 20, 8, -7]
mock_array2=[-10001, 10, -20, 8, -7]

assert indexOf(mock_array,20)==1
assert indexOf(mock_array,-20)==-1
assert indexOf([], 20)==-1

assert lastIndexOf(mock_array,20)==3
assert lastIndexOf(mock_array,-20)==-1
assert lastIndexOf([], 20)==-1

assert min_even(mock_array)==10
assert min_even(mock_array1)==8
assert min_even(mock_array2)==-20

