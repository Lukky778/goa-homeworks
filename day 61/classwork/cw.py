#1
def make_upper_case(s):
     return s.upper()
 
 
 #2
def repeat_str(repeat, string):
    return string * repeat


#3
def no_space(x):
     return x.replace(' ', '')
 
 #4
def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1  
    return res


#5
def maps(a):
    return [x * 2 for x in a]


#6
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2


#7
def grader(score):
    if score > 1 or score < 0.6:
        return 'F'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'


#8
websites = ["codewars"] * 1000


#9
def double_char(s):
    result = ""
    for char in s:
        result += char * 2 
    return result


#10
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"


#11
def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}"
    else:
        return f"${salary}"


#12
def monkey_count(n):
    return list(range(1, n + 1))
