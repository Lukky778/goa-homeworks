#1
def multi_table(number):
    result = ""
    for i in range(1, 11):
        result += f"{i} * {number} = {i * number}\n"
    return result.strip()

#2
def print_array(arr):
    result = []
    for item in arr:
        result.append(str(item))
    return ','.join(result)

#3
def string_clean(s):
    """
    Function will return the cleaned string with all numeric characters removed.
    """
    cleaned_string = ""
    for char in s:
        if not char.isdigit():
            cleaned_string += char
    return cleaned_string

#4
def remove_consecutive_duplicates(s: str) -> str:
    words = s.split()  
    result = []
    
    for word in words:
        if not result or result[-1] != word: 
            result.append(word)  
    
    return ' '.join(result) 

#5
def between_extremes(numbers):
    return max(numbers) - min(numbers)
