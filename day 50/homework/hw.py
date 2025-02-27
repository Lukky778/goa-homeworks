#1
def binary_array_to_number(arr):
    result = 0
    for digit in arr:
        result = result * 2 + digit
    return result

#2
def lovefunc(flower1, flower2):
    return (flower1 % 2 != flower2 % 2)

#3
def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

#4
def longest(a1, a2):
    combined = a1 + a2
    unique_chars = []
    
    for char in combined:
        if char not in unique_chars:
            unique_chars.append(char)
    
    return ''.join(sorted(unique_chars))

#5
def invert(lst):
    return [-x for x in lst]

#6
def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

#7
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

#8
def printer_error(s):
    errors = 0
    for char in s:
        if char not in 'abcdefghijklm':
            errors += 1
    return f"{errors}/{len(s)}"

#9
def dna_to_rna(dna):
    return dna.replace('T', 'U')

#10
def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"