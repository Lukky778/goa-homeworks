#1
def digitize(n):
    result = []  
    for digit in str(n)[::-1]:  
        result.append(int(digit)) 
    return result  


#2
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

#3
def get_count(sentence):
    vowels = "aeiou"  
    count = 0        


    for char in sentence:
        if char in vowels:
            count += 1  

    return count  

#4
def filter_list(l):
    return [item for item in l if isinstance(item, int)]

