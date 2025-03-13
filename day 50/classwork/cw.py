#1
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))

#2
def accum(st):
    result = []
    for i, char in enumerate(st):
        part = char.upper() + char.lower() * i
        result.append(part)
    return '-'.join(result)
