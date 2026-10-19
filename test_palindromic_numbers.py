from palindromic_numbers import int_reverse
from palindromic_numbers import is_digit
from palindromic_numbers import create_palindromic_list

assert is_digit(0)== True
assert is_digit(9)==True
assert is_digit(-1)==False
assert is_digit(10)==False

assert int_reverse(20) == "02"
assert int_reverse(7) == "7"
assert int_reverse(0)=="0"
assert int_reverse(-10)=="01-"
assert int_reverse(-2320)=="0232-"

assert create_palindromic_list(20,20)==[]
assert create_palindromic_list(22,22)==[22]
assert create_palindromic_list(20,22)==[22]
assert create_palindromic_list(40,22)==[33,22]
assert create_palindromic_list(-20,40)==[0,1,2,3,4,5,6,7,8,9,11,22,33]
assert create_palindromic_list(-40, -20) == []
assert create_palindromic_list(100, 112)==[101, 111]
assert create_palindromic_list(1000, 1002)==[1001]

