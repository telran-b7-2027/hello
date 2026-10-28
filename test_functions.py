from functions import *

mock_array=[10, 20, 30, 20, -1]
mock_array1=[-10001, 10, 20, 8, -7]
mock_array2=[-10001, 10, -20, 8, -7]
mock_array4=[1, -1, 40, 50, 0]

assert indexOf(mock_array,20)==1
assert indexOf(mock_array,-20)==-1
assert indexOf([], 20)==-1

assert lastIndexOf(mock_array,20)==3
assert lastIndexOf(mock_array,-20)==-1
assert lastIndexOf([], 20)==-1

assert min_even(mock_array)==10
assert min_even(mock_array1)==8
assert min_even(mock_array2)==-20

assert count(mock_array, 20)==2
assert count(mock_array, 23)==0

assert sum_of_two_exists(mock_array4, 0)==True
assert sum_of_two_exists(mock_array4, 42)==False

assert optimal_sum_of_two_exists(mock_array4, 0)==True
assert optimal_sum_of_two_exists(mock_array4, 42)==False

