#1
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


#2
def find_short(s):
    words = s.split()
    shortest = 1000  

    for word in words:
        count = 0
        for char in word:
            count += 1  
        if count < shortest:
            shortest = count 
            
    return shortest

#3
def solution(text, ending):
    text_index = 0
    ending_index = 0

    for _ in text:
        text_index += 1

    for _ in ending:
        ending_index += 1

    if ending_index == 0:
        return True

    text_position = text_index - ending_index 
    if text_position < 0:  
        return False

    text_counter = 0 
    ending_counter = 0  

    for char in text:
        if text_counter >= text_position:  
            if char != ending[ending_counter]:
                return False
            ending_counter += 1
        text_counter += 1

    return True

#4
def accum(st):
    result = []
    index = 0  

    for char in st:
        repeat_count = 0  
        for _ in st[:index + 1]: 
            repeat_count += 1

        new_str = char.upper()  
        count = 1
        for _ in range(repeat_count - 1): 
            new_str += char.lower()
            count += 1

        result.append(new_str)
        index += 1  

    return "-".join(result)