#1
def find_next_square(sq):
    root = sq ** 0.5  
    if root % 1 == 0:  
        return int((root + 1) ** 2)
    return -1 

#2
def min_max(lst):
    return [min(lst), max(lst)]

#3
def series_sum(n):
    if n == 0:
        return "0.00"

    total = 0
    for i in range(n):
        total += 1 / (1 + 3 * i)

    return f"{total:.2f}"