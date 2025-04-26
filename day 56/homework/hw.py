# 1
def solution(text, ending):
    return text.endswith(ending)

# 2


def even_or_odd(s):
    even_sum = 0
    odd_sum = 0

    for digit in s:
        num = int(digit)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"


# 3
def even_numbers(arr, n):
    even_numbers = [num for num in arr if num % 2 == 0]

    return even_numbers[-n:]


#4
def vowel_indices(word):
    vowels = "aeiouyAEIOUY" 
    indices = []
    
    for i, char in enumerate(word):
        if char in vowels:
            indices.append(i + 1)  
    
    return indices

#5
def geometric_sequence_elements(a, r, n):
    return ', '.join([str(a * r**i) for i in range(n)])
