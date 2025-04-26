#1
def vowel_one(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char in vowels:
            result += "1"
        else:
            result += "0"
    return result


#2
import math
 
def reduce_fraction(fraction):
     numerator, denominator = fraction
     gcd = math.gcd(numerator, denominator)     
     reduced_numerator = numerator // gcd
     reduced_denominator = denominator // gcd
     
     return [reduced_numerator, reduced_denominator]

#3
def count_letters_and_digits(s):
    count = 0
    for char in s:
        if char.isalnum(): 
            count += 1
    return count


#4
def solution(text, ending):
    return text.endswith(ending)

#5
def elimination(arr):
    for num in arr:
        if arr.count(num) > 1:
            return num  
   