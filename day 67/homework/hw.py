#1
def double(x):
    return x * 2

#2
def string_length(s):
    return len(s)

#3
def is_odd(x):
    return x % 2 == 1

#4
def square(x):
    return x ** 2

#5
def even_squares(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num ** 2)
    return result