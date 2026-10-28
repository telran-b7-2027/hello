from functions import *

mock_array=[10, 20, 30, 20, -1]

assert indexOf(mock_array,20)==1
assert indexOf(mock_array,-20)==-1
assert indexOf([], 20)==-1

assert lastIndexOf(mock_array,20)==3
assert lastIndexOf(mock_array,-20)==-1
assert lastIndexOf([], 20)==-1

