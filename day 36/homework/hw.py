#1
def filter_list(l):
    return [item for item in l if isinstance(item, int)]

#2
def square_digits(num):
    digits = str(num)
    
    squared_digits = ''.join(str(int(digit)**2) for digit in digits)

    return int(squared_digits)

#3
def get_middle(s):
    length = len(s)

    if length % 2 == 1:
        return s[length // 2]
    else:
        return s[length // 2 - 1 : length // 2 + 1]

#4
def find_short(s):
    return min(len(word) for word in s.split())

#5
def solution(text, ending):
    return text.endswith(ending)
