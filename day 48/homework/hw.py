#1
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9

#2
def invert(lst):
    result = []
    for x in lst:
        result.append(-x)
    return result

#3
def fake_bin(x):
    result = ""
    for d in x:
        if int(d) < 5:
            result += "0"
        else:
            result += "1"
    return result


#4
def string_to_array(s):
    return s.split(" ") 


#5
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    
    if p1 == "scissors":
        return "Player 1 won!" if p2 == "paper" else "Player 2 won!"
    elif p1 == "rock":
        return "Player 1 won!" if p2 == "scissors" else "Player 2 won!"
    elif p1 == "paper":
        return "Player 1 won!" if p2 == "rock" else "Player 2 won!"
    

#6
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

#7
def monkey_count(n):
    return list(range(1, n + 1))

#8
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

#9
def is_isogram(string):
    string = string.lower()  
    return len(string) == len(set(string)) 

#10
def binary_array_to_number(arr):
    result = 0
    for digit in arr:
        result = result * 2 + digit
    return result