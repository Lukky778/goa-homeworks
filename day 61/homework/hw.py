#1
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
        
        
#2
def to_alternating_case(string):
    result = ''
    for char in string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result


#3
def correct(s):
    s = s.replace('5', 'S')
    s = s.replace('0', 'O')
    s = s.replace('1', 'I')
    return s


#4
def is_palindrome(s):
    s = s.lower() 
    return s == s[::-1] 


#5
def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}"
    else:
        return f"${salary}"
    
#6
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0


#7
def min_max(lst):
    return [min(lst), max(lst)]

