#1
def remove_duplicate_words(s):
    words = s.split()
    unique_words = []
    
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    
    return ' '.join(unique_words)

#2
def stray(arr):
    return min(arr, key=arr.count)

#3
def solution(nums):
    if nums is None or len(nums) == 0:
        return []
    
    return sorted(nums)

#4
def capitals(word):
    return [i for i, char in enumerate(word) if char.isupper()]


#5
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
