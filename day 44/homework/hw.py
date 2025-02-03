#1
def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()

#2
def row_sum_odd_numbers(n):
    return n ** 3

#3
def binary_array_to_number(arr):
    binary_str = ""
    for num in arr:
        binary_str += str(num)
    return int(binary_str, 2)

#4
def min_max(lst):
    return [min(lst), max(lst)]


#5
def divisors(integer):
    divisors_list = []
    
    for i in range(2, integer):
        if integer % i == 0: 
            divisors_list.append(i)
    
    if not divisors_list: 
        return f"{integer} is prime"
    
    return divisors_list


