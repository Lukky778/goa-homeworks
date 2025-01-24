#1
def string_to_array(s):
    return s.split()

print(string_to_array("Robin Singh"))  
print(string_to_array("I love arrays they are my favorite")) 

#2
def string_to_number(s):
    return int(s)
    pass

print(string_to_number("1234")) 
print(string_to_number("605"))  
print(string_to_number("1405"))
print(string_to_number("-7"))  


#3
def string_to_number(s):
    return int(s)
    pass

print(string_to_number("1234")) 
print(string_to_number("605"))  
print(string_to_number("1405"))
print(string_to_number("-7"))  


#4
def fake_bin(x):
    return ''.join('0' if int(c) < 5 else '1' for c in x)

#5
def high_and_low(numbers):
    num_list = list(map(int, numbers.split())) 
    return f"{max(num_list)} {min(num_list)}"  

#6
