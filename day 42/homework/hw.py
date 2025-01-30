#1
def sum_mix(arr):
    total = 0  
    for num in arr:  
        total += int(num)
    return total

#2
def double_char(s):
    result = ""
    for char in s:
        result += char * 2 
    return result
#3
def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)

#4
def reverse_words(s):
    words = s.split() 
    words.reverse()  
    return ' '.join(words) 

#5
def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"

    return str(int(a) + int(b))
