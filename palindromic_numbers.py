def int_reverse(num):
    return str(num)[::-1]
    
def create_palindromic_list(start, stop) :
    step = 1 if stop - start >= 0 else -1
    return [num for num in range(start, stop+step, step) if 0 <= num == int(int_reverse(num))]


print(create_palindromic_list(20, 40)) #should print   [22, 33] 
print(create_palindromic_list(40, 20)) #should print   [33, 22] 