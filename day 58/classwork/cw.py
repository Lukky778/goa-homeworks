#1
def lottery(s):
    digits = []
    for char in s:
        if char.isdigit() and char not in digits:
            digits.append(char)
    if digits:
        return ''.join(digits)
    else:
        return "One more run!"


#2
def longest_word(string_of_words):
    words = string_of_words.split()
    longest = ''
    for word in words:
        if len(word) >= len(longest): 
            longest = word
    return longest


