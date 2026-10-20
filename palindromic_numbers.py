def int_reverse(num):
    current_num=abs(num) #local variable to apply manipulations on reverse 
    str_num="" #target string
    if(current_num==0): 
        return "0"
    while current_num != 0:
            str_num += str(current_num % 10)
            current_num //= 10
    if num < 0:
        str_num += "-" #add minus for negative numbers
    return str_num
    
def create_palindromic_list(start, stop) :
    result = [] #target array
    step = 1 if stop - start >= 0 else -1 #choose loop direction
    for num in range(start, stop+step, step):
        #exclude negative numbers from the start as int_reverse should not be dependend on create_palindromic_list implementation
        if num>=0 and int(int_reverse(num))==num:
            result.append(num)
    return result
    

print(create_palindromic_list(20, 40)) #should print   [22, 33] 
print(create_palindromic_list(40, 20)) #should print   [33, 22] 