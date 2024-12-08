def custom_split(string, delimiter=" "):
    result = []
    word = ""
    
    for char in string:
        if char == delimiter:
            if word:
                result.append(word)
                word = ""
        else:
            word += char
    
    if word: 
        result.append(word)
    
    return result


string = "Hello world this is a test"
print(custom_split(string))
