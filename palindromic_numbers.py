def int_reverse(num):
    #to avoid issues with negative numbers I added abs. minus will be handled in the end of the loop
    current_num=abs(num) #local variable to apply manipulations on reverse 
    str_num="" #target string
    while current_num >= 0:
        if is_digit(current_num):
            str_num += str(current_num) 
            if num < 0:
                str_num += "-" #add minus for negative numbers
            return str_num
        else:
            str_num += str(current_num % 10)
            current_num //= 10

def is_digit(num: int):
    return (num>=0 and num<=9) #checks if number is digit
    
def create_palindromic_list(start, stop) :
    result = []
    step = 1 if stop - start >= 0 else -1
    for num in range(start, stop+step, step):
        if num>=0 and int(int_reverse(num))==num:
            result.append(num)

    return result
    

print(create_palindromic_list(20, 40)) #should print   [22, 33] 
print(create_palindromic_list(40, 20)) #should print   [33, 22] 