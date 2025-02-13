#1
def high_and_low(numbers):
    num_list = numbers.split() 
    highest = int(num_list[0])  
    lowest = int(num_list[0]) 

    for num in num_list: 
        n = int(num)  
        if n > highest:
            highest = n 
        if n < lowest:
            lowest = n  
    
    return f"{highest} {lowest}"

#2
def validate_pin(pin):
    count = 0 
    
    for char in pin:
        if not char.isdigit(): 
            return False
        count += 1 
    
    return count == 4 or count == 6 



#3
def odd_or_even(arr):
    total = 0
    for num in arr:
        total += num 
    
    if total % 2 != 0:
        return "odd" 
    else:
        return "even"  
    

#4
def solution(nums):
    if not nums: 
        return []
    
    nums.sort()  
    return nums  


#5
def greet(name):
    name = name.title() 
    return "Hello " + name + "!"  
