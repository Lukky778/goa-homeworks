#1
def password(st):
    if len(st) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in st:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        
        if has_upper and has_lower and has_digit:
            return True
    return False

#2
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))

#3
def friend(x):
    return [name for name in x if len(name) == 4]

#4
def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()
