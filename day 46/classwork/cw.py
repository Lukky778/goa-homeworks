#1
def filter_list(k):
    new_list = []
    for item in k:
        if type(item) == int:
            new_list.append(item)
    return new_list


#2
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = ""

    for char in string_:
        if char not in vowels:
            result += char  

    return result

#3
def descending_order(num):
    digits = str(num)
    result = ''

    while digits:
        max_digit = max(digits)
        result += max_digit
        digits = digits.replace(max_digit, '', 1)

    return int(result)
