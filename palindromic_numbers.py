def int_reverse(num):
    current_num=abs(num)
    str_num=""
    if(current_num==0): 
        return "0"
    while current_num != 0:
            str_num += str(current_num % 10)
            current_num //= 10
    if num < 0:
        str_num += "-"
    return str_num
    
def create_palindromic_list(start, stop) :
    result = []
    step = 1 if stop - start >= 0 else -1
    for num in range(start, stop+step, step):
        if num>=0 and int(int_reverse(num))==num:
            result.append(num)
    return result
    

print(create_palindromic_list(20, 40)) #should print   [22, 33] 
print(create_palindromic_list(40, 20)) #should print   [33, 22] 