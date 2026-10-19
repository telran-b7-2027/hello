import random
def exists(numbers, num):
    for n in numbers:
        if n==num: 
            return True
    return False


def distinct_random_numbers(min_value, max_value, size):
    #apply correct order to passed values
    current_min=min(min_value, max_value)
    current_max=max(max_value, min_value)

    #check if collecting size distinct numbers is possible
    if current_max-current_min+1 < size or size <=0: 
        return []
    
    result=[] #target array

    while len(result) < size:
        num = random.randint(current_min, current_max)
        if not exists(result, num):
            result.append(num)
        #shrink range window to increase possibility of getting non-existent value
        if current_max == num:
            current_max -= 1
        if current_min == num:
            current_min += 1

    return result
    


print (distinct_random_numbers(1, 49, 7))
